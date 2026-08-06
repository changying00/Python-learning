# -*- coding: utf-8 -*-
"""Phase 4b: finish remaining long lines + ch36.16 eng header."""
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")


def re_sub_n(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def force_split_line(line: str, limit: int = 450) -> list[str]:
    if not line.startswith(">") or len(line) <= limit:
        return [line]
    body = line[1:].lstrip()

    # Prefer sentence boundaries
    splitters = [
        r"(?<=[.!?]) +(?=[A-Z\"'(\[$])",
        r"(?<=;) +(?=[A-Z\"'(\[])",
        r" — (?=[A-Z])",
        r"(?<=[)\]}'\"`]) +(?=[A-Z])",
        r"(?<=:) +(?=[A-Z\"'(\[$#])",
        r" (?=\$ python)",
        r" (?=# )",
        r"(?<=[a-z]) (?=[A-Z][a-z]+ [a-z])",  # weak camel break
    ]
    parts = [body]
    for sp in splitters:
        new_parts = []
        for p in parts:
            if len(p) <= limit:
                new_parts.append(p)
                continue
            bits = re.split(sp, p)
            if len(bits) > 1:
                new_parts.extend(bits)
            else:
                new_parts.append(p)
        parts = new_parts

    # hard wrap remaining monsters near limit on spaces
    final = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if len(p) <= limit:
            final.append(p)
            continue
        while len(p) > limit:
            cut = p.rfind(" ", 0, limit)
            if cut < limit // 3:
                cut = limit
            final.append(p[:cut].rstrip())
            p = p[cut:].lstrip()
        if p:
            final.append(p)

    out = []
    for i, para in enumerate(final):
        out.append("> " + para)
        if i < len(final) - 1:
            out.append(">")
    return out or [line]


def split_all_long(text: str, limit: int = 450) -> str:
    lines = text.splitlines()
    out = []
    in_e = False
    for line in lines:
        if line.startswith("### 英文原文"):
            in_e = True
            out.append(line)
            continue
        if line.startswith("### "):
            in_e = False
            out.append(line)
            continue
        if in_e and line.startswith(">") and len(line) > limit:
            out.extend(force_split_line(line, limit))
        else:
            out.append(line)
    return "\n".join(out) + "\n"


def fix_ch36():
    p = ROOT / "ch36.md"
    text = p.read_text(encoding="utf-8")

    # 36.16: add ### 英文原文 before leading quotes
    def mut(part: str) -> str:
        lines = part.splitlines()
        if any(l.strip() == "### 英文原文" for l in lines):
            return part
        # insert after title blank
        # find first content line
        out = [lines[0], ""]
        out.append("### 英文原文")
        out.append("")
        # rest skipping initial blanks after title
        i = 1
        while i < len(lines) and lines[i].strip() == "":
            i += 1
        out.extend(lines[i:])
        return "\n".join(out) + "\n"

    parts = re.split(r"(?m)^(?=## )", text)
    newp = [parts[0]]
    for part in parts[1:]:
        first = part.splitlines()[0] if part.splitlines() else ""
        if first.startswith("## 36.16 ") and "36.16." not in first:
            part = mut(part)
        newp.append(part if part.endswith("\n") else part + "\n")
    text = "".join(newp)

    # peel Chinese glued in long eng line around tools section
    text = re.sub(
        r"(Pyflakes)[，,]相当于 C 的 lint[）)]?",
        r"\1)",
        text,
    )
    # more mixed CJK in eng - peel common patterns
    def peel_line(m):
        line = m.group(0)
        # drop CJK tails
        line2 = re.sub(r"[（(]?[\u4e00-\u9fff][^A-Za-z]{0,40}$", "", line)
        return line2

    text = split_all_long(text, 480)
    text = re_sub_n(text)
    p.write_text(text, encoding="utf-8")
    print("ch36", p.stat().st_size)


def fix_rest():
    for n in (38, 40, 41):
        p = ROOT / f"ch{n:02d}.md"
        text = p.read_text(encoding="utf-8")
        for _ in range(4):
            text = split_all_long(text, 450)
        text = re_sub_n(text)
        p.write_text(text, encoding="utf-8")
        print(f"ch{n}", p.stat().st_size)


if __name__ == "__main__":
    fix_ch36()
    fix_rest()
    import validate_ch36_41

    print("--- validate ---")
    validate_ch36_41.report()
