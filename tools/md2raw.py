"""把用 curl 下載的 markdown 原文存成 raw 檔（CLAUDE.md 第 3 節）。

用於原文本身就是 markdown 的資料，例如 GitHub Docs 在網址後加上 .md 取得的原文。
內容不做任何刪改，只在開頭加上資訊區塊與原文網址的註解。

用法（下載的檔案放在專案外的暫存資料夾）：
    curl -sSL -o page.md "<網址>.md"
    python -I tools/md2raw.py <網址> page.md --out raw/Sxx-slug.md \\
        --meta id=Sxx --meta title=... --meta url=... --meta publisher=... \\
        --meta published=... --meta license=... --meta stored=full --meta retrieved=YYYY-MM-DD

輸出：原文與存檔正文的字數（兩者應相同），以及第一段與最後一段（不含標題、清單與程式碼）。
"""
import re
import sys

WORD = re.compile(r"[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*")


def prose_paragraphs(md):
    """取出一般段落：略過標題、清單、程式碼區塊、圖片與 HTML 區塊標籤。"""
    paras, cur, fence = [], [], False
    for line in md.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if not s:
            if cur:
                paras.append(" ".join(cur))
                cur = []
            continue
        if s.startswith(("#", "* ", "- ", "![", "<div", "</div", "> [!")) or re.match(r"^\d+\.\s", s):
            if cur:
                paras.append(" ".join(cur))
                cur = []
            continue
        cur.append(s)
    if cur:
        paras.append(" ".join(cur))
    return paras


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = sys.argv[1:]
    url, path = args[0], args[1]
    out = args[args.index("--out") + 1]
    metas = [m for i, m in enumerate(args) if i > 0 and args[i - 1] == "--meta"]
    body = open(path, encoding="utf-8-sig").read()
    front = "---\n" + "\n".join(m.replace("=", ": ", 1) for m in metas) + "\n---\n\n"
    comment = f"<!-- 原文網址：{url} -->\n\n"
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(front + comment + body)
    saved = open(out, encoding="utf-8").read()
    saved_body = saved[len(front) + len(comment):]
    paras = prose_paragraphs(body)
    print("網址：", url)
    print(f"原文字數：{len(WORD.findall(body))}　存檔正文字數：{len(WORD.findall(saved_body))}　"
          f"內容{'完全相同' if saved_body == body else '不同（請檢查）'}")
    print("--- 第一段 ---\n" + paras[0])
    print("--- 最後一段 ---\n" + paras[-1])


if __name__ == "__main__":
    main()
