#!/usr/bin/env python3
"""逐句核對的驗證工具（CLAUDE.md 第 5 節第 4 步）。

確認 checks/Sxx-quotes.md 中列出的每一句英文原句，都逐字存在於標註的 raw 檔。

用法：
    python tools/verify_quotes.py checks/S05-quotes.md   # 驗證一個檔案
    python tools/verify_quotes.py                        # 驗證 checks/ 中所有檔案

checks/Sxx-quotes.md 的格式：

    # S05 逐句核對

    ## 1｜sources/S05 重點 1
    - 句子：復原要小心……
    - 來源：S05
    - 原句：
      - Be careful, because you can’t always undo some of these undos.
      - This is one of the few areas in Git where you may lose some work if you do it wrong.

    ## 2｜sources/S05 重點 2
    - 句子：它會用新的 commit 完全取代舊的，所以只能用在還沒 push 的 commit。
    - 來源：S05
    - 處理：改寫，原文沒有寫「所以」的因果關係，改寫後見第 3 筆
    - 原句：（找不到）

規則：
- 每一筆以「## 編號｜頁面與位置」開頭，必須有「句子」「來源」「原句」。
- 「來源」可以有多個，以頓號或逗號分隔，原句只要存在於其中任一篇 raw 即可。
- 原句寫「（找不到）」的句子，必須有「處理」欄位，說明刪除或改寫。
- 比對時忽略空白與換行的差異，也忽略 raw 中提示框開頭的「> 」。

有比對失敗，或找不到原句卻沒寫「處理」時，以結束代碼 1 結束。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
CHECKS = ROOT / "checks"
NOT_FOUND = "（找不到）"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def load_raw(sid: str, cache: dict[str, str | None]) -> str | None:
    if sid not in cache:
        path = next(RAW.glob(f"{sid}-*.md"), None)
        if path is None:
            cache[sid] = None
        else:
            lines = [re.sub(r"^>\s?", "", l) for l in path.read_text(encoding="utf-8-sig").split("\n")]
            cache[sid] = norm(" ".join(lines))
    return cache[sid]


def parse(path: Path) -> list[dict]:
    entries: list[dict] = []
    cur: dict | None = None
    in_quotes = False
    for no, line in enumerate(path.read_text(encoding="utf-8-sig").split("\n"), 1):
        m = re.match(r"^##\s+(\d+)\s*[｜|]\s*(.+?)\s*$", line)
        if m:
            cur = {"no": int(m.group(1)), "where": m.group(2), "line": no,
                   "sentence": None, "sources": [], "action": None, "quotes": [], "not_found": False}
            entries.append(cur)
            in_quotes = False
            continue
        if cur is None:
            continue
        f = re.match(r"^- (句子|來源|處理|原句)：\s*(.*)$", line)
        if f:
            key, val = f.group(1), f.group(2).strip()
            in_quotes = key == "原句"
            if key == "句子":
                cur["sentence"] = val
            elif key == "來源":
                cur["sources"] = [s for s in re.split(r"[、,，\s]+", val) if s]
            elif key == "處理":
                cur["action"] = val
            elif key == "原句" and val == NOT_FOUND:
                cur["not_found"] = True
                in_quotes = False
            continue
        q = re.match(r"^\s+- (.+)$", line)
        if in_quotes and q:
            cur["quotes"].append(q.group(1))
    return entries


def verify(path: Path) -> bool:
    entries = parse(path)
    cache: dict[str, str | None] = {}
    errors: list[str] = []
    found = changed = 0
    for e in entries:
        where = f"{path.relative_to(ROOT).as_posix()}:{e['line']}（第 {e['no']} 筆，{e['where']}）"
        if not e["sentence"]:
            errors.append(f"{where}：缺少「句子」")
        if not e["sources"]:
            errors.append(f"{where}：缺少「來源」")
            continue
        texts = []
        for sid in e["sources"]:
            t = load_raw(sid, cache)
            if t is None:
                errors.append(f"{where}：raw/ 中沒有 {sid}")
            else:
                texts.append(t)
        if e["not_found"]:
            changed += 1
            if not e["action"]:
                errors.append(f"{where}：找不到原句，但沒有寫「處理」（刪除或改寫）")
            continue
        if not e["quotes"]:
            errors.append(f"{where}：沒有列出原句，找不到原句時請寫「- 原句：{NOT_FOUND}」並加上「處理」")
            continue
        bad = [q for q in e["quotes"] if not any(norm(q) in t for t in texts)]
        if bad:
            for q in bad:
                errors.append(f"{where}：原句不在 {'、'.join(e['sources'])} 中：{q}")
        else:
            found += 1
    print(f"{path.relative_to(ROOT).as_posix()}：核對 {len(entries)} 筆，"
          f"找到原句 {found} 筆，找不到原句而刪改 {changed} 筆，錯誤 {len(errors)} 個")
    for err in errors:
        print(f"  [錯誤] {err}")
    for e in entries:
        if e["not_found"]:
            print(f"  [刪改] 第 {e['no']} 筆 {e['where']}：{e['sentence']}\n         處理：{e['action']}")
    return not errors


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    paths = [Path(a).resolve() for a in sys.argv[1:]] or sorted(CHECKS.glob("S*-quotes.md"))
    if not paths:
        print("checks/ 中沒有任何 Sxx-quotes.md")
        return 0
    ok = True
    for p in paths:
        if not p.is_file():
            print(f"[錯誤] 找不到檔案：{p}")
            ok = False
            continue
        ok = verify(p) and ok
    print("結果：" + ("通過" if ok else "未通過"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
