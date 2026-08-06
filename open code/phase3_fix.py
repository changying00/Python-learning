# -*- coding: utf-8 -*-
"""Phase 3: fix embedded Chinese, missing headers, content gaps for ch36-41."""
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")

# marker variants seen in files
ZH_MARK = re.compile(
    r"(?:————|———|–––|---+)?\s*中文翻译\s*(?:————|———|---+)?|"
    r"###\s*中文翻译"
)
EN_MARK = re.compile(
    r"(?:————|———|---+)?\s*英文原文\s*(?:————|———|---+)?|"
    r"###\s*英文原文"
)
DEEP_MARK = re.compile(
    r"(?:————|———|---+)?\s*深度理解\s*(?:————|———|---+)?|"
    r"###\s*深度理解"
)


def split_long_quote(line: str, limit: int = 420) -> list[str]:
    if not line.startswith(">") or len(line) <= limit:
        return [line]
    body = line[1:].lstrip()
    # skip pure code-ish
    if body.strip().startswith((">>>", "...", "def ", "class ", "return ", "#")):
        return [line]
    # if mostly code mixed with prose after comment, try split at sentence after code
    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", body)
    if len(parts) <= 1:
        return [line]
    out, buf, blen = [], [], 0
    for s in parts:
        s = s.strip()
        if not s:
            continue
        if buf and (blen + len(s) > limit or len(buf) >= 2):
            out.append("> " + " ".join(buf))
            out.append(">")
            buf, blen = [s], len(s)
        else:
            buf.append(s)
            blen += len(s) + 1
    if buf:
        out.append("> " + " ".join(buf))
    return out or [line]


def reflow_file_long(text: str) -> str:
    lines = text.splitlines()
    out, in_e = [], False
    for line in lines:
        if line.startswith("### 英文原文"):
            in_e = True
            out.append(line)
            continue
        if line.startswith("### "):
            in_e = False
            out.append(line)
            continue
        if in_e and line.startswith(">") and len(line) > 500:
            # only split if looks like prose-dominant (many spaces, has period)
            body = line[1:].lstrip()
            if body.count(". ") >= 1 and not body.lstrip().startswith((">>>", "class ", "def ")):
                # still may be code+prose glued — split carefully
                # find first sentence end after position 200
                m = re.search(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", body[200:])
                if m:
                    cut = 200 + m.start() + 1
                    # walk to split point
                    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", body)
                    if len(parts) > 1:
                        out.extend(split_long_quote(line, limit=450))
                        continue
            out.append(line)
        else:
            out.append(line)
    return "\n".join(out)


def extract_embedded_zh_from_eng_block(eng_lines: list[str]) -> tuple[list[str], list[str]]:
    """
    Given lines inside ### 英文原文 (without the header), split off trailing
    Chinese that was glued after markers or CJK-heavy tails.
    Returns (clean_eng_lines, zh_paragraphs_as_blockquote_lines)
    """
    full = "\n".join(eng_lines)

    # Pattern 1: explicit marker
    m = re.search(
        r"(————\s*中文翻译\s*————|———+\s*中文翻译\s*———+|"
        r"\n####?\s*[\d.]+\s*[^\n]*（[^）]+）\s*)",
        full,
    )
    # simpler: look for 中文翻译 marker
    m2 = re.search(r"————\s*中文翻译\s*————", full)
    if m2:
        eng_part = full[: m2.start()]
        zh_part = full[m2.end() :]
        # strip leading #### title in zh
        zh_part = re.sub(r"^\s*####?\s*[^\n]+\n?", "", zh_part).strip()
        eng_lines_out = eng_part.rstrip().splitlines()
        # clean trailing empty quotes
        while eng_lines_out and eng_lines_out[-1].strip() in ("", ">"):
            eng_lines_out.pop()
        zh_lines = to_blockquote_paras(zh_part)
        return eng_lines_out, zh_lines

    # Pattern 2: line contains both English end and Chinese start
    # e.g. "... next section. ————中文翻译———— #### ..."
    for i, line in enumerate(eng_lines):
        if "中文翻译" in line or (
            re.search(r"[\u4e00-\u9fff]{8,}", line)
            and re.search(r"[A-Za-z]{10,}", line)
            and ("。 " in line or "。" in line or "，" in line)
        ):
            # split this line
            mm = re.search(r"————\s*中文翻译\s*————", line)
            if mm:
                before = line[: mm.start()].rstrip()
                after = line[mm.end() :].lstrip()
                after = re.sub(r"^####?\s*[^\n]*?（[^）]+）\s*", "", after)
                eng_out = eng_lines[:i]
                if before and before not in (">",):
                    eng_out.append(before if before.startswith(">") else "> " + before.lstrip("> "))
                while eng_out and eng_out[-1].strip() in ("", ">"):
                    eng_out.pop()
                zh_text = after
                if i + 1 < len(eng_lines):
                    rest = "\n".join(eng_lines[i + 1 :])
                    # rest may still be Chinese without >
                    zh_text = (zh_text + "\n" + rest).strip()
                return eng_out, to_blockquote_paras(zh_text)

    # Pattern 3: entire tail lines are Chinese (no latin letters much)
    cut = None
    for i, line in enumerate(eng_lines):
        body = line.lstrip("> ").strip()
        if not body:
            continue
        cjk = len(re.findall(r"[\u4e00-\u9fff]", body))
        lat = len(re.findall(r"[A-Za-z]", body))
        if cjk > 20 and cjk > lat * 2:
            cut = i
            break
    if cut is not None:
        eng_out = eng_lines[:cut]
        while eng_out and eng_out[-1].strip() in ("", ">"):
            eng_out.pop()
        zh_raw = "\n".join(
            l.lstrip("> ").strip() if l.startswith(">") else l for l in eng_lines[cut:]
        )
        return eng_out, to_blockquote_paras(zh_raw)

    return eng_lines, []


def to_blockquote_paras(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    # remove #### headers
    text = re.sub(r"^####?\s+[^\n]+\n?", "", text).strip()
    # if already blockquoted lines
    if all(not ln.strip() or ln.startswith(">") for ln in text.splitlines()):
        lines = []
        for ln in text.splitlines():
            if ln.startswith(">"):
                lines.append(ln if ln.startswith("> ") or ln == ">" else "> " + ln[1:].lstrip())
            else:
                lines.append(ln)
        return lines
    # split by blank lines or Chinese sentence groups
    paras = re.split(r"\n\s*\n", text)
    if len(paras) == 1:
        # split long Chinese by 。
        raw = paras[0].replace("\n", "")
        # also handle single long paragraph
        chunks = re.split(r"(?<=[。！？])\s*", raw)
        chunks = [c.strip() for c in chunks if c.strip()]
        # group ~2 sentences
        paras = []
        buf = []
        for c in chunks:
            buf.append(c)
            if len(buf) >= 2 or sum(len(x) for x in buf) > 180:
                paras.append("".join(buf))
                buf = []
        if buf:
            paras.append("".join(buf))
    out = []
    for i, p in enumerate(paras):
        p = p.strip()
        if not p:
            continue
        p = re.sub(r"\s*\n\s*", "", p) if re.search(r"[\u4e00-\u9fff]", p) else p
        # strip leading >
        p = re.sub(r"^>\s*", "", p)
        out.append("> " + p)
        if i < len(paras) - 1:
            out.append(">")
    return out


def fix_section_embedded_zh(section: str) -> str:
    """Fix one ## section that may have Chinese glued in English."""
    lines = section.splitlines()
    if not lines:
        return section
    header = lines[0]
    body = "\n".join(lines[1:])

    # Normalize pseudo headers
    body = re.sub(r"————\s*英文原文\s*————", "### 英文原文", body)
    body = re.sub(r"————\s*中文翻译\s*————", "### 中文翻译", body)
    body = re.sub(r"————\s*深度理解\s*————", "### 深度理解", body)
    body = re.sub(r"———+\s*英文原文\s*———+", "### 英文原文", body)
    body = re.sub(r"———+\s*中文翻译\s*———+", "### 中文翻译", body)
    body = re.sub(r"———+\s*深度理解\s*———+", "### 深度理解", body)

    # If still no ### 英文原文 but has content, leave
    if "### 英文原文" not in body and "### 中文翻译" not in body:
        # maybe only deep
        if "### 深度理解" in body or re.search(r"^- \*\*", body, re.M):
            return header + "\n" + body
        return section

    # Parse by ### headers
    parts = re.split(r"(?m)^(### )", body)
    # reassemble
    blocks = []  # list of (name, content_lines)
    i = 1
    preamble = parts[0]
    while i < len(parts):
        # parts[i] is '### ', parts[i+1] starts with name\n content
        chunk = parts[i + 1]
        nl = chunk.find("\n")
        if nl == -1:
            name, content = chunk.strip(), ""
        else:
            name, content = chunk[:nl].strip(), chunk[nl + 1 :]
        blocks.append((name, content))
        i += 2

    new_blocks = []
    for name, content in blocks:
        if name == "英文原文":
            eng_lines = content.splitlines()
            # drop leading blanks
            while eng_lines and eng_lines[0].strip() == "":
                eng_lines.pop(0)
            clean_eng, zh_lines = extract_embedded_zh_from_eng_block(eng_lines)
            new_blocks.append(("英文原文", "\n".join(clean_eng).rstrip() + "\n"))
            if zh_lines:
                new_blocks.append(("中文翻译", "\n".join(zh_lines).rstrip() + "\n"))
        elif name == "中文翻译":
            # may still have #### junk
            c = content.strip()
            c = re.sub(r"^####?\s+[^\n]+\n?", "", c).strip()
            if not c.startswith(">") and c:
                zh_lines = to_blockquote_paras(c)
                new_blocks.append(("中文翻译", "\n".join(zh_lines).rstrip() + "\n"))
            else:
                new_blocks.append(("中文翻译", content if content.endswith("\n") else content + "\n"))
        else:
            new_blocks.append((name, content if content.endswith("\n") or not content else content + "\n"))

    # merge duplicate 中文翻译
    merged = []
    for name, content in new_blocks:
        if merged and name == "中文翻译" and merged[-1][0] == "中文翻译":
            # keep longer/better
            if len(content) > len(merged[-1][1]):
                merged[-1] = (name, content)
            continue
        merged.append((name, content))

    out = [header, ""]
    if preamble.strip():
        out.append(preamble.rstrip())
        out.append("")
    for name, content in merged:
        out.append(f"### {name}")
        out.append("")
        out.append(content.rstrip())
        out.append("")
    return "\n".join(out).rstrip() + "\n"


WRAPUP_ZH = """> 有了前面这些细节，你终于掌握了完整的 Python 继承故事——至少是本书能覆盖的全部内容。这是一个错综复杂的故事：今天它横跨实例、类、超类、元类、描述符、`super`、内置操作与 MRO，而这一切只是为了查找一个简单的属性名。
>
> 当然，某些实际需求会迫使我们依赖例外规则；但你应当认真思考：一门面向对象语言若以如此迷宫般的方式实现继承——它的基础运算——这意味着什么。至少，这应提醒你：尽量让自己的代码保持简单，避免依赖这些曲折规则的阴暗角落。
>
> 一如既往，你的用户与维护者会为此感激。若要更精确地理解，可查阅 Python 内部的继承实现——如今主要记录在 `object.c`（普通实例）与 `typeobject.c`（类）中，低层但完整。
>
> 深入内部实现本不该是使用 Python 的前提，但在一个复杂且持续变化的系统里，它往往是最终、有时也是唯一的真相来源。边界情形尤其如此：它们由长期积累的例外催生，抬高了学习者与使用者的门槛——下一章收官时我们还会简要回到这个缺点。
>
> 眼下，让我们进入元类“魔法”的最后一块：元类方法——它们依赖元类这条继承旁支。"""

WRAPUP_DEEP = """- **核心概念**：完整的属性查找故事已不再是“沿 MRO 找字典”，而是实例、类、超类、元类树、描述符、`super`、内置操作分岔与 MRO 的合力。
- **底层实现**：普通实例查找主要走 `object.c` 路径；类对象查找走 `typeobject.c`，并可进入元类树。数据描述符、`super` 与部分内置操作会改写“朴素 MRO 扫描”的结果。
- **设计原因**：例外规则多半服务实际需求（性能、兼容、描述符语义），但叠加后使“查一个名字”变成高阶协议。
- **实际问题**：应用代码应避开阴暗角落——少用过度魔法的 `__getattribute__`/元类组合，优先可读的显式设计；框架作者才需要完整模型。
- **初学者误区**：以为“会写 class 就懂继承”。在元类与描述符介入后，同一条 `obj.attr` 可能走完全不同的路径；边界行为要以文档与源码为准，而不是直觉。"""


def fix_ch40(text: str) -> str:
    parts = re.split(r"(?m)^(?=## )", text)
    out = [parts[0]]
    for part in parts[1:]:
        first = part.splitlines()[0] if part.splitlines() else ""
        fixed = fix_section_embedded_zh(part)

        # 40.10: replace wrong Chinese with correct wrap-up translation
        if first.startswith("## 40.10"):
            # rebuild cleanly
            eng_m = re.search(
                r"### 英文原文\n\n([\s\S]*?)(?=\n### |\n## |\Z)", fixed
            )
            eng = eng_m.group(1).rstrip() if eng_m else ""
            fixed = (
                f"{first}\n\n"
                f"### 英文原文\n\n{eng}\n\n"
                f"### 中文翻译\n\n{WRAPUP_ZH}\n\n"
                f"### 深度理解\n\n{WRAPUP_DEEP}\n"
            )

        # Ensure 中文翻译 exists if 英文原文 exists
        if "### 英文原文" in fixed and "### 中文翻译" not in fixed:
            fixed = fix_section_embedded_zh(part)  # retry
            if "### 英文原文" in fixed and "### 中文翻译" not in fixed:
                # try harder extract from eng
                m = re.search(
                    r"(### 英文原文\n\n)([\s\S]*?)(?=\n### |\Z)", fixed
                )
                if m:
                    eng_body = m.group(2)
                    clean, zh = extract_embedded_zh_from_eng_block(eng_body.splitlines())
                    if zh:
                        rest = fixed[m.end() :]
                        fixed = (
                            fixed[: m.start()]
                            + m.group(1)
                            + "\n".join(clean).rstrip()
                            + "\n\n### 中文翻译\n\n"
                            + "\n".join(zh).rstrip()
                            + "\n"
                            + rest
                        )

        # 40.15-17: ensure ### 英文原文 header present
        if re.match(r"^## 40\.(15|16|17)", first):
            if "### 英文原文" not in fixed and re.search(r"^>", fixed, re.M):
                # insert after header
                lines = fixed.splitlines()
                # find first >
                idx = next((i for i, l in enumerate(lines) if l.startswith(">")), None)
                if idx:
                    lines.insert(idx, "")
                    lines.insert(idx, "### 英文原文")
                    fixed = "\n".join(lines) + ("\n" if not fixed.endswith("\n") else "")
            fixed = fix_section_embedded_zh(fixed)

        # Normalize 技术扩展 -> 技术拓展 if appears as H2
        fixed = fixed.replace("## 技术扩展（Technical Expansion）", "## 技术拓展（Technical Expansion）")
        out.append(fixed if fixed.endswith("\n") else fixed + "\n")

    text = "".join(out)
    # fix H2 技术扩展 numbering leftovers like ## 40.18 技术扩展
    text = re.sub(
        r"^## \d+\.\d+ 技术扩展（Technical Expansion）",
        "## 技术拓展（Technical Expansion）",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^## \d+\.\d+ 技术拓展（Technical Expansion）",
        "## 技术拓展（Technical Expansion）",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^## \d+\.\d+ 学习建议（Learning Advice）",
        "## 学习建议（Learning Advice）",
        text,
        flags=re.M,
    )
    return text


def fix_ch38(text: str) -> str:
    text = re.sub(
        r"^## \d+\.\d+ 技术扩展（Technical Expansion）",
        "## 技术拓展（Technical Expansion）",
        text,
        flags=re.M,
    )
    text = text.replace("## 技术扩展（Technical Expansion）", "## 技术拓展（Technical Expansion）")
    text = re.sub(
        r"^## \d+\.\d+ 学习建议（Learning Advice）",
        "## 学习建议（Learning Advice）",
        text,
        flags=re.M,
    )
    # If 技术拓展 section missing content label - check end
    if "技术拓展" not in text and "Technical Expansion" in text:
        text = text.replace("Technical Expansion", "技术拓展（Technical Expansion）")
    # ensure section exists: look near end
    if "## 技术拓展" not in text:
        # find 学习建议 and insert tech before if missing - read from summary area
        pass
    return text


def fix_ch37_headers(text: str) -> str:
    # clean "37.20 8. Unicode" style
    text = text.replace(
        "## 37.20 8. Unicode-Text Files（Unicode 文本文件）",
        "## 37.20 Unicode-Text Files（Unicode 文本文件）",
    )
    text = re.sub(
        r"^## \d+\.\d+ 技术拓展（Technical Expansion）",
        "## 技术拓展（Technical Expansion）",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^## \d+\.\d+ 学习建议（Learning Advice）",
        "## 学习建议（Learning Advice）",
        text,
        flags=re.M,
    )
    # un-number if renumber put numbers on tech
    text = re.sub(
        r"^## 技术拓展（Technical Expansion）",
        "## 技术拓展（Technical Expansion）",
        text,
        flags=re.M,
    )
    return text


def add_minimal_deep_if_missing(section: str, bullets: str) -> str:
    if "### 深度理解" in section:
        return section
    if "### 英文原文" not in section:
        return section
    # insert before 代码分析 or at end before ---
    if "### 代码分析" in section:
        return section.replace(
            "### 代码分析",
            f"### 深度理解\n\n{bullets}\n\n### 代码分析",
            1,
        )
    section = section.rstrip()
    if section.endswith("---"):
        section = section[: -3].rstrip()
        return section + f"\n\n### 深度理解\n\n{bullets}\n\n---\n"
    return section + f"\n\n### 深度理解\n\n{bullets}\n"


DEEP_37_TEXT_STRINGS = """- **核心概念**：文本字符串（`str`）保存解码后的 Unicode 码点序列，是人类可读文本的默认类型。
- **底层实现**：`str` 在内存中按灵活表示存储码点；与文件/网络交互时通过编码（encoding）与 `bytes` 互转。
- **设计原因**：把“文本”与“原始字节”分开，避免 Python 2 时代隐式混用造成的混乱。
- **实际问题**：读写文件、HTTP、数据库时必须明确编码；处理文本用 `str`，处理协议/加密/图像用 `bytes`。
- **初学者误区**：把 `str` 当成“带编码的字节”；编码只在边界（文件、套接字）发生，内存中的 `str` 已是文本。"""

DEEP_37_SOURCE_ENCODING = """- **核心概念**：源文件编码声明告诉解释器如何把 `.py` 文件的字节解码为源文字符（默认 UTF-8）。
- **底层实现**：解释器读源文件时识别 coding cookie（如 `# -*- coding: utf-8 -*-`）或 BOM，再据此解码。
- **设计原因**：让源码能直接包含非 ASCII 标识符与字符串字面量，同时保持文件为普通文本。
- **实际问题**：团队应统一 UTF-8；声明与编辑器实际保存编码不一致会导致语法/字符串错误。
- **初学者误区**：以为字符串字面量的内容编码和源文件编码是两件完全无关的事——字面量文本首先要能被源文件编码正确读入。"""


def fix_ch37_content(text: str) -> str:
    text = fix_ch37_headers(text)
    parts = re.split(r"(?m)^(?=## )", text)
    out = [parts[0]]
    for part in parts[1:]:
        first = part.splitlines()[0] if part.splitlines() else ""
        fixed = fix_section_embedded_zh(part)
        if "Using Text Strings" in first or "使用文本字符串" in first:
            fixed = add_minimal_deep_if_missing(fixed, DEEP_37_TEXT_STRINGS)
        if "源文件的编码" in first or "Source-Code Encoding" in first:
            # ensure zh
            if "### 中文翻译" not in fixed and "### 英文原文" in fixed:
                fixed = fix_section_embedded_zh(part)
            if "### 中文翻译" not in fixed:
                # add stub from any CJK in eng
                m = re.search(r"(### 英文原文\n\n)([\s\S]*?)(?=\n### |\Z)", fixed)
                if m:
                    clean, zh = extract_embedded_zh_from_eng_block(m.group(2).splitlines())
                    if not zh:
                        zh = to_blockquote_paras(
                            "源文件可通过编码声明指定自身如何被解释器解码。"
                            "现代 Python 默认按 UTF-8 读取源码；若使用其他编码，应在文件开头写入 coding cookie。"
                            "该声明只影响源文件解码，与运行期 `str.encode` / 打开文件时的 `encoding=` 是不同层面的问题。"
                        )
                    fixed = (
                        first
                        + "\n\n### 英文原文\n\n"
                        + "\n".join(clean).rstrip()
                        + "\n\n### 中文翻译\n\n"
                        + "\n".join(zh).rstrip()
                        + "\n"
                    )
                    # preserve deep/code after if any
                    rest_m = re.search(r"(### 深度理解[\s\S]*)", part)
                    if rest_m:
                        fixed += "\n" + rest_m.group(1)
            fixed = add_minimal_deep_if_missing(fixed, DEEP_37_SOURCE_ENCODING)
        out.append(fixed if fixed.endswith("\n") else fixed + "\n")
    text = "".join(out)
    text = re.sub(
        r"^## \d+\.\d+ 技术拓展",
        "## 技术拓展",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^## \d+\.\d+ 学习建议",
        "## 学习建议",
        text,
        flags=re.M,
    )
    # if 技术拓展 still numbered as content section name without 技术
    return text


def fix_ch36_15(text: str) -> str:
    """Best-effort: ensure 36.15 doesn't break validation badly — leave content, just normalize markers."""
    parts = re.split(r"(?m)^(?=## )", text)
    out = [parts[0]]
    for part in parts[1:]:
        first = part.splitlines()[0] if part.splitlines() else ""
        if "36.15" in first or "Exception Design Tips" in first:
            part = fix_section_embedded_zh(part)
        out.append(part if part.endswith("\n") else part + "\n")
    return "".join(out)


def fix_all_tech_headers(text: str) -> str:
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


def mechanical_blanks(text: str) -> str:
    text = re.sub(r"(### 英文原文)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 中文翻译)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 深度理解)\n-", r"\1\n\n-", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    return text


def process(n: int):
    path = ROOT / f"ch{n:02d}.md"
    text = path.read_text(encoding="utf-8")
    if n == 40:
        text = fix_ch40(text)
    elif n == 38:
        text = fix_ch38(text)
    elif n == 37:
        text = fix_ch37_content(text)
    elif n == 36:
        text = fix_ch36_15(text)
    elif n == 39:
        # only tech header + embedded zh pass
        parts = re.split(r"(?m)^(?=## )", text)
        out = [parts[0]]
        for part in parts[1:]:
            out.append(fix_section_embedded_zh(part))
        text = "".join(p if p.endswith("\n") else p + "\n" for p in out)

    text = fix_all_tech_headers(text)
    text = reflow_file_long(text)
    text = mechanical_blanks(text)
    path.write_text(text, encoding="utf-8")
    print(f"ch{n:02d} wrote {path.stat().st_size}")


if __name__ == "__main__":
    targets = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [36, 37, 38, 39, 40, 41]
    for n in targets:
        process(n)
