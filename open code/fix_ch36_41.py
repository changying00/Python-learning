# -*- coding: utf-8 -*-
"""
Phase 1+2 for ch36-ch41:
- mechanical format (title, blanks, ---)
- split long English blockquotes
- renumber ## section headers
"""
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")


def is_codeish(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if t.startswith((">>>", "...", "$ ", "```", "# ", "##")):
        return True
    if re.match(r"^(def|async def|class|import|from|@)\b", t):
        return True
    if re.match(r"^(return|if |elif |else:|for |while |try:|except|with |yield |raise |pass\b)", t):
        return True
    if t.startswith(("<!", "<html", "<head", "<body", "<meta", "<table", "<td", "<div", "</")):
        return True
    if t in {")", "]", "}", "),", "],", "},", '"""', "'''", "):", "(", "[", ":", "..."}:
        return True
    if re.match(r"^[A-Za-z_][\w.]*\s*=\s*\S", t) and not t.endswith((".", "?", "!")) and len(t) < 120:
        if re.search(r"""['\"\[\](){}]|True|False|None|\d""", t):
            return True
    return False


def split_long_quote(line: str, limit: int = 420) -> list[str]:
    """Split a single > quote line into multiple > paragraphs by sentences."""
    if not line.startswith(">"):
        return [line]
    prefix = "> "
    body = line[1:]
    if body.startswith(" "):
        body = body[1:]
    if len(line) <= limit or is_codeish(body):
        return [line]
    # bold title lines keep as-is if short enough after bold
    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", body)
    if len(parts) <= 1:
        # try Chinese-unfriendly: also split on ; when very long
        if len(body) > limit * 1.5:
            parts = re.split(r"(?<=;) +(?=[A-Z\"'])", body)
        if len(parts) <= 1:
            return [line]

    out_paras = []
    buf = []
    buf_len = 0
    for s in parts:
        s = s.strip()
        if not s:
            continue
        if buf and (buf_len + len(s) > limit or len(buf) >= 2):
            out_paras.append(" ".join(buf))
            buf = [s]
            buf_len = len(s)
        else:
            buf.append(s)
            buf_len += len(s) + 1
    if buf:
        out_paras.append(" ".join(buf))

    result = []
    for i, para in enumerate(out_paras):
        result.append(prefix + para)
        if i < len(out_paras) - 1:
            result.append(">")
    return result if result else [line]


def reflow_english_sections(text: str) -> str:
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "### 英文原文":
            out.append(line)
            i += 1
            # optional blank
            if i < len(lines) and lines[i].strip() == "":
                out.append(lines[i])
                i += 1
            while i < len(lines) and not lines[i].startswith("### "):
                cur = lines[i]
                if cur.startswith(">") and len(cur) > 500:
                    out.extend(split_long_quote(cur))
                else:
                    out.append(cur)
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def fix_mechanical(text: str, chap: int) -> str:
    text = re.sub(rf"^# 第\s*{chap}\s*章", f"# 第 {chap} 章", text, count=1, flags=re.M)
    text = re.sub(
        r"(> \*\*本章地位\*\*[^\n]*)\n+---",
        r"\1\n\n---",
        text,
        count=1,
    )
    text = re.sub(r"(### 英文原文)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 中文翻译)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 中文翻译)\n#", r"\1\n\n#", text)
    text = re.sub(r"(### 深度理解)\n-", r"\1\n\n-", text)
    text = re.sub(r"(### 代码分析)\n```", r"\1\n\n```", text)
    text = re.sub(r"(### 代码分析)\n-", r"\1\n\n-", text)

    # Ensure --- before each ## N.M (except first after meta) and before # 本章总结
    def ensure_hr_before_h2(m):
        prev = m.group(1)
        hdr = m.group(2)
        if prev.rstrip().endswith("---"):
            return m.group(0)
        return prev.rstrip() + "\n\n---\n\n" + hdr

    text = re.sub(
        r"([^\n])\n+(## \d+\.\d+[^\n]*)",
        lambda m: m.group(1) + "\n\n---\n\n" + m.group(2)
        if not m.group(0).count("---")
        else m.group(0),
        text,
    )
    # cleaner approach: split by ## headers
    lines = text.splitlines()
    out = []
    for idx, line in enumerate(lines):
        if line.startswith("## ") and out:
            # look back skip blanks
            j = len(out) - 1
            while j >= 0 and out[j].strip() == "":
                j -= 1
            if j >= 0 and out[j].strip() != "---" and not (
                idx > 0 and lines[0].startswith("# ") and j < 6 and "本章地位" in "\n".join(out)
            ):
                # always separate major sections
                if out[j].strip() != "---":
                    # remove trailing blanks then add hr
                    while out and out[-1].strip() == "":
                        out.pop()
                    if out and out[-1].strip() != "---":
                        out.append("")
                        out.append("---")
                        out.append("")
        if line.startswith("# 本章总结") and out:
            while out and out[-1].strip() == "":
                out.pop()
            if out and out[-1].strip() != "---":
                out.append("")
                out.append("---")
                out.append("")
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\n---\n\n---\n", "\n---\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    return text


# ---------- numbering maps ----------

def renumber_by_order(text: str, chap: int, skip_prefixes=None) -> str:
    """Assign chap.N sequentially to all ## headers except tech/advice."""
    skip_prefixes = skip_prefixes or ("## 技术拓展", "## 学习建议")
    lines = text.splitlines()
    n = 0
    out = []
    for line in lines:
        if line.startswith("## "):
            if any(line.startswith(s) for s in skip_prefixes):
                out.append(line)
                continue
            n += 1
            rest = line[3:].strip()
            # strip existing leading number like 37.2 / 2.3 / 40.1 / 8.
            rest = re.sub(r"^\d+(\.\d+)*\s+", "", rest)
            out.append(f"## {chap}.{n} {rest}")
        else:
            out.append(line)
    return "\n".join(out)


def apply_exact_map(text: str, mapping: list[tuple[str, str]]) -> tuple[str, int]:
    """Apply exact full-line replacements; mapping is list of (old, new)."""
    lines = text.splitlines()
    table = {a: b for a, b in mapping}
    count = 0
    out = []
    for line in lines:
        if line in table:
            out.append(table[line])
            count += 1
        else:
            out.append(line)
    return "\n".join(out), count


def fix_ch38_partial(text: str) -> str:
    mapping = [
        ("## Chapter Summary（章节小结）", "## 38.6 Chapter Summary（章节小结）"),
        ("## Test Your Knowledge: Quiz（知识测验：测验）", "## 38.7 Test Your Knowledge: Quiz（知识测验：测验）"),
        ("## 38.8 Test Your Knowledge: Answers（知识测验：答案）", "## 38.8 Test Your Knowledge: Answers（知识测验：答案）"),
    ]
    text, n = apply_exact_map(text, mapping)
    print(f"  ch38 exact map hits={n}")
    return text


def fix_ch40_partial(text: str) -> str:
    # Use sequential renumber for reliability on remaining unnumbered
    return renumber_by_order(text, 40)


def fix_ch37(text: str) -> str:
    return renumber_by_order(text, 37)


def fix_ch39(text: str) -> str:
    return renumber_by_order(text, 39)


def fix_ch36(text: str) -> str:
    # already mostly numbered; normalize via sequential to fix any strays
    return renumber_by_order(text, 36)


def fix_ch41(text: str) -> str:
    return renumber_by_order(text, 41)


def process(chap: int) -> None:
    path = ROOT / f"ch{chap:02d}.md"
    text = path.read_text(encoding="utf-8")
    orig_size = len(text)

    text = reflow_english_sections(text)

    if chap == 38:
        text = fix_ch38_partial(text)
        # still renumber all to be safe/consistent
        text = renumber_by_order(text, 38)
    elif chap == 39:
        text = fix_ch39(text)
    elif chap == 40:
        text = fix_ch40_partial(text)
    elif chap == 37:
        text = fix_ch37(text)
    elif chap == 36:
        text = fix_ch36(text)
    elif chap == 41:
        text = fix_ch41(text)

    text = fix_mechanical(text, chap)
    # second pass reflow after mechanical (in case)
    text = reflow_english_sections(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"

    path.write_text(text, encoding="utf-8")
    print(f"ch{chap:02d}: {orig_size} -> {len(text)} bytes ({path.stat().st_size} file)")


def main():
    targets = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else list(range(36, 42))
    for chap in targets:
        process(chap)


if __name__ == "__main__":
    main()
