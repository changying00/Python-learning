# -*- coding: utf-8 -*-
"""Post-polish English sections in ch38.md / ch40.md."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CHAP = Path(__file__).resolve().parent / "chapters"


def is_codeish_line(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if t.startswith((">>>", "...", "$ ", "#")):
        return True
    if re.match(r"^(def|async def|class|import|from|return|yield|raise|pass|if |elif |else:|for |while |try:|except|with |@)\b", t):
        return True
    if re.match(r"^[A-Za-z_][\w.]*\s*=\s*\S", t) and not t.endswith((".", "?", "!")) and len(t) < 100:
        return True
    if re.match(r"^[A-Za-z_][\w.]*\([^)]*\)\s*$", t) and len(t) < 80:
        return True
    if t in {")", "]", "}", "):", "...", "…", "pass"}:
        return True
    if re.match(r"^Example\s+\d+", t):
        return True
    if t.startswith(("Traceback", "AttributeError", "TypeError", "ValueError")):
        return True
    return False


def split_sentences(text: str, limit: int = 320) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return [text] if text else []
    # Also split before inline code-ish fragments stuck in prose
    text = re.sub(r"\s+(?=(?:person\.|self\.|[A-Z][a-zA-Z]+\(|def |class |>>> ))", "\n", text)
    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[]|__|Note |TIP|WARNING)", text)
    out, buf, blen = [], [], 0
    for s in parts:
        for piece in s.split("\n"):
            piece = piece.strip()
            if not piece:
                continue
            if buf and (blen + len(piece) > limit or (is_codeish_line(piece) and buf and not is_codeish_line(buf[-1]))):
                out.append(" ".join(buf))
                buf, blen = [piece], len(piece)
            else:
                buf.append(piece)
                blen += len(piece) + 1
    if buf:
        out.append(" ".join(buf))
    # second pass: if still huge, hard-wrap on ; : or —
    final = []
    for p in out:
        if len(p) <= limit * 1.2:
            final.append(p)
            continue
        bits = re.split(r"(?<=[;:]) +", p)
        cur = ""
        for b in bits:
            if cur and len(cur) + len(b) > limit:
                final.append(cur.strip())
                cur = b
            else:
                cur = (cur + " " + b).strip()
        if cur:
            final.append(cur)
    return final or [text]


def extract_inline_code(para: str) -> list[tuple[str, str]]:
    """
    Split a prose paragraph that has trailing/leading code crumbs into
    alternating prose/code segments. Conservative.
    """
    s = para.strip()
    # Pattern: prose ...: code-like rest without sentence end
    # Pull out sequences of codeish tokens jammed together
    # e.g. "syntax: person.name # Fetch ... person.name = value # Change ... In most cases"
    m = re.search(
        r"^(.*?:\s*)([A-Za-z_][\w.]*\s*(?:=|\(|#).*)$",
        s,
    )
    if m and len(m.group(2)) > 20:
        head, tail = m.group(1).strip(), m.group(2).strip()
        # find where prose resumes in tail (capital word after code)
        m2 = re.search(r"\s+(?=[A-Z][a-z]+(?:\s+[a-z]+){3,})", tail)
        if m2:
            code, rest = tail[: m2.start()].strip(), tail[m2.start():].strip()
            segs = []
            if head:
                segs.append(("prose", head))
            if code:
                segs.append(("code", code.replace(" # ", "\n# ").replace(" person.", "\nperson.")))
            if rest:
                segs.extend(extract_inline_code(rest) or [("prose", rest)])
            return segs
    return [("prose", s)]


def polish_english_block(lines: list[str]) -> list[str]:
    """lines are raw lines inside 英文原文 section (may include blanks), without the heading."""
    # Parse existing > quotes and code fences into blocks
    blocks: list[tuple[str, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if not line.startswith(">"):
            i += 1
            continue
        body = line[1:]
        if body.startswith(" "):
            body = body[1:]
        if body.strip() == "```python":
            code = []
            i += 1
            while i < len(lines):
                ln = lines[i]
                b = ln[1:] if ln.startswith(">") else ln
                if b.startswith(" "):
                    b = b[1:]
                if b.strip() == "```":
                    i += 1
                    break
                code.append(b)
                i += 1
            blocks.append(("code", "\n".join(code)))
            continue
        if body.strip() == "```":
            i += 1
            continue
        if body.strip():
            blocks.append(("prose", body.strip()))
        i += 1

    # Rebuild: split huge prose, extract inline code, merge adjacent tiny prose
    new_blocks: list[tuple[str, str]] = []
    for kind, text in blocks:
        if kind == "code":
            # drop empty
            if text.strip():
                # if code block is single weak line and next will be prose, keep
                new_blocks.append(("code", text))
            continue
        for seg_kind, seg in extract_inline_code(text):
            if seg_kind == "code":
                new_blocks.append(("code", seg))
            else:
                for chunk in split_sentences(seg, 320):
                    # if chunk itself is codeish short, emit as code
                    if is_codeish_line(chunk) and len(chunk) < 100 and not chunk.endswith((".", "?", "!")):
                        new_blocks.append(("code", chunk))
                    else:
                        new_blocks.append(("prose", chunk))

    # merge consecutive code
    merged: list[tuple[str, str]] = []
    for kind, text in new_blocks:
        if merged and kind == "code" and merged[-1][0] == "code":
            merged[-1] = ("code", merged[-1][1] + "\n" + text)
        elif merged and kind == "prose" and merged[-1][0] == "prose" and len(merged[-1][1]) < 60 and len(text) < 60:
            # don't merge short+short if both look like code leftovers
            if is_codeish_line(merged[-1][1]) or is_codeish_line(text):
                merged.append((kind, text))
            else:
                merged[-1] = ("prose", merged[-1][1] + " " + text)
        else:
            merged.append((kind, text))

    # emit
    out: list[str] = []
    for kind, text in merged:
        if kind == "code":
            out.append(">")
            out.append("> ```python")
            for cl in text.splitlines():
                out.append(f"> {cl}")
            out.append("> ```")
            out.append(">")
        else:
            out.append(f"> {text}")
            out.append(">")
    while out and out[-1] == ">":
        out.pop()
    return out


def process_file(path: Path) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    i = 0
    fixed = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "### 英文原文":
            out.append(line)
            i += 1
            if i < len(lines) and lines[i].strip() == "":
                out.append(lines[i])
                i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("### "):
                block.append(lines[i])
                i += 1
            new_block = polish_english_block(block)
            if new_block != block:
                fixed += 1
            out.extend(new_block)
            out.append("")
            continue
        out.append(line)
        i += 1

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")

    # stats
    long_q = short_q = huge = 0
    in_eng = in_code = False
    for line in text.splitlines():
        if line.strip() == "### 英文原文":
            in_eng, in_code = True, False
            continue
        if line.startswith("### "):
            in_eng = False
            continue
        if not in_eng or not line.startswith(">"):
            continue
        body = line[1:].strip()
        if body.startswith("```"):
            in_code = body.startswith("```python")
            if body == "```":
                in_code = False
            continue
        if in_code or not body:
            continue
        if len(body) > 420:
            huge += 1
        if len(body) > 100:
            long_q += 1
        elif len(body) < 45:
            short_q += 1
    print(f"{path.name}: fixed_sections={fixed} eng_long={long_q} eng_short={short_q} eng_huge={huge}")


def main():
    for name in ("ch38.md", "ch40.md"):
        process_file(CHAP / name)
    # show sample around Why Manage
    p = CHAP / "ch38.md"
    lines = p.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if "Why Manage Attributes" in line:
            for j in range(i, min(i + 45, len(lines))):
                print(f"{j+1:4d}|{lines[j][:120]}")
            break


if __name__ == "__main__":
    main()
