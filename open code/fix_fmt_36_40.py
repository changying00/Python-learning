# -*- coding: utf-8 -*-
"""Fix structural format of ch36-40 to closer match ch01.md style."""
from pathlib import Path
import re

ROOT = Path("chapters")


def stats(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
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
    title = lines[0] if lines else ""
    has_hr = "\n---\n" in path.read_text(encoding="utf-8")
    numbered = len(re.findall(r"^## \d+\.", path.read_text(encoding="utf-8"), re.M))
    return {
        "title": title,
        "long": long_q,
        "short": short_q,
        "hr": has_hr,
        "numbered": numbered,
        "space_title": bool(re.match(r"^# 第 \d+ 章", title)),
    }


def fix_common(path: Path, chap_num: int):
    text = path.read_text(encoding="utf-8")
    orig = text

    # title spacing
    text = re.sub(rf"^# 第\s*{chap_num}\s*章", f"# 第 {chap_num} 章", text, count=1, flags=re.M)

    # meta blank before ---
    text = re.sub(
        r"(> \*\*本章地位\*\*[^\n]*)\n+---",
        r"\1\n\n---",
        text,
        count=1,
    )

    # blank after ### headings before content
    text = re.sub(r"(### 英文原文)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 中文翻译)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 深度理解)\n-", r"\1\n\n-", text)
    text = re.sub(r"(### 代码分析)\n```", r"\1\n\n```", text)

    # collapse excess blanks
    text = re.sub(r"\n{3,}", "\n\n", text)

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def fix_ch38_40_section_titles():
    """Add Chinese-first numbering-ish titles where pure English headers remain."""
    # ch38
    p = ROOT / "ch38.md"
    text = p.read_text(encoding="utf-8")
    mapping = {
        "## Chapter Introduction（章节介绍）": "## 38.1 开篇引言（Chapter Introduction）",
        "## Properties（属性）": "## 38.2 Properties（属性）",
        "## Descriptors（描述符）": "## 38.3 Descriptors（描述符）",
        "## Generic Attribute Management（通用属性管理）": "## 38.4 Generic Attribute Management（通用属性管理）",
        "## Intercepting Built-in Operation Attributes（拦截内置操作属性）": "## 38.5 Intercepting Built-in Operation Attributes（拦截内置操作属性）",
        "## Chapter Summary（章节小结）": "## 38.6 Chapter Summary（章节小结）",
        "## Test Your Knowledge: Quiz（知识测验：测验）": "## 38.7 Test Your Knowledge: Quiz（知识测验：测验）",
        "## Test Your Knowledge: Answers（知识测验：答案）": "## 38.8 Test Your Knowledge: Answers（知识测验：答案）",
    }
    for a, b in mapping.items():
        text = text.replace(a, b)
    # strip glued chapter title in first english para
    text = re.sub(
        r"(### 英文原文\n\n)> Chapter 38\. Managed Attributes ",
        r"\1> ",
        text,
        count=1,
    )
    p.write_text(text, encoding="utf-8")

    # ch40
    p = ROOT / "ch40.md"
    text = p.read_text(encoding="utf-8")
    mapping = {
        "## Chapter Introduction（章节导言）": "## 40.1 开篇引言（Chapter Introduction）",
        "## Inheritance: The Finale（继承：终章篇）": "## 40.2 Inheritance: The Finale（继承：终章篇）",
        "## Metaclass Versus Superclass（元类与超类）": "## 40.3 Metaclass Versus Superclass（元类与超类）",
        "## Metaclass Inheritance（元类继承）": "## 40.4 Metaclass Inheritance（元类继承）",
        "## Python Inheritance Algorithm: The Simple Version（Python 继承算法：简单版本）": "## 40.5 Python Inheritance Algorithm: The Simple Version（Python 继承算法：简单版本）",
        "## The Descriptors Deviation（描述符带来的偏误）": "## 40.6 The Descriptors Deviation（描述符带来的偏误）",
        "## The Assignment Addendum（赋值补篇）": "## 40.7 The Assignment Addendum（赋值补篇）",
        "## The super supplement（`super` 补篇）": "## 40.8 The super supplement（`super` 补篇）",
        "## The Built-ins Bifurcation（内置操作的分岔）": "## 40.9 The Built-ins Bifurcation（内置操作的分岔）",
        "## The Inheritance Wrap-Up（继承总结）": "## 40.10 The Inheritance Wrap-Up（继承总结）",
        "## Metaclass Methods（元类方法）": "## 40.11 Metaclass Methods（元类方法）",
        "## Metaclass Methods Versus Class Methods（元类方法与类方法）": "## 40.12 Metaclass Methods Versus Class Methods（元类方法与类方法）",
    }
    for a, b in mapping.items():
        text = text.replace(a, b)
    text = re.sub(
        r"(### 英文原文\n\n)> Metaclasses and Inheritance ",
        r"\1> ",
        text,
        count=1,
    )
    # also common glued subsection titles at start of english blocks
    for title in [
        "To Metaclass or Not to Metaclass ",
        "The Downside of “Helper” Functions ",
        "The Downside of \"Helper\" Functions ",
    ]:
        text = text.replace(f"> {title}", f"> **{title.strip()}** ")
    p.write_text(text, encoding="utf-8")


def main():
    for n in range(36, 41):
        path = ROOT / f"ch{n:02d}.md"
        changed = fix_common(path, n)
        print(f"ch{n:02d} common-fix={'yes' if changed else 'no'}", stats(path))

    fix_ch38_40_section_titles()
    print("after section renumber:")
    for n in (38, 40):
        print(f" ch{n}", stats(ROOT / f"ch{n:02d}.md"))


if __name__ == "__main__":
    main()
