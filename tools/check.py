#!/usr/bin/env python3
"""Git 與 GitHub 入門 LLM Wiki 的規則檢查程式（對應 CLAUDE.md 第 9 節）。

用法：
    python tools/check.py        （Windows）
    python3 tools/check.py       （macOS / Linux）

有任何「錯誤」時以結束代碼 1 結束；只有「警告」時仍以 0 結束。
警告代表程式無法確定、需要人工判斷的地方，lint 時要一併看過。
只使用 Python 標準函式庫，不需要安裝任何套件。
"""
from __future__ import annotations

import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

# ──────────────────────────────────────────────
# 路徑與規則設定
# ──────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
WIKI = ROOT / "wiki"
SOURCES = WIKI / "sources"
CONCEPTS = WIKI / "concepts"
SLIDES_DIR = ROOT / "slides"
OUTLINE = SLIDES_DIR / "outline.md"
SLIDES = SLIDES_DIR / "index.html"

# 第 3 節：raw 資訊區塊欄位
RAW_FIELDS = ["id", "title", "url", "publisher", "published", "license", "stored", "retrieved"]
RAW_NAME = re.compile(r"^S(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")

# 第 3 節：允許保存全文（stored: full）的授權。key 為正規化後的授權名稱。
FULL_TEXT_LICENSES = {
    "CC BY NC SA 3.0": "《Pro Git》",
    "CC BY 4.0": "GitHub Docs",
}
EXCERPT_MAX_CHARS = 3000  # excerpt 正文超過這個字數就發出警告（可能貼了全文）

# 第 4-1 節：資料摘要頁
SOURCE_SECTIONS = ["重點", "影響的 wiki 頁面", "與其他資料的衝突或過時之處"]
SOURCE_META = ["來源", "年份", "時效風險"]
SOURCE_POINTS = (3, 6)

# 第 4-2 節：概念頁
CONCEPT_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
CONCEPT_SECTIONS = ["白話解釋", "指令範例", "新手常見誤解", "時效註記", "相關頁面", "來源"]
UNCITED_EXEMPT_SECTIONS = {"相關頁面", "來源"}

# 第 2 節：wiki 根目錄只允許這三個檔案；後兩者不檢查是否為孤立頁面
WIKI_TOP_PAGES = {"index.md", "overview.md", "log.md"}

# 第 7 節：操作紀錄
LOG_TYPES = {"setup", "ingest", "lint", "outline", "slide", "regenerate", "fix"}
LOG_FIELDS = ["做了什麼", "討論結果", "檢查結果", "待找資料"]

# 第 6 節：簡報
SLIDE_COUNT = (12, 18)
ALLOWED_EXTERNAL_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com"}

# 第 9 節：過時用語。發現新的過時用語時，請同時更新 CLAUDE.md 第 9 節與這份清單。
# 格式：(正規表示式, 用語名稱, 建議做法)
LEGACY_TERMS = [
    (re.compile(r"git\s+checkout", re.I),
     "git checkout", "切換分支請用 git switch"),
    (re.compile(r"\bmaster\b", re.I),
     "master（預設分支名稱）", "GitHub 新 repository 預設分支為 main"),
    (re.compile(r"帳號.{0,4}密碼|github.{0,8}密碼|密碼.{0,12}(?:push|推送)"
                r"|(?:push|推送).{0,12}密碼|\bpassword\b", re.I),
     "用帳號密碼推送到 GitHub", "需改用 personal access token 或 SSH"),
]

# ──────────────────────────────────────────────
# 共用工具
# ──────────────────────────────────────────────
CITE_BRACKET = re.compile(r"\[([^\[\]\n]+)\](?!\()")
CITE_BODY = re.compile(r"^\s*S\d{2}(?:\s*[,，、]\s*(?:S\d{2}|\d{4}))*\s*$")
CITE_LOOKALIKE = re.compile(r"^\s*[Ss]\s*\d")
MD_LINK = re.compile(r"\[([^\]\n]*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
HEADING2 = re.compile(r"^##\s+(.+?)\s*$")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}：{msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}：{msg}")

    def note(self, msg: str) -> None:
        self.notes.append(msg)


R = Report()


def rel(path: Path, line: int | None = None) -> str:
    s = path.relative_to(ROOT).as_posix()
    return f"{s}:{line}" if line else s


def read(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        R.error(rel(path), "不是 UTF-8 編碼")
        return None


def md_files(folder: Path) -> list[Path]:
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir() if p.is_file() and not p.name.startswith("."))


def masked_lines(text: str) -> list[str]:
    """把程式碼區塊與行內程式碼換成空白，避免裡面的文字被當成連結或來源標註。行號不變。"""
    out, in_fence = [], False
    for line in text.split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
            out.append("")
        elif in_fence:
            out.append("")
        else:
            out.append(INLINE_CODE.sub(lambda m: " " * len(m.group()), line))
    return out


def citations(line: str) -> list[list[tuple[str, str | None]]]:
    """取出一行中的來源標註，例如 [S02]、[S03, 2014]、[S02, S03]。
    每個標註回傳 [(來源編號, 年份或 None), ...]。格式可疑的標註會發警告（由呼叫者處理）。"""
    found = []
    for m in CITE_BRACKET.finditer(line):
        body = m.group(1)
        if not CITE_BODY.match(body):
            continue
        items: list[tuple[str, str | None]] = []
        for tok in re.split(r"\s*[,，、]\s*", body.strip()):
            if tok.startswith("S"):
                items.append((tok, None))
            elif items:
                items[-1] = (items[-1][0], tok)
        found.append(items)
    return found


def lookalike_citations(line: str) -> list[str]:
    return [m.group(0) for m in CITE_BRACKET.finditer(line)
            if CITE_LOOKALIKE.match(m.group(1)) and not CITE_BODY.match(m.group(1))]


def has_citation(text: str) -> bool:
    return bool(citations(text))


def has_year_citation(text: str) -> bool:
    return any(year for c in citations(text) for _, year in c)


def split_sections(lines: list[str]) -> dict[str, tuple[int, list[str]]]:
    """依 ## 標題切段。回傳 {標題: (標題行號, 內容行)}。"""
    sections: dict[str, tuple[int, list[str]]] = {}
    current = None
    for i, line in enumerate(lines, 1):
        m = HEADING2.match(line)
        if m:
            current = m.group(1)
            sections[current] = (i, [])
        elif current:
            sections[current][1].append(line)
    return sections


def normalize_license(s: str) -> str:
    s = re.sub(r"[-_]", " ", s.upper())
    return re.sub(r"\s+", " ", s).strip()


# ──────────────────────────────────────────────
# 1. raw/
# ──────────────────────────────────────────────
def parse_front_matter(path: Path, text: str) -> tuple[dict[str, str] | None, str]:
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        R.error(rel(path, 1), "開頭缺少 --- 資訊區塊")
        return None, text
    meta: dict[str, str] = {}
    for i, line in enumerate(lines[1:], 2):
        if line.strip() == "---":
            return meta, "\n".join(lines[i:])
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("\"'")
        elif line.strip():
            R.error(rel(path, i), f"資訊區塊格式錯誤：{line.strip()}")
    R.error(rel(path), "資訊區塊沒有結尾的 ---")
    return None, text


def check_raw() -> dict[str, dict[str, str]]:
    """回傳 {來源編號: 資訊區塊}。"""
    raws: dict[str, dict[str, str]] = {}
    if not RAW.is_dir():
        R.error("raw/", "資料夾不存在")
        return raws
    files = md_files(RAW)
    if not files:
        R.note("raw/ 目前沒有任何資料")
    for path in files:
        m = RAW_NAME.match(path.name)
        if not m:
            R.error(rel(path), "檔名不符合 S<兩位數編號>-<小寫英文 slug>.md")
            continue
        sid = f"S{m.group(1)}"
        if sid in raws:
            R.error(rel(path), f"編號 {sid} 重複使用")
            continue
        text = read(path)
        if text is None:
            continue
        meta, body = parse_front_matter(path, text)
        if meta is None:
            raws[sid] = {}
            continue
        raws[sid] = meta
        missing = [f for f in RAW_FIELDS if not meta.get(f)]
        if missing:
            R.error(rel(path), f"資訊區塊缺少欄位：{', '.join(missing)}")
        if meta.get("id") and meta["id"] != sid:
            R.error(rel(path), f"id 為 {meta['id']}，與檔名編號 {sid} 不符")
        if meta.get("url") and not re.match(r"^https?://", meta["url"]):
            R.error(rel(path), "url 必須以 http:// 或 https:// 開頭")
        pub = meta.get("published", "")
        if pub and not re.fullmatch(r"\d{4}|unknown", pub):
            R.error(rel(path), f"published 應為四位數年份或 unknown，目前為「{pub}」")
        ret = meta.get("retrieved", "")
        if ret and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", ret):
            R.error(rel(path), f"retrieved 應為 YYYY-MM-DD，目前為「{ret}」")
        stored = meta.get("stored", "")
        lic = normalize_license(meta.get("license", ""))
        if stored and stored not in ("full", "excerpt"):
            R.error(rel(path), f"stored 只能是 full 或 excerpt，目前為「{stored}」")
        elif stored == "full" and lic not in FULL_TEXT_LICENSES:
            R.error(rel(path), f"授權「{meta.get('license')}」不允許轉載，stored 必須是 excerpt")
        elif stored == "excerpt" and lic in FULL_TEXT_LICENSES:
            R.warn(rel(path), f"授權「{meta.get('license')}」允許轉載，依第 3 節應保存全文（stored: full）")
        if stored == "excerpt" and len(body.strip()) > EXCERPT_MAX_CHARS:
            R.warn(rel(path), f"excerpt 正文超過 {EXCERPT_MAX_CHARS} 字，請確認沒有貼上全文")
    for path in RAW.iterdir():
        if path.is_file() and not path.name.startswith(".") and path.suffix != ".md":
            R.warn(rel(path), "raw/ 中有非 .md 檔案")
    return raws


def git(*args: str) -> subprocess.CompletedProcess | None:
    try:
        return subprocess.run(["git", "-c", "core.quotepath=false", "-C", str(ROOT), *args],
                              capture_output=True, text=True, encoding="utf-8")
    except FileNotFoundError:
        return None


def check_raw_unchanged() -> None:
    """raw/ 中已經 commit 過的檔案不可被修改、刪除或改名（第 3 節「寫入後不可修改」）。"""
    r = git("rev-parse", "--is-inside-work-tree")
    if r is None:
        R.warn("raw/", "找不到 git 指令，無法檢查 raw 檔案是否被修改")
        return
    if r.returncode != 0 or r.stdout.strip() != "true":
        R.warn("raw/", "專案不是 git repository，無法檢查 raw 檔案是否被修改")
        return
    if git("rev-parse", "--verify", "-q", "HEAD").returncode != 0:
        R.note("尚未有任何 commit，略過 raw 修改檢查")
        return

    def is_raw_file(p: str) -> bool:
        return p.startswith("raw/") and not p.rsplit("/", 1)[-1].startswith(".")

    labels = {"M": "被修改", "D": "被刪除或改名", "T": "檔案類型被改變"}
    # 1. 工作目錄與暫存區相對於最新 commit 的變化
    d = git("diff", "--name-status", "--no-renames", "HEAD", "--", "raw/")
    for line in d.stdout.splitlines():
        status, _, path = line.partition("\t")
        if status[:1] in labels and is_raw_file(path):
            R.error(path, f"已經 commit 過的 raw 檔案{labels[status[:1]]}（raw 寫入後不可修改，"
                          f"要復原請執行 git restore --source=HEAD --staged --worktree -- {path}）")
    # 2. 歷史紀錄中有沒有 commit 改過已存在的 raw 檔案
    log = git("log", "--format=@%h %s", "--name-status", "--no-renames", "--diff-filter=MDT", "--", "raw/")
    commit = ""
    for line in log.stdout.splitlines():
        if line.startswith("@"):
            commit = line[1:]
        elif "\t" in line:
            status, _, path = line.partition("\t")
            if is_raw_file(path):
                R.error(path, f"commit「{commit}」中{labels.get(status[:1], '被變更')}（raw 寫入後不可修改）")


# ──────────────────────────────────────────────
# 2. wiki/sources/
# ──────────────────────────────────────────────
def check_sources(raws: dict[str, dict[str, str]]) -> None:
    raw_names = {p.name for p in md_files(RAW)}
    src_files = md_files(SOURCES) if SOURCES.is_dir() else []
    if not SOURCES.is_dir():
        R.error("wiki/sources/", "資料夾不存在")
    src_names = {p.name for p in src_files}
    for name in sorted(raw_names - src_names):
        R.error(f"wiki/sources/{name}", "raw/ 有這篇資料，但缺少對應的資料摘要頁")
    for name in sorted(src_names - raw_names):
        R.error(f"wiki/sources/{name}", "沒有對應的 raw/ 檔案（檔名需與 raw 相同）")

    for path in src_files:
        text = read(path)
        if text is None:
            continue
        lines = masked_lines(text)
        m = RAW_NAME.match(path.name)
        sid = f"S{m.group(1)}" if m else None
        h1 = next(((i, l) for i, l in enumerate(lines, 1) if l.startswith("# ")), None)
        if not h1:
            R.error(rel(path), "缺少「# Sxx｜原文標題」標題")
        else:
            hm = re.match(r"^#\s+(S\d{2})｜.+", h1[1])
            if not hm:
                R.error(rel(path, h1[0]), "標題格式應為「# Sxx｜原文標題」（全形｜）")
            elif sid and hm.group(1) != sid:
                R.error(rel(path, h1[0]), f"標題編號 {hm.group(1)} 與檔名 {sid} 不符")
        for key in SOURCE_META:
            hit = next((l for l in lines if re.match(rf"^\s*-\s*{key}\s*[：:]\s*\S", l)), None)
            if not hit:
                R.error(rel(path), f"缺少「- {key}：」欄位")
            elif key == "時效風險" and not re.search(r"[：:]\s*(高|中|低)", hit):
                R.error(rel(path), "時效風險只能填 高 / 中 / 低")
        sections = split_sections(lines)
        for sec in SOURCE_SECTIONS:
            if sec not in sections:
                R.error(rel(path), f"缺少「## {sec}」段落")
        if "重點" in sections:
            line_no, body = sections["重點"]
            n = sum(1 for l in body if re.match(r"^(?:[-*+]|\d+\.)\s+", l))
            lo, hi = SOURCE_POINTS
            if not lo <= n <= hi:
                R.error(rel(path, line_no), f"重點應為 {lo}～{hi} 點，目前 {n} 點")


# ──────────────────────────────────────────────
# 3. wiki/concepts/
# ──────────────────────────────────────────────
def text_blocks(body: list[str], start_line: int) -> list[tuple[int, str]]:
    """把段落內容切成「段落」或「清單項目」，回傳 (起始行號, 文字)。"""
    blocks: list[tuple[int, str]] = []
    cur: list[str] = []
    cur_line = 0

    def flush() -> None:
        if cur:
            blocks.append((cur_line, " ".join(s.strip() for s in cur)))
            cur.clear()

    for offset, line in enumerate(body, 1):
        n = start_line + offset
        if not line.strip() or line.lstrip().startswith("#"):  # 空行與小標題都是段落分隔
            flush()
        elif LIST_ITEM.match(line):
            flush()
            cur_line = n
            cur.append(line)
        else:
            if not cur:
                cur_line = n
            cur.append(line)
    flush()
    return blocks


def check_concepts() -> None:
    if not CONCEPTS.is_dir():
        R.error("wiki/concepts/", "資料夾不存在")
        return
    for path in md_files(CONCEPTS):
        if not CONCEPT_NAME.match(path.name):
            R.error(rel(path), "概念頁檔名必須是小寫英文 slug，例如 commit.md")
        text = read(path)
        if text is None:
            continue
        lines = masked_lines(text)
        h1 = next((i for i, l in enumerate(lines, 1) if l.startswith("# ")), None)
        if not h1:
            R.error(rel(path), "缺少「# 標題」")
        else:
            first = next(((i, l) for i, l in enumerate(lines[h1:], h1 + 1) if l.strip()), None)
            if not first or not first[1].lstrip().startswith(">"):
                R.error(rel(path, h1), "標題下方第一段必須是「> 一句話定義。[Sxx]」")
            elif not has_citation(first[1]):
                R.error(rel(path, first[0]), "一句話定義沒有標註來源")
        sections = split_sections(lines)
        present = [s for s in sections if s in CONCEPT_SECTIONS]
        for sec in CONCEPT_SECTIONS:
            if sec not in sections:
                R.error(rel(path), f"缺少「## {sec}」段落")
        if present != [s for s in CONCEPT_SECTIONS if s in present]:
            R.warn(rel(path), f"段落順序應為：{'、'.join(CONCEPT_SECTIONS)}")
        if not any(has_citation(l) for l in lines):
            R.error(rel(path), "整頁沒有任何來源標註")
        if "時效註記" in sections:
            line_no, body = sections["時效註記"]
            if not "".join(body).strip():
                R.error(rel(path, line_no), "時效註記不可留白，沒有就寫「無」")
        if "相關頁面" in sections:
            line_no, body = sections["相關頁面"]
            joined = "\n".join(body)
            if not MD_LINK.search(joined) and joined.strip() != "無":
                R.warn(rel(path, line_no), "相關頁面沒有任何相對連結（沒有就寫「無」）")
        # 每段事實陳述都要有來源：程式只能粗略判斷，所以發警告
        for sec, (line_no, body) in sections.items():
            if sec in UNCITED_EXEMPT_SECTIONS or sec not in CONCEPT_SECTIONS:
                continue
            for n, block in text_blocks(body, line_no):
                plain = LIST_ITEM.sub("", block).lstrip("> ").strip()
                if not plain or plain == "無" or plain.endswith(("：", ":")):
                    continue
                if re.fullmatch(r"[|\-:\s]+", plain):
                    continue
                if not has_citation(block):
                    R.warn(rel(path, n), f"這段可能沒有標註來源：{plain[:30]}…")


# ──────────────────────────────────────────────
# 4. 所有 wiki 頁面：來源標註、過時標註、連結、孤立頁面、index
# ──────────────────────────────────────────────
def all_wiki_pages() -> list[Path]:
    if not WIKI.is_dir():
        R.error("wiki/", "資料夾不存在")
        return []
    pages = sorted(p for p in WIKI.rglob("*.md") if not p.name.startswith("."))
    for p in pages:
        r = p.relative_to(WIKI)
        if len(r.parts) == 1 and r.name not in WIKI_TOP_PAGES:
            R.warn(rel(p), "wiki/ 根目錄只應有 index.md、overview.md、log.md")
        elif len(r.parts) > 1 and r.parts[0] not in ("sources", "concepts"):
            R.warn(rel(p), "不在第 2 節規定的 wiki 結構內")
    for name in WIKI_TOP_PAGES:
        if not (WIKI / name).is_file():
            R.error(f"wiki/{name}", "檔案不存在")
    return pages


def check_citations_and_legacy(pages: list[Path], raws: dict[str, dict[str, str]]) -> None:
    for path in pages:
        if path == WIKI / "log.md":  # 紀錄檔可能引用錯誤訊息，不檢查
            continue
        text = read(path)
        if text is None:
            continue
        lines = masked_lines(text)
        for i, line in enumerate(lines, 1):
            for c in citations(line):
                for sid, year in c:
                    if sid not in raws:
                        R.error(rel(path, i), f"來源標註 [{sid}] 在 raw/ 中不存在")
                        continue
                    pub = raws[sid].get("published", "")
                    if year and re.fullmatch(r"\d{4}", pub) and year != pub:
                        R.warn(rel(path, i), f"[{sid}, {year}] 的年份與 raw 的 published（{pub}）不同")
            for bad in lookalike_citations(line):
                R.warn(rel(path, i), f"疑似來源標註格式錯誤：{bad}（應為 [S02] 或 [S03, 2014]）")
            # 第 4-3 節：過時資訊必須同時保留新舊說法並標註年份
            if re.search(r"過時\s*[：:]", line):
                if not has_year_citation(line):
                    R.error(rel(path, i), "過時說法需標註來源與年份，例如 [S03, 2014]")
                following = []
                for nxt in lines[i:]:
                    if not nxt.strip():
                        break
                    following.append(nxt)
                cur = next((l for l in following if "現行做法" in l), None)
                if cur is None:
                    R.error(rel(path, i), "過時說法下一行必須接「現行做法：」（第 4-3 節）")
                elif not has_year_citation(cur):
                    R.error(rel(path, i), "「現行做法」需標註來源與年份，例如 [S06, 2019]")


def check_links_and_index(pages: list[Path]) -> None:
    page_set = {p.resolve() for p in pages}
    inbound: dict[Path, set[Path]] = {p.resolve(): set() for p in pages}
    index = (WIKI / "index.md").resolve()
    index_targets: set[Path] = set()

    for path in pages:
        text = read(path)
        if text is None:
            continue
        for i, line in enumerate(masked_lines(text), 1):
            for m in MD_LINK.finditer(line):
                target = m.group(2)
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
                    continue  # 外部網址或同頁錨點
                file_part = unquote(target.split("#", 1)[0])
                dest = (path.parent / file_part).resolve()
                if not dest.exists():
                    R.error(rel(path, i), f"連結斷掉：{target}")
                    continue
                if dest in page_set and dest != path.resolve():
                    inbound[dest].add(path.resolve())
                    if path.resolve() == index:
                        index_targets.add(dest)

    # 孤立頁面：除了 index.md 以外沒有任何頁面連到它
    for dest, sources in inbound.items():
        if dest.parent == WIKI.resolve() and dest.name in WIKI_TOP_PAGES:
            continue
        if not (sources - {index}):
            R.error(rel(dest), "孤立頁面：除了 index.md 以外，沒有任何 wiki 頁面連到它")

    # 每一頁都要列在 index.md
    if index in page_set:
        for p in pages:
            if p.resolve() != index and p.resolve() not in index_targets:
                R.error(rel(p), "沒有列在 wiki/index.md")
        text = read(WIKI / "index.md") or ""
        heads = {m.group(1) for l in masked_lines(text) if (m := HEADING2.match(l))}
        for sec in ("資料摘要", "概念"):
            if sec not in heads:
                R.error("wiki/index.md", f"缺少「## {sec}」分類")


# ──────────────────────────────────────────────
# 5. wiki/log.md
# ──────────────────────────────────────────────
def check_log() -> None:
    path = WIKI / "log.md"
    if not path.is_file():
        return
    text = read(path)
    if text is None:
        return
    lines = masked_lines(text)
    entries: list[tuple[int, str, list[str]]] = []
    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            m = re.match(r"^##\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2})｜([a-z]+)(?:｜.+)?\s*$", line)
            if not m:
                R.error(rel(path, i), "紀錄標題格式應為「## YYYY-MM-DD HH:MM｜類型｜對象」（全形｜）")
                entries.append((i, "", []))
                continue
            if m.group(2) not in LOG_TYPES:
                R.error(rel(path, i), f"操作類型「{m.group(2)}」不在 {'、'.join(sorted(LOG_TYPES))} 之中")
            entries.append((i, m.group(1), []))
        elif entries:
            entries[-1][2].append(line)
    last = ""
    for line_no, stamp, body in entries:
        for field in LOG_FIELDS:
            if not any(re.match(rf"^\s*-\s*{field}\s*[：:]\s*\S", l) for l in body):
                R.error(rel(path, line_no), f"這筆紀錄缺少「- {field}：」（沒有就寫「無」）")
        if stamp and last and stamp < last:
            R.warn(rel(path, line_no), "時間早於上一筆紀錄，新紀錄應加在檔案最後")
        last = stamp or last


# ──────────────────────────────────────────────
# 6. slides/outline.md 與 slides/index.html
# ──────────────────────────────────────────────
def split_paths(s: str) -> list[str]:
    return [p.strip("`") for p in re.split(r"[、,，\s]+", s) if p.strip("`")]


def check_outline() -> list[tuple[int, list[str]]] | None:
    """回傳每張投影片的 (行號, 依據清單)；沒有 outline.md 時回傳 None。"""
    if not OUTLINE.is_file():
        return None
    text = read(OUTLINE)
    if text is None:
        return None
    lines = masked_lines(text)
    slides: list[tuple[int, int, list[str]]] = []  # (行號, 編號, 內容行)
    for i, line in enumerate(lines, 1):
        m = re.match(r"^##\s*第\s*(\d+)\s*張\s*[｜|]\s*\S", line)
        if m:
            slides.append((i, int(m.group(1)), []))
        elif line.startswith("## "):
            R.warn(rel(OUTLINE, i), "標題格式應為「## 第 N 張｜標題」")
        elif slides:
            slides[-1][2].append(line)
    result = []
    for k, (line_no, num, body) in enumerate(slides, 1):
        if num != k:
            R.error(rel(OUTLINE, line_no), f"投影片編號應為 {k}，目前為 {num}")
        for field in ("教學目標", "要點", "依據"):
            if not any(re.match(rf"^\s*-\s*{field}\s*[：:]", l) for l in body):
                R.error(rel(OUTLINE, line_no), f"缺少「- {field}：」")
        basis_line = next((l for l in body if re.match(r"^\s*-\s*依據\s*[：:]", l)), "")
        basis = split_paths(re.sub(r"^\s*-\s*依據\s*[：:]", "", basis_line))
        for b in basis:
            if not (WIKI / b).is_file():
                R.error(rel(OUTLINE, line_no), f"依據的 wiki 頁面不存在：{b}")
        result.append((line_no, basis))
    lo, hi = SLIDE_COUNT
    if not lo <= len(result) <= hi:
        R.error(rel(OUTLINE), f"大綱應有 {lo}～{hi} 張投影片，目前 {len(result)} 張")
    return result


class SlideParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slides: list[dict] = []
        self.cur: dict | None = None
        self.depth = 0
        self.skip = 0
        self.in_style = False
        self.external: list[tuple[int, str]] = []

    def _external(self, url: str | None) -> None:
        if url and re.match(r"^(https?:)?//", url.strip(), re.I):
            self.external.append((self.getpos()[0], url.strip()))

    def handle_starttag(self, tag: str, attrs: list) -> None:
        a = dict(attrs)
        if tag in ("script", "img", "iframe", "video", "audio", "source"):
            self._external(a.get("src"))
        if tag == "link":
            self._external(a.get("href"))
        if tag in ("script", "style"):
            self.skip += 1
            self.in_style = tag == "style"
        if tag == "section":
            if self.cur is not None:
                self.depth += 1
            elif "slide" in (a.get("class") or "").split():
                self.cur = {"line": self.getpos()[0], "sources": a.get("data-sources"),
                            "legacy": "data-legacy" in a, "text": [], "hrefs": []}
                self.depth = 1
                return
        if self.cur is not None and tag == "a" and a.get("href"):
            self.cur["hrefs"].append(a["href"])

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
            self.in_style = False
        if tag == "section" and self.cur is not None:
            self.depth -= 1
            if self.depth == 0:
                self.slides.append(self.cur)
                self.cur = None

    def handle_data(self, data: str) -> None:
        if self.in_style:
            for m in re.finditer(r"(?:@import\s+|url\()\s*['\"]?((?:https?:)?//[^'\")\s]+)", data):
                self.external.append((self.getpos()[0], m.group(1)))
        if self.cur is not None and not self.skip:
            self.cur["text"].append(data)


def check_slides(outline: list[tuple[int, list[str]]] | None) -> None:
    if not SLIDES.is_file():
        if outline is None:
            R.note("尚未建立 slides/outline.md 與 slides/index.html，略過簡報檢查")
        else:
            R.note("尚未建立 slides/index.html，只檢查了大綱")
        return
    text = read(SLIDES)
    if text is None:
        return
    parser = SlideParser()
    parser.feed(text)
    parser.close()
    if parser.cur is not None:
        R.error(rel(SLIDES, parser.cur["line"]), "<section class=\"slide\"> 沒有結束標籤")

    for line_no, url in parser.external:
        host = urlparse(url if not url.startswith("//") else "https:" + url).hostname or ""
        if host not in ALLOWED_EXTERNAL_HOSTS:
            R.error(rel(SLIDES, line_no), f"只允許 Google Fonts，不可載入外部資源：{url}")

    slides = parser.slides
    lo, hi = SLIDE_COUNT
    if not lo <= len(slides) <= hi:
        R.error(rel(SLIDES), f"簡報應有 {lo}～{hi} 張，目前 {len(slides)} 張")
    if outline is None:
        R.error(rel(OUTLINE), "已有簡報但缺少大綱 slides/outline.md")
    elif len(outline) != len(slides):
        R.error(rel(SLIDES), f"投影片張數（{len(slides)}）與 outline.md（{len(outline)}）不一致")

    for k, s in enumerate(slides, 1):
        where = rel(SLIDES, s["line"])
        label = f"第 {k} 張"
        srcs = split_paths(s["sources"] or "")
        if not srcs:
            R.error(where, f"{label}缺少 data-sources")
        for p in srcs:
            if p.startswith(("/", "..")) or not p.endswith(".md") or not (WIKI / p).is_file():
                R.error(where, f"{label}的 data-sources 指向不存在的 wiki 頁面：{p}")
            elif not any(unquote(h).split("#")[0].endswith("wiki/" + p) for h in s["hrefs"]):
                R.warn(where, f"{label}底部沒有連到 GitHub 上的 wiki/{p}")
        if outline is not None and k <= len(outline) and srcs and set(srcs) != set(outline[k - 1][1]):
            R.error(where, f"{label}的 data-sources 與 outline.md 第 {outline[k - 1][0]} 行的「依據」不同")
        if not s["legacy"]:
            body = re.sub(r"\s+", " ", " ".join(s["text"]))
            for pattern, term, advice in LEGACY_TERMS:
                m = pattern.search(body)
                if m:
                    R.error(where, f"{label}出現過時用語「{term}」：…{m.group(0)}…"
                                   f"（{advice}；若是刻意說明舊寫法，請在該張加上 data-legacy）")


# ──────────────────────────────────────────────
# 主程式
# ──────────────────────────────────────────────
def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    raws = check_raw()
    check_raw_unchanged()
    check_sources(raws)
    check_concepts()
    pages = all_wiki_pages()
    check_citations_and_legacy(pages, raws)
    check_links_and_index(pages)
    check_log()
    check_slides(check_outline())

    print(f"檢查範圍：{len(raws)} 篇原始資料、{len(pages)} 個 wiki 頁面")
    for n in R.notes:
        print(f"  [說明] {n}")
    for w in R.warnings:
        print(f"  [警告] {w}")
    for e in R.errors:
        print(f"  [錯誤] {e}")
    if R.errors:
        print(f"結果：未通過（{len(R.errors)} 個錯誤、{len(R.warnings)} 個警告）")
        return 1
    print(f"結果：通過（0 個錯誤、{len(R.warnings)} 個警告）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
