"""把用 curl 下載的 git-scm.com Pro Git 章節 HTML 轉成 markdown（CLAUDE.md 第 3 節）。

只取 <div id="main"> 到 <div id="nav"> 之間的正文，不做任何摘要或改寫。
其他網站的 HTML 結構不同，使用前需先擴充本程式。

用法（下載的 HTML 放在專案外的暫存資料夾）：
    curl -sSL -o page.html "<網址>"
    python -I tools/html2md.py <網址> page.html [<網址2> page2.html ...] \\
        --out raw/Sxx-slug.md --meta id=Sxx --meta title=... --meta url=... \\
        --meta publisher=... --meta published=... --meta license=... \\
        --meta stored=full --meta retrieved=YYYY-MM-DD

輸出：每個網頁的「HTML 正文字數」與「markdown 字數」（兩者應相同）、第一段與最後一段。
"""
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urljoin


class Conv(HTMLParser):
    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.on = False
        self.done = False
        self.blocks = []
        self.buf = None
        self.kind = None  # 'h1'..'h3', 'p', 'caption'
        self.prefix = ""
        self.lists = []  # [[tag, counter]]
        self.pending_li = None
        self.links = []
        self.pre = None
        self.pre_lang = ""
        self.divs = []
        self.admon = 0        # 目前在幾層 Note / Tip 等提示框裡
        self.admon_id = 0     # 提示框編號，同一個提示框的區塊要接在同一個引用區塊中
        self.plain = []  # 正文純文字，用來核對轉換前後字數

    # ---- block helpers ----
    def emit(self, md, kind):
        """輸出一個區塊；在提示框裡的區塊轉成 markdown 引用（> ）。"""
        aid = self.admon_id if self.admon else None
        if aid:
            md = "\n".join("> " + l if l else ">" for l in md.split("\n"))
        self.blocks.append((md, aid, kind))

    def markdown(self):
        out, prev = [], None
        for md, aid, _ in self.blocks:
            if out:
                out.append("\n>\n" if aid and aid == prev else "\n\n")
            out.append(md)
            prev = aid
        return "".join(out)

    def start_block(self, kind):
        self.flush()
        self.buf, self.kind = [], kind
        if self.pending_li:
            self.prefix, self.pending_li = self.pending_li, None
        else:
            self.prefix = ""

    def flush(self):
        if self.buf is None:
            return
        text = "".join(self.buf)
        lines = [l.strip() for l in text.split("\n")]
        lines = [l for l in lines if l]
        if lines:
            if self.kind in ("h1", "h2", "h3"):
                md = "#" * int(self.kind[1]) + " " + " ".join(lines)
            elif self.kind == "caption":
                # 提示框的標題（Note、Tip 等）用粗體，圖片說明用斜體
                mark = "**" if self.admon else "*"
                md = mark + " ".join(lines) + mark
            else:
                pad = " " * len(self.prefix)
                md = self.prefix + ("\n" + pad).join(lines)
            self.emit(md, self.kind)
        self.buf, self.kind, self.prefix = None, None, ""

    # ---- parser events ----
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "div" and a.get("id") == "main":
            self.on = True
            return
        if not self.on or self.done:
            return
        if tag == "div" and a.get("id") == "nav":
            self.flush()
            self.done = True
            return
        if tag == "div":
            cls = (a.get("class") or "").split()
            self.divs.append(cls)
            if "admonitionblock" in cls:
                self.flush()
                self.admon += 1
                self.admon_id += 1
            elif "title" in cls:
                self.start_block("caption")
        elif tag in ("h1", "h2", "h3", "h4"):
            self.start_block("h" + str(min(int(tag[1]), 3)))
        elif tag == "p":
            self.start_block("p")
        elif tag in ("ul", "ol"):
            self.flush()
            self.lists.append([tag, 0])
        elif tag == "li":
            self.flush()
            lst = self.lists[-1]
            lst[1] += 1
            self.pending_li = "- " if lst[0] == "ul" else f"{lst[1]}. "
        elif tag == "pre":
            self.flush()
            self.pre = []
            self.pre_lang = ""
        elif tag == "code" and self.pre is not None:
            lang = [c for c in (a.get("class") or "").split() if c.startswith("language-")]
            self.pre_lang = lang[0][len("language-"):] if lang else ""
        elif self.pre is not None:
            return  # 程式碼區塊裡的其他標籤只保留文字
        elif tag == "code":
            self._inline("`")
        elif tag == "em":
            self._inline("*")
        elif tag == "strong":
            self._inline("**")
        elif tag == "a":
            self._inline("[")
            self.links.append(urljoin(self.base, a.get("href", "")))
        elif tag == "img":
            self.flush()
            self.emit(f"![{a.get('alt', '')}]({urljoin(self.base, a.get('src', ''))})", "img")
        elif tag == "br" and self.buf is not None:
            self.buf.append("\n")

    def _inline(self, mark):
        if self.buf is None:
            self.start_block("p")
        self.buf.append(mark)

    def handle_endtag(self, tag):
        if not self.on or self.done:
            return
        if tag == "div" and self.divs:
            cls = self.divs.pop()
            if "title" in cls:
                self.flush()
            elif "admonitionblock" in cls:
                self.flush()
                self.admon -= 1
        elif tag in ("h1", "h2", "h3", "h4", "p"):
            self.flush()
        elif tag in ("ul", "ol"):
            self.flush()
            self.lists.pop()
        elif tag == "li":
            self.flush()
            self.pending_li = None
        elif tag == "pre":
            self.emit(f"```{self.pre_lang}\n" + "".join(self.pre).strip("\n") + "\n```", "code")
            self.pre = None
        elif self.pre is not None:
            return
        elif tag == "code":
            self._inline("`")
        elif tag == "em":
            self._inline("*")
        elif tag == "strong":
            self._inline("**")
        elif tag == "a" and self.links:
            self.buf.append(f"]({self.links.pop()})")

    def handle_data(self, data):
        if not self.on or self.done:
            return
        self.plain.append(data)
        if self.pre is not None:
            self.pre.append(data)
            return
        if self.buf is None:
            if not data.strip():
                return
            self.start_block("p")
        self.buf.append(data)


WORD = re.compile(r"[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*")


def md_words(md):
    # 圖片與連結的網址只在程式碼區塊外處理；程式碼區塊裡的 [x](y) 是原文文字，要照算
    parts = re.split(r"(?m)(^(?:> )?```\w*\n.*?^(?:> )?```$)", md, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"!\[([^\]]*)\]\([^)]*\)", "", parts[i])  # 圖片 alt 是屬性，HTML 正文不含，不算
        parts[i] = re.sub(r"\]\([^)]*\)", "]", parts[i])            # 連結只算文字
        parts[i] = re.sub(r"(?m)^(> )?\d+\. ", "", parts[i])        # 編號清單的數字是 markdown 加上的，不算
    md = "".join(parts)
    md = re.sub(r"(?m)^(> )?```\w*$", "", md)           # 程式碼區塊的語言標記是 markdown 加上的，不算
    md = re.sub(r"(?s)\A---\n.*?\n---\n", "", md)
    return len(WORD.findall(md))


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = sys.argv[1:]
    out = args[args.index("--out") + 1]
    metas = [m for i, m in enumerate(args) if i > 0 and args[i - 1] == "--meta"]
    pairs = args[: args.index("--out")]
    parts, report = [], []
    for url, path in zip(pairs[0::2], pairs[1::2]):
        html = open(path, encoding="utf-8").read()
        c = Conv(url)
        c.feed(html)
        c.close()
        if not c.done:
            sys.exit(f"{path}: 找不到正文結尾 <div id=\"nav\">")
        md = c.markdown()
        body_paras = [b for b, _, kind in c.blocks if kind == "p"]
        report.append({
            "url": url,
            "html_words": len(WORD.findall(" ".join(c.plain))),
            "md_words": md_words(md),
            "chars": len(md),
            "first": body_paras[0],
            "last": body_paras[-1],
        })
        parts.append(f"<!-- 原文網址：{url} -->\n\n{md}")
    front = "---\n" + "\n".join(m.replace("=", ": ", 1) for m in metas) + "\n---\n\n"
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(front + "\n\n".join(parts) + "\n")
    for r in report:
        print("=" * 60)
        print("網址：", r["url"])
        print(f"HTML 正文字數：{r['html_words']}　markdown 字數：{r['md_words']}　字元數：{r['chars']}")
        print("--- 第一段 ---\n" + r["first"])
        print("--- 最後一段 ---\n" + r["last"])


if __name__ == "__main__":
    main()
