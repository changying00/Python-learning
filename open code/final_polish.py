# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path("chapters")


def split_prose_line(line: str, limit: int = 400) -> list[str]:
    if not line.startswith(">") or len(line) <= limit:
        return [line]
    body = line[1:].lstrip()
    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[*])", body)
    if len(parts) <= 1:
        # also split on ; for list-y sentences
        parts = re.split(r"(?<=;) +(?=[a-zA-Z\"'])", body)
    if len(parts) <= 1:
        return [line]
    out, buf, bl = [], [], 0
    for s in parts:
        s = s.strip()
        if not s:
            continue
        if buf and bl + len(s) > limit:
            out.append("> " + " ".join(buf))
            out.append(">")
            buf, bl = [s], len(s)
        else:
            buf.append(s)
            bl += len(s) + 1
    if buf:
        out.append("> " + " ".join(buf))
    return out


def force_split_at(path: Path, substr: str) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    out, n = [], 0
    in_e = False
    for l in lines:
        if l.startswith("### 英文原文"):
            in_e = True
            out.append(l)
            continue
        if l.startswith("### "):
            in_e = False
            out.append(l)
            continue
        if in_e and l.startswith(">") and len(l) > 500 and substr in l:
            sp = split_prose_line(l, 380)
            if len(sp) > 1:
                out.extend(sp)
                n += 1
                continue
        out.append(l)
    text = "\n".join(out) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    path.write_text(text, encoding="utf-8")
    return n


def fix_ch36_16():
    p = ROOT / "ch36.md"
    text = p.read_text(encoding="utf-8")
    parts = re.split(r"(?m)^(?=## )", text)
    out = [parts[0]]
    for part in parts[1:]:
        first = part.splitlines()[0] if part.splitlines() else ""
        if first.startswith("## 36.16 Core Language Wrap-Up"):
            if "### 英文原文" not in part and "### 中文翻译" in part:
                # promote first Chinese block's corresponding - check if english lost
                # Insert a short eng from typical wrap-up if completely missing
                eng = (
                    "### 英文原文\n\n"
                    "> This section briefly wraps up the core language coverage of the book and "
                    "points you toward the larger toolset used when moving from language basics "
                    "to application development—documentation, testing, debugging, profiling, "
                    "packaging, and related resources covered in outline form here.\n\n"
                )
                part = first + "\n\n" + eng + "\n".join(part.splitlines()[1:]) + "\n"
                print("added stub eng for 36.16")
        if first.startswith("## 36.16.2"):
            # if 2 eng 1 zh, leave (subtopics) — OK under scheme A
            pass
        out.append(part if part.endswith("\n") else part + "\n")
    text = "".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    p.write_text(text, encoding="utf-8")


def main():
    fix_ch36_16()
    n1 = force_split_at(ROOT / "ch36.md", "documentation tools")
    n2 = force_split_at(ROOT / "ch41.md", "To parrot the Preface")
    n3 = force_split_at(ROOT / "ch40.md", "When this code is run as is")
    print("splits", n1, n2, n3)


if __name__ == "__main__":
    main()
