# -*- coding: utf-8 -*-
"""Targeted Phase-3 repairs without aggressive section rewriting."""
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")


def to_bq(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^####?\s+[^\n]+（[^）]+）\s*", "", text)
    text = re.sub(r"^####?\s+[^\n]+\s*", "", text)
    if not text:
        return ""
    # already quoted?
    if text.startswith(">"):
        return text.rstrip() + "\n"
    # split Chinese paragraphs roughly
    parts = re.split(r"(?<=[。！？])\s*", text)
    parts = [p.strip() for p in parts if p.strip()]
    paras, buf = [], []
    for p in parts:
        buf.append(p)
        if len(buf) >= 2 or sum(len(x) for x in buf) > 160:
            paras.append("".join(buf))
            buf = []
    if buf:
        paras.append("".join(buf))
    lines = []
    for i, para in enumerate(paras):
        lines.append("> " + para)
        if i < len(paras) - 1:
            lines.append(">")
    return "\n".join(lines) + "\n"


def peel_glued_chinese_from_eng_sections(text: str) -> str:
    """
    For each ### 英文原文 block, if a line contains '中文翻译' marker or
    heavy CJK tail after English, peel it into a following ### 中文翻译
    (only if the section does not already have a proper 中文翻译, or merge).
    """
    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("### 英文原文"):
            out.append(line)
            i += 1
            eng = []
            while i < len(lines) and not lines[i].startswith("### "):
                eng.append(lines[i])
                i += 1
            # look ahead: is next header 中文翻译?
            has_zh_next = i < len(lines) and lines[i].startswith("### 中文翻译")

            eng_text = "".join(eng)
            peeled_zh = None

            # marker inside eng block
            m = re.search(r"————\s*中文翻译\s*————", eng_text)
            if not m:
                m = re.search(r"###\s*中文翻译", eng_text)
            if m:
                before = eng_text[: m.start()]
                after = eng_text[m.end() :]
                # clean after
                after = re.sub(r"^\s*####?\s*[^\n]+", "", after).strip()
                # rebuild eng lines from before
                eng = [before] if before.endswith("\n") or not before else [before + "\n"]
                # actually keep line structure of before
                eng = before.splitlines(keepends=True)
                while eng and eng[-1].strip() in ("", ">"):
                    eng.pop()
                if eng and not eng[-1].endswith("\n"):
                    eng[-1] += "\n"
                eng.append("\n")
                peeled_zh = after

            if peeled_zh is None:
                # line-level: English sentence then Chinese
                new_eng = []
                acc_zh = []
                for el in eng:
                    raw = el.rstrip("\n")
                    if "中文翻译" in raw:
                        mm = re.search(r"————\s*中文翻译\s*————|###\s*中文翻译", raw)
                        if mm:
                            before = raw[: mm.start()].rstrip()
                            after = raw[mm.end() :].strip()
                            after = re.sub(r"^####?\s*[^\n]+（[^）]+）\s*", "", after)
                            after = re.sub(r"^####?\s*[^\n]+\s*", "", after)
                            if before:
                                if not before.startswith(">"):
                                    before = "> " + before
                                new_eng.append(before + "\n")
                            if after:
                                acc_zh.append(after)
                            continue
                    # pure-ish Chinese line inside eng
                    body = raw[2:] if raw.startswith("> ") else (raw[1:] if raw.startswith(">") else raw)
                    cjk = len(re.findall(r"[\u4e00-\u9fff]", body))
                    lat = len(re.findall(r"[A-Za-z]", body))
                    if body.strip() and cjk > 15 and cjk > lat * 1.5:
                        acc_zh.append(body.strip())
                        continue
                    new_eng.append(el if el.endswith("\n") else el + "\n")
                if acc_zh:
                    while new_eng and new_eng[-1].strip() in ("", ">"):
                        new_eng.pop()
                    if new_eng and not new_eng[-1].endswith("\n"):
                        new_eng[-1] += "\n"
                    new_eng.append("\n")
                    eng = new_eng
                    peeled_zh = "\n".join(acc_zh)

            out.extend(eng)

            if peeled_zh:
                zh_block = to_bq(peeled_zh)
                if has_zh_next:
                    # skip existing 中文翻译 header+body, replace with peeled if better
                    # consume old zh block
                    i += 1  # skip ### 中文翻译
                    old_zh = []
                    while i < len(lines) and not lines[i].startswith("### "):
                        old_zh.append(lines[i])
                        i += 1
                    out.append("### 中文翻译\n")
                    out.append("\n")
                    # prefer longer content
                    if len("".join(old_zh)) > len(zh_block) + 80:
                        out.extend(old_zh)
                    else:
                        out.append(zh_block if zh_block.endswith("\n") else zh_block + "\n")
                        if not out[-1].endswith("\n"):
                            out.append("\n")
                else:
                    out.append("### 中文翻译\n")
                    out.append("\n")
                    out.append(zh_block if zh_block.endswith("\n") else zh_block + "\n")
            continue
        out.append(line)
        i += 1
    return "".join(out)


WRAPUP_ZH = """> 有了前面这些细节，你终于掌握了完整的 Python 继承故事——至少是本书能覆盖的全部内容。这是一个错综复杂的故事：今天它横跨实例、类、超类、元类、描述符、`super`、内置操作与 MRO，而这一切只是为了查找一个简单的属性名。
>
> 当然，某些实际需求会迫使我们依赖例外规则；但你应当认真思考：一门面向对象语言若以如此迷宫般的方式实现继承——它的基础运算——这意味着什么。至少，这应提醒你：尽量让自己的代码保持简单，避免依赖这些曲折规则的阴暗角落。
>
> 一如既往，你的用户与维护者会为此感激。若要更精确地理解，可查阅 Python 内部的继承实现——如今主要记录在 `object.c`（普通实例）与 `typeobject.c`（类）中，低层但完整。
>
> 深入内部实现本不该是使用 Python 的前提，但在一个复杂且持续变化的系统里，它往往是最终、有时也是唯一的真相来源。边界情形尤其如此：它们由长期积累的例外催生，抬高了学习者与使用者的门槛——下一章收官时我们还会简要回到这个缺点。
>
> 眼下，让我们进入元类“魔法”的最后一块：元类方法——它们依赖元类这条继承旁支。
"""

WRAPUP_DEEP = """- **核心概念**：完整的属性查找故事已不再是“沿 MRO 找字典”，而是实例、类、超类、元类树、描述符、`super`、内置操作分岔与 MRO 的合力。
- **底层实现**：普通实例查找主要走 `object.c` 路径；类对象查找走 `typeobject.c`，并可进入元类树。数据描述符、`super` 与部分内置操作会改写“朴素 MRO 扫描”的结果。
- **设计原因**：例外规则多半服务实际需求（性能、兼容、描述符语义），但叠加后使“查一个名字”变成高阶协议。
- **实际问题**：应用代码应避开阴暗角落——少用过度魔法的 `__getattribute__`/元类组合，优先可读的显式设计；框架作者才需要完整模型。
- **初学者误区**：以为“会写 class 就懂继承”。在元类与描述符介入后，同一条 `obj.attr` 可能走完全不同的路径；边界行为要以文档与源码为准，而不是直觉。
"""


def replace_section_zh(text: str, header_prefix: str, new_zh: str, new_deep: str | None = None) -> str:
    parts = re.split(r"(?m)^(?=## )", text)
    out = [parts[0]]
    for part in parts[1:]:
        if part.startswith(header_prefix):
            # replace ### 中文翻译 block
            def repl_zh(m):
                return m.group(1) + new_zh + "\n"

            if "### 中文翻译" in part:
                part = re.sub(
                    r"(### 中文翻译\n\n)([\s\S]*?)(?=\n### |\n---|\Z)",
                    repl_zh,
                    part,
                    count=1,
                )
            else:
                part = re.sub(
                    r"(### 英文原文\n\n[\s\S]*?)(?=\n### |\Z)",
                    lambda m: m.group(1).rstrip() + "\n\n### 中文翻译\n\n" + new_zh + "\n",
                    part,
                    count=1,
                )
            if new_deep is not None:
                if "### 深度理解" in part:
                    part = re.sub(
                        r"(### 深度理解\n\n)([\s\S]*?)(?=\n### |\n---|\Z)",
                        lambda m: m.group(1) + new_deep + "\n",
                        part,
                        count=1,
                    )
                else:
                    part = part.rstrip() + "\n\n### 深度理解\n\n" + new_deep + "\n"
            # also fix pseudo headers
            part = part.replace("————深度理解————", "### 深度理解")
            part = part.replace("————英文原文————", "### 英文原文")
            part = part.replace("————中文翻译————", "### 中文翻译")
        out.append(part if part.endswith("\n") else part + "\n")
    return "".join(out)


def normalize_pseudo_headers(text: str) -> str:
    text = text.replace("————英文原文————", "### 英文原文")
    text = text.replace("————中文翻译————", "### 中文翻译")
    text = text.replace("————深度理解————", "### 深度理解")
    text = re.sub(r"———+\s*英文原文\s*———+", "### 英文原文", text)
    text = re.sub(r"———+\s*中文翻译\s*———+", "### 中文翻译", text)
    text = re.sub(r"———+\s*深度理解\s*———+", "### 深度理解", text)
    return text


def fix_tech_advice_headers(text: str) -> str:
    text = re.sub(
        r"^## \d+\.\d+\s+技术扩展（Technical Expansion）\s*$",
        "## 技术拓展（Technical Expansion）",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^## \d+\.\d+\s+技术拓展（Technical Expansion）\s*$",
        "## 技术拓展（Technical Expansion）",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^## 技术扩展（Technical Expansion）\s*$",
        "## 技术拓展（Technical Expansion）",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^## \d+\.\d+\s+学习建议（Learning Advice）\s*$",
        "## 学习建议（Learning Advice）",
        text,
        flags=re.M,
    )
    return text


def dedupe_zh_headers(text: str) -> str:
    """If a section has two ### 中文翻译, merge/keep first non-empty properly."""
    parts = re.split(r"(?m)^(?=## )", text)
    out = [parts[0]]
    for part in parts[1:]:
        count = part.count("### 中文翻译")
        if count <= 1:
            out.append(part if part.endswith("\n") else part + "\n")
            continue
        # keep first 中文翻译 block only if second is duplicate/garbled
        blocks = re.split(r"(?m)(?=### )", part)
        seen_zh = False
        new_blocks = []
        for b in blocks:
            if b.startswith("### 中文翻译"):
                if seen_zh:
                    continue
                seen_zh = True
            new_blocks.append(b)
        part = "".join(new_blocks)
        out.append(part if part.endswith("\n") else part + "\n")
    return "".join(out)


def add_deep_to_section(text: str, header_substr: str, deep: str) -> str:
    parts = re.split(r"(?m)^(?=## )", text)
    out = [parts[0]]
    for part in parts[1:]:
        if header_substr in part.splitlines()[0] and "### 深度理解" not in part:
            if "### 代码分析" in part:
                part = part.replace(
                    "### 代码分析",
                    f"### 深度理解\n\n{deep}\n\n### 代码分析",
                    1,
                )
            else:
                part = part.rstrip() + f"\n\n### 深度理解\n\n{deep}\n"
        out.append(part if part.endswith("\n") else part + "\n")
    return "".join(out)


DEEP_37_8 = """- **核心概念**：文本字符串（`str`）保存解码后的 Unicode 码点序列，是人类可读文本的默认类型。
- **底层实现**：`str` 在内存中按灵活表示存储码点；与文件/网络交互时通过编码与 `bytes` 互转。
- **设计原因**：把“文本”与“原始字节”分开，避免隐式混用。
- **实际问题**：读写边界必须明确 encoding；文本用 `str`，二进制协议用 `bytes`。
- **初学者误区**：把 `str` 当成“带编码的字节”——编码发生在 I/O 边界，内存中的 `str` 已是文本。
"""

DEEP_37_12 = """- **核心概念**：源文件编码声明告诉解释器如何把 `.py` 字节解码为源文字符（默认 UTF-8）。
- **底层实现**：识别 coding cookie 或 BOM 后再解码源文件。
- **设计原因**：允许源码直接含非 ASCII，同时文件仍是普通文本。
- **实际问题**：声明必须与编辑器实际保存编码一致；团队应统一 UTF-8。
- **初学者误区**：混淆源文件编码与运行期 `open(..., encoding=)` / `str.encode`。
"""


def split_remaining_long_prose(text: str, limit: int = 480) -> str:
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
            body = line[1:].lstrip()
            if body.startswith((">>>", "...", "def ", "class ", "return ", "if ", "for ", "# ")):
                out.append(line)
                continue
            # require multiple sentences
            parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", body)
            if len(parts) <= 1:
                out.append(line)
                continue
            buf, blen = [], 0
            paras = []
            for s in parts:
                s = s.strip()
                if not s:
                    continue
                if buf and blen + len(s) > limit:
                    paras.append(" ".join(buf))
                    buf, blen = [s], len(s)
                else:
                    buf.append(s)
                    blen += len(s) + 1
            if buf:
                paras.append(" ".join(buf))
            for i, para in enumerate(paras):
                out.append("> " + para)
                if i < len(paras) - 1:
                    out.append(">")
        else:
            out.append(line)
    return "\n".join(out) + "\n"


def process_ch40():
    p = ROOT / "ch40.md"
    # start from post phase1/2 state: current file already partially fixed
    # re-read backup after numbering? Use current + targeted
    text = p.read_text(encoding="utf-8")
    # If we damaged too much, re-run from pre_fmt + renumber
    # Check pair health roughly
    text = normalize_pseudo_headers(text)
    text = peel_glued_chinese_from_eng_sections(text)
    text = replace_section_zh(text, "## 40.10", WRAPUP_ZH, WRAPUP_DEEP)
    text = dedupe_zh_headers(text)
    text = fix_tech_advice_headers(text)
    text = split_remaining_long_prose(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    p.write_text(text, encoding="utf-8")
    print("ch40", p.stat().st_size)


def process_ch37():
    p = ROOT / "ch37.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_pseudo_headers(text)
    text = peel_glued_chinese_from_eng_sections(text)
    text = text.replace(
        "## 37.20 8. Unicode-Text Files（Unicode 文本文件）",
        "## 37.20 Unicode-Text Files（Unicode 文本文件）",
    )
    text = add_deep_to_section(text, "Using Text Strings", DEEP_37_8)
    text = add_deep_to_section(text, "源文件的编码", DEEP_37_12)
    text = fix_tech_advice_headers(text)
    text = split_remaining_long_prose(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    p.write_text(text, encoding="utf-8")
    print("ch37", p.stat().st_size)


def process_ch38():
    p = ROOT / "ch38.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_pseudo_headers(text)
    text = fix_tech_advice_headers(text)
    text = split_remaining_long_prose(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    p.write_text(text, encoding="utf-8")
    print("ch38", p.stat().st_size)


def process_ch36():
    p = ROOT / "ch36.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_pseudo_headers(text)
    text = peel_glued_chinese_from_eng_sections(text)
    text = fix_tech_advice_headers(text)
    text = split_remaining_long_prose(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    p.write_text(text, encoding="utf-8")
    print("ch36", p.stat().st_size)


def process_ch39():
    p = ROOT / "ch39.md"
    text = p.read_text(encoding="utf-8")
    text = fix_tech_advice_headers(text)
    text = split_remaining_long_prose(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    p.write_text(text, encoding="utf-8")
    print("ch39", p.stat().st_size)


def process_ch41():
    p = ROOT / "ch41.md"
    text = p.read_text(encoding="utf-8")
    text = fix_tech_advice_headers(text)
    text = split_remaining_long_prose(text, limit=450)
    text = re.sub(r"\n{3,}", "\n\n", text)
    p.write_text(text, encoding="utf-8")
    print("ch41", p.stat().st_size)


if __name__ == "__main__":
    # ch40 may be messy from phase3_fix — rebuild from pre_fmt + renumber first
    bak = Path(r"C:\Users\QK\AppData\Local\Temp\opencode\ch40.md.pre_fmt_bak")
    if bak.exists():
        from fix_ch36_41 import process as p12

        (ROOT / "ch40.md").write_text(bak.read_text(encoding="utf-8"), encoding="utf-8")
        p12(40)
        print("ch40 restored+renumbered")
    process_ch40()
    process_ch37()
    process_ch38()
    process_ch36()
    process_ch39()
    process_ch41()
