# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path("chapters/ch41.md")
text = p.read_text(encoding="utf-8")

text = re.sub(
    r"^# 第\s*41\s*章[：:].*",
    "# 第 41 章：All Good Things（美好的终结）",
    text,
    count=1,
    flags=re.M,
)
text = re.sub(
    r"> \*\*本章地位\*\*[^\n]*",
    "> **本章地位**：全书收官章——不再教新语法，而是回望 Python 的演化速度、工具箱膨胀与开源治理张力，并以结业证书脚本收尾。读完应能把“会写 Python”提升为“会判断版本与特性是否值得”。",
    text,
    count=1,
)
text = re.sub(
    r"(> \*\*本章地位\*\*[^\n]*)\n+---",
    r"\1\n\n---",
    text,
    count=1,
)

repls = [
    ("## Chapter Introduction（章节导言）", "## 41.1 开篇引言"),
    ("## The Python Tsunami（Python 海啸）", "## 41.2 The Python Tsunami（Python 海啸）"),
    ("## The Python Sandbox（Python 沙盒）", "## 41.3 The Python Sandbox（Python 沙盒）"),
    ("## The Python Upside（Python 的优势）", "## 41.4 The Python Upside（Python 的优势）"),
    ("## Closing Thoughts（收束思考）", "## 41.5 Closing Thoughts（收束思考）"),
    ("## Where to Go from Here（接下来去哪里）", "## 41.6 Where to Go from Here（接下来去哪里）"),
    (
        "## Encore: Print Your Own Completion Certificate!（加餐：打印自己的完成证书）",
        "## 41.7 Encore: Print Your Own Completion Certificate!（加餐：打印自己的完成证书）",
    ),
]
for a, b in repls:
    text = text.replace(a, b)

patterns = [
    (r"(### 英文原文\n\n)> Chapter 41\. All Good Things ", r"\1> "),
    (r"(### 英文原文\n\n)> The Python Tsunami ", r"\1> "),
    (r"(### 英文原文\n\n)> The Python Sandbox ", r"\1> "),
    (r"(### 英文原文\n\n)> The Python Upside ", r"\1> "),
    (r"(### 英文原文\n\n)> Closing Thoughts ", r"\1> "),
    (r"(### 英文原文\n\n)> Where to Go from Here ", r"\1> "),
    (r"(### 英文原文\n\n)> Encore: Print Your Own Completion Certificate! ", r"\1> "),
]
for pat, rep in patterns:
    text = re.sub(pat, rep, text, count=1)

TABLE = """
**Table 41-1. A sampling of redundancy and tool explosion in Python**

| Category | Members |
|---|---|
| 3 major paradigms | Procedural, functional, object-oriented |
| 4 string-formatting tools | `%` expression, `str.format`, `string.Template`, f-strings |
| 4 attribute-accessor tools | properties, descriptors, `__getattr__`, `__getattribute__` |
| 2 finalization statements | `try`/`finally`, `with` plus context managers |
| 4 varieties of comprehension | List, set, dictionary, generator |
| 3 class-augmentation options | Manual rebinding, `@` decorators, metaclasses |
| 4 kinds of methods | Instance, static, class, metaclass |
| 2 attribute-storage systems | `__dict__`, `__slots__` |
| 4 flavors of imports | Module, package, package relative, namespace package |
| 2 superclass-reference tools | Explicit class names, `super` plus MRO |
| 6 assignment forms | Basic, sequence, multitarget, `+=` augmented, `*` unpacking, `:=` named |
| 3 types of functions | Basic, `yield` generator, `async` coroutine |
| 6 function-argument forms | Basic, `name=X`, `*X`, `**X`, keyword-only, positional-only |
| 2 class-behavior sources | Superclasses, metaclasses |
| 3 multiple-choice tools | `if`/`elif`, dictionary indexing, `match` |
| 4 state-retention options | Classes, closures, function attributes, mutables |
| 2 bytecode storage schemes | timestamp, hashkey |
| 3 name-string importers | `exec`, `__import__`, `importlib` |
| 2 kinds of decorators | Function, class |
| 4 dictionary-merge options | `for` loops, `update` method, `**D` unpacking, `|` union |
| 2 exception-handler models | `except` singles, `except*` groups |
| 4 statement-aping expressions | `if`/`else`, comprehensions, `lambda`, `:=` assignment |
| 8 starred collectors/unpackers | Assignment; function header/call; list/tuple/dict/set literal; `match` |

"""

if "| Category | Members |" not in text:
    text2, n = re.subn(
        r"> Table 41-1\.\s*\n>\s*\n> A sampling of redundancy[\s\S]*?match If you care about Python",
        TABLE + "> If you care about Python",
        text,
        count=1,
    )
    if n:
        text = text2
    else:
        text2, n = re.subn(
            r"> Table 41-1\.[\s\S]*?(?=\n### 中文翻译)",
            TABLE + "\n",
            text,
            count=1,
        )
        if n:
            text = text2
        else:
            # joined one-liner table mess
            text2, n = re.subn(
                r"> Table 41-1\..*?match If you care about Python",
                TABLE + "> If you care about Python",
                text,
                count=1,
                flags=re.S,
            )
            if n:
                text = text2

# Clean encore English: keep intro, drop mangled inline code
m = re.search(
    r"(## 41\.7 Encore[\s\S]*?### 英文原文\n\n)(>[\s\S]*?)(\n\n### 中文翻译)",
    text,
)
if m:
    intro = m.group(2)
    # cut at Example or code docstring
    parts = re.split(r"\n> Example 41-1\.|\n> \"\"\"|\n> import time", intro, maxsplit=1)
    cut = parts[0].rstrip()
    if "supported." in cut:
        idx = cut.index("supported.") + len("supported.")
        cut = cut[:idx]
    # ensure blockquote format
    if not cut.startswith(">"):
        cut = "> " + cut
    clean = cut.rstrip()
    clean += (
        "\n>\n"
        "> **Example 41-1. You-made-it.py** — complete source is in the **代码分析** section below "
        "(comments translated to Chinese). Run with `python3 You-made-it.py`. "
        "See also Figure 41-1 in the original book."
    )
    # append short run-note English after Chinese is hard; keep note here
    text = text[: m.start()] + m.group(1) + clean + m.group(3) + text[m.end() :]

# Insert --- between sections after 深度理解 blocks before next ## 41.
def add_hr(m):
    body = m.group(1).rstrip()
    return body + "\n\n---\n" + m.group(2)


text = re.sub(r"(\n### 深度理解\n[\s\S]*?)(\n## 41\.)", add_hr, text)

# Fix summary header to match ch01-ish
text = text.replace("# 本章总结", "# 本章总结")

text = re.sub(r"\n{3,}", "\n\n", text)
if not text.endswith("\n"):
    text += "\n"
p.write_text(text, encoding="utf-8")
print("wrote", p, "size", p.stat().st_size)

lines = text.splitlines()
print("title:", lines[0])
print("headers:")
for l in lines:
    if l.startswith("## ") or l.startswith("# "):
        print(" ", l[:100])

in_eng = False
long_q = short_q = 0
for line in lines:
    if line.startswith("### 英文原文"):
        in_eng = True
        continue
    if line.startswith("### "):
        in_eng = False
        continue
    if in_eng and line.startswith(">"):
        b = line[1:].strip()
        if len(b) > 100:
            long_q += 1
        elif b:
            short_q += 1
print("eng long", long_q, "short", short_q)
