# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path("chapters/ch41.md")
text = p.read_text(encoding="utf-8")
lines = text.splitlines()
out = []
in_eng = False
for line in lines:
    if line.startswith("### 英文原文"):
        in_eng = True
        out.append(line)
        continue
    if line.startswith("### "):
        in_eng = False
        out.append(line)
        continue
    if in_eng and line.startswith("> ") and len(line) > 900:
        body = line[2:]
        parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'])", body)
        paras = []
        buf = []
        for s in parts:
            buf.append(s)
            if len(buf) >= 2 or sum(len(x) for x in buf) > 350:
                paras.append(" ".join(buf))
                buf = []
        if buf:
            paras.append(" ".join(buf))
        for i, para in enumerate(paras):
            out.append("> " + para.strip())
            if i < len(paras) - 1:
                out.append(">")
        continue
    out.append(line)

new = "\n".join(out)
new = re.sub(r"\n---\n\n---\n", "\n---\n", new)
new = re.sub(r"\n{3,}", "\n\n", new)
if not new.endswith("\n"):
    new += "\n"
p.write_text(new, encoding="utf-8")
print("ok", p.stat().st_size)
