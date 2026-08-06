# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path("chapters/ch40.md")
text = p.read_text(encoding="utf-8")

ZH_11 = """### 中文翻译

> 现在已经理解元类如何改变名字继承，可以准确讨论元类方法了。简而言之，元类中的方法会被元类的实例——也就是类对象——继承并处理；它们处理的不是这些类创建出来的普通非类实例。
>
> 因此元类方法在形式和功能上类似第 32 章介绍的类方法（class method），只是它面向类的绑定行为是自动发生的。根据上一节的继承规则，它们只对类可见，对普通实例不可见——这正是前面提到的那个限制性“转折”。
>
> 类装饰器没有与之直接对应的机制，不过装饰器可以返回任意对象，理论上仍能实现很多变体。示例中，元类 `M` 定义 `z(cls)` 与 `y(cls)`，类 `C` 自己定义 `y(self)`、`x(self)`。
>
> 从 `C` 取得 `C.x`、`C.y` 时，名字来自类字典，因此是普通函数；`C.z` 来自元类，因此自动绑定到类 `C`，调用 `C.z()` 时 `cls` 就是 `C`。创建普通实例 `I = C()` 后，`I.x()` 与 `I.y()` 会按普通实例方法绑定到 `I`，但 `I.z()` 失败，因为普通实例不会进入 `C` 的元类树。
>
> 元类方法真正新增的两点就是：只被类继承，以及从类取得时自动绑定到该类。后半部分绑定细节见下一节。

"""

parts = re.split(r"(?m)^(?=## )", text)
out = [parts[0]]
for part in parts[1:]:
    first = part.splitlines()[0] if part.splitlines() else ""
    if first.startswith("## 40.11") and "### 中文翻译" not in part:
        part2, n = re.subn(
            r"(### 英文原文\n\n[\s\S]*?)(\n### 深度理解)",
            r"\1\n" + ZH_11 + r"\2",
            part,
            count=1,
        )
        if n:
            part = part2
            print("inserted 40.11 zh")
        else:
            print("FAILED insert 40.11")
    if re.match(r"^## 40\.(15|16|17)", first):
        part = part.replace("————英文原文————", "### 英文原文")
        part = part.replace("————中文翻译————", "### 中文翻译")
        part = part.replace("————深度理解————", "### 深度理解")
        if "### 英文原文" not in part:
            lines = part.splitlines()
            insert_at = 1
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            lines.insert(insert_at, "### 英文原文")
            lines.insert(insert_at + 1, "")
            part = "\n".join(lines) + "\n"
            print("added eng header", first[:40])
    out.append(part if part.endswith("\n") else part + "\n")

text = "".join(out)
text = re.sub(
    r"^## \d+\.\d+\s+技术扩展.*$",
    "## 技术拓展（Technical Expansion）",
    text,
    flags=re.M,
)
text = re.sub(
    r"^## \d+\.\d+\s+技术拓展.*$",
    "## 技术拓展（Technical Expansion）",
    text,
    flags=re.M,
)
text = re.sub(
    r"^## 技术扩展.*$",
    "## 技术拓展（Technical Expansion）",
    text,
    flags=re.M,
)
text = re.sub(
    r"^## \d+\.\d+\s+学习建议.*$",
    "## 学习建议（Learning Advice）",
    text,
    flags=re.M,
)
text = re.sub(r"\n{3,}", "\n\n", text)
p.write_text(text, encoding="utf-8")
print("wrote", p.stat().st_size)

# pair check 40.10-17
parts = re.split(r"(?m)^(?=## )", text)
for part in parts[1:]:
    first = part.splitlines()[0]
    if first.startswith("## 40.1"):
        e = part.count("### 英文原文")
        z = part.count("### 中文翻译")
        d = part.count("### 深度理解")
        print(first[:55], f"e/z/d={e}/{z}/{d}")
