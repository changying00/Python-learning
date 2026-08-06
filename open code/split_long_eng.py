# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def is_codeish(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if t.startswith((">>>", "...", "$ ", "```")):
        return True
    if re.match(r"^(def|async def|class|import|from|@)\b", t):
        return True
    return False


def split_long(line: str, limit: int = 450) -> list:
    if not line.startswith(">"):
        return [line]
    body = line[1:]
    if body.startswith(" "):
        body = body[1:]
    if len(line) <= limit or is_codeish(body) or body.startswith("```"):
        return [line]
    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", body)
    if len(parts) <= 1:
        return [line]
    out = []
    buf = []
    bl = 0
    for s in parts:
        s = s.strip()
        if not s:
            continue
        if buf and (bl + len(s) > limit or len(buf) >= 2):
            out.append("> " + " ".join(buf))
            out.append(">")
            buf = [s]
            bl = len(s)
        else:
            buf.append(s)
            bl += len(s) + 1
    if buf:
        out.append("> " + " ".join(buf))
    return out if out else [line]


def process(name: str):
    p = Path("chapters") / name
    lines = p.read_text(encoding="utf-8").splitlines()
    out = []
    in_eng = False
    fixed = 0
    for line in lines:
        if line.strip() == "### 英文原文":
            in_eng = True
            out.append(line)
            continue
        if line.startswith("### "):
            in_eng = False
            out.append(line)
            continue
        if in_eng and line.startswith(">") and len(line) > 550:
            new = split_long(line, 450)
            if new != [line]:
                fixed += 1
            out.extend(new)
        else:
            out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    p.write_text(text, encoding="utf-8")

    lines = p.read_text(encoding="utf-8").splitlines()
    in_eng = False
    huge = longq = shortq = 0
    for L in lines:
        if L.strip() == "### 英文原文":
            in_eng = True
            continue
        if L.startswith("### "):
            in_eng = False
            continue
        if in_eng and L.startswith(">"):
            b = L[1:].strip()
            if not b:
                continue
            if len(b) > 600:
                huge += 1
            elif len(b) > 100:
                longq += 1
            else:
                shortq += 1
    print(f"{name}: fixed={fixed} long={longq} short={shortq} huge={huge} size={p.stat().st_size}")


if __name__ == "__main__":
    process("ch38.md")
    process("ch40.md")
