# -*- coding: utf-8 -*-
"""
Merge consecutive ### 英文原文 blocks (no 中文翻译 between them) into one.
Also aggressive reflow for remaining short English prose.
Force-split remaining >600 quotes.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")


def is_code_line(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if t.startswith((">>>", "...", "$ ", "```", "#")):
        return True
    if re.match(
        r"^(def |async def |class |import |from |@|return |if |elif |else:|for |while |try:|except|with |print\(|raise |self\.|yield |pass$|case |match )",
        t,
    ):
        return True
    if re.match(r"^[A-Za-z_][\w.]*\s*=\s*\S", t) and len(t) < 100 and not t.endswith((".", "?", "!")):
        if re.search(r"""['\"\[\](){}]|True|False|None|\d""", t):
            return True
    if re.match(r"^<(__main__\.|class '|bound method|function )", t):
        return True
    return False


def ends_sentence(s: str) -> bool:
    s = s.rstrip()
    while s and s[-1] in "\"')]}”’":
        s = s[:-1]
    return bool(s) and s[-1] in ".!?"


def join_frags(frags):
    if not frags:
        return ""
    r = frags[0].strip()
    for p in frags[1:]:
        p = p.strip()
        if not p:
            continue
        if r.endswith("-") and p[:1].islower():
            r = r[:-1] + p
            continue
        if r[-1:] in "([{\"'“‘" or p[:1] in ",.;:!?)]}'\"”’":
            r += p
            continue
        r += " " + p
    r = re.sub(r"[ \t]{2,}", " ", r)
    r = re.sub(r" +([,.;:!?])", r"\1", r)
    return r.strip()


def reflow_quoted_lines(lines: list[str]) -> list[str]:
    """Given lines of an eng section body, reflow short > prose."""
    items = []
    for line in lines:
        if not line.strip():
            items.append(("BLANK", None))
            continue
        if line.startswith(">"):
            body = line[1:]
            if body.startswith(" "):
                body = body[1:]
            if body.strip().startswith("```") or is_code_line(body):
                items.append(("CODE", body if line.startswith("> ") else body))
            else:
                items.append(("PROSE", body))
        else:
            items.append(("RAW", line))

    prose_only = [b for k, b in items if k == "PROSE" and b]
    short = sum(1 for t in prose_only if len(t) <= 75)
    if short < 4:
        return lines

    out = []
    buf = []

    def flush():
        nonlocal buf
        if not buf:
            return
        text = join_frags(buf)
        buf = []
        if not text:
            return
        if len(text) > 480:
            parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[*])", text)
            b2, bl = [], 0
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                if b2 and bl + len(p) > 420:
                    out.append("> " + " ".join(b2))
                    out.append(">")
                    b2, bl = [p], len(p)
                else:
                    b2.append(p)
                    bl += len(p) + 1
            if b2:
                out.append("> " + " ".join(b2))
        else:
            out.append("> " + text)
        out.append("")

    for kind, body in items:
        if kind == "PROSE":
            buf.append(body)
        elif kind == "BLANK":
            if buf and ends_sentence(buf[-1]):
                flush()
        else:
            flush()
            if kind == "CODE":
                out.append("> " + body)
            else:
                out.append(body)
    flush()
    while out and out[-1] == "":
        out.pop()
    return out if out else lines


def merge_consecutive_eng(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out = []
    i = 0
    merges = 0
    while i < len(lines):
        if lines[i].strip() == "### 英文原文":
            out.append(lines[i])
            i += 1
            # gather first body
            body = []
            while i < len(lines) and not lines[i].startswith("### "):
                body.append(lines[i])
                i += 1
            # merge following eng blocks
            while i < len(lines) and lines[i].strip() == "### 英文原文":
                merges += 1
                i += 1
                while i < len(lines) and not lines[i].startswith("### "):
                    # skip leading blanks duplication
                    body.append(lines[i])
                    i += 1
            # reflow merged body
            body = reflow_quoted_lines(body)
            out.extend(body)
            if out and out[-1] != "":
                out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), merges


def force_split_huge(text: str, limit: int = 480) -> tuple[str, int]:
    lines = text.splitlines()
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
        if in_eng and line.startswith(">") and len(line) > limit + 2:
            body = line[1:]
            if body.startswith(" "):
                body = body[1:]
            if body.startswith("```") or is_code_line(body):
                out.append(line)
                continue
            # split on sentences; also on " - " list items and table rows roughly
            parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[*])", body)
            if len(parts) == 1 and " | " in body:
                # leave tables
                out.append(line)
                continue
            if len(parts) == 1:
                # split on ; or — 
                parts = re.split(r"(?<=;) +", body)
            if len(parts) <= 1:
                out.append(line)
                continue
            buf, bl = [], 0
            chunks = []
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                if buf and bl + len(p) > limit:
                    chunks.append(" ".join(buf))
                    buf, bl = [p], len(p)
                else:
                    buf.append(p)
                    bl += len(p) + 1
            if buf:
                chunks.append(" ".join(buf))
            if len(chunks) > 1:
                fixed += 1
                for j, ch in enumerate(chunks):
                    out.append("> " + ch)
                    if j < len(chunks) - 1:
                        out.append(">")
            else:
                out.append(line)
        else:
            out.append(line)
    return "\n".join(out), fixed


def reflow_all_eng(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out = []
    i = 0
    fixed = 0
    while i < len(lines):
        if lines[i].strip() == "### 英文原文":
            out.append(lines[i])
            i += 1
            if i < len(lines) and lines[i].strip() == "":
                out.append(lines[i])
                i += 1
            body = []
            while i < len(lines) and not lines[i].startswith("### "):
                body.append(lines[i])
                i += 1
            newb = reflow_quoted_lines(body)
            if newb != body:
                fixed += 1
            out.extend(newb)
            if out and out[-1] != "":
                out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), fixed


def process(path: Path):
    text = path.read_text(encoding="utf-8")
    text, m = merge_consecutive_eng(text)
    text, r = reflow_all_eng(text)
    text, r2 = reflow_all_eng(text)
    text, s = force_split_huge(text)
    text, s2 = force_split_huge(text)
    text = re.sub(r"(### 英文原文)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 中文翻译)\n>", r"\1\n\n>", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")
    lines = path.read_text(encoding="utf-8").splitlines()
    eng = sum(1 for L in lines if L.strip() == "### 英文原文")
    zh = sum(1 for L in lines if L.strip() == "### 中文翻译")
    deep = sum(1 for L in lines if L.strip() == "### 深度理解")
    in_eng = False
    huge = short = 0
    for L in lines:
        if L.strip() == "### 英文原文":
            in_eng = True
            continue
        if L.startswith("### "):
            in_eng = False
            continue
        if in_eng and L.startswith(">"):
            b = L[1:].strip()
            if not b or is_code_line(b) or b.startswith("```"):
                continue
            if len(b) > 600:
                huge += 1
            elif len(b) <= 55 and b[:1].islower():
                short += 1
    return path.name, m, r + r2, s + s2, eng, zh, deep, huge, short


def main():
    files = sorted(ROOT.glob("ch*.md")) + sorted(ROOT.glob("appendix_*.md")) + [ROOT / "about_the_author.md"]
    print(f"{'file':18s} {'mg':>3} {'rf':>3} {'sp':>3} eng zh deep huge sh")
    mis = []
    for p in files:
        if not p.exists():
            continue
        row = process(p)
        name, m, r, s, eng, zh, deep, huge, short = row
        flag = "Y" if eng != zh else " "
        print(f"{name:18s} {m:3d} {r:3d} {s:3d} {eng:3d} {zh:3d} {deep:4d} {huge:4d} {short:3d} {flag}")
        if eng != zh:
            mis.append((name, eng, zh))
    print("mismatches:", mis)


if __name__ == "__main__":
    main()
