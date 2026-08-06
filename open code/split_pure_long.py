# -*- coding: utf-8 -*-
from pathlib import Path
import re


def split_line(line: str, limit: int = 420) -> list[str]:
    if not line.startswith(">") or len(line) <= limit:
        return [line]
    body = line[1:].lstrip()
    if re.match(r"^(>>>|def |class |# |\.\.\.)", body):
        return [line]
    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", body)
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


def process(n: int) -> None:
    p = Path(f"chapters/ch{n:02d}.md")
    lines = p.read_text(encoding="utf-8").splitlines()
    out = []
    in_e = False
    fixed = 0
    pure_left = 0
    codeish_left = 0
    for l in lines:
        if l.startswith("### 英文原文"):
            in_e = True
            out.append(l)
            continue
        if l.startswith("### "):
            in_e = False
            out.append(l)
            continue
        if in_e and l.startswith(">") and len(l) > 500:
            body = l[1:].lstrip()
            code_score = sum(
                k in body for k in [">>>", " def ", " class ", " return ", "print(", "\t"]
            )
            is_pure = body.count(". ") >= 2 and code_score == 0 and not re.match(
                r"^[A-Za-z_][\w.]*\s*=", body
            )
            if is_pure:
                sp = split_line(l)
                if len(sp) > 1:
                    out.extend(sp)
                    fixed += 1
                    continue
                pure_left += 1
            else:
                codeish_left += 1
        out.append(l)
    text = "\n".join(out) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    p.write_text(text, encoding="utf-8")
    print(f"ch{n:02d} fixed={fixed} pure_left~={pure_left} codeish_long~={codeish_left} size={p.stat().st_size}")


if __name__ == "__main__":
    for n in range(36, 42):
        process(n)
