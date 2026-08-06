# -*- coding: utf-8 -*-
"""
Rebuild ch38.md / ch40.md from PDF-extracted txt.

Pipeline:
1) Line-aware reflow: join PDF-broken prose; isolate real code runs.
2) Split by PDF-outline headings.
3) Emit ch37/ch39-style markdown with Chinese + teaching notes.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
CHAP = ROOT / "chapters"

HEADINGS_38 = [
    "Why Manage Attributes?",
    "Inserting Code to Run on Attribute Access",
    "Properties",
    "The Basics",
    "A First Example",
    "Computed Attributes",
    "Coding Properties with Decorators",
    "Descriptors",
    "The Basics",
    "A First Example",
    "Computed Attributes",
    "Using State Information in Descriptors",
    "How Properties and Descriptors Relate",
    "__getattr__ and __getattribute__",
    "The Basics",
    "A First Example",
    "Computed Attributes",
    "__getattr__ and __getattribute__ Compared",
    "Management Techniques Compared",
    "Intercepting Built-in Operation Attributes",
    "Example: Attribute Validations",
    "Using Properties to Validate",
    "Using Descriptors to Validate",
    "Using __getattr__ to Validate",
    "Using __getattribute__ to Validate",
    "Chapter Summary",
    "Test Your Knowledge: Quiz",
    "Test Your Knowledge: Answers",
]

HEADINGS_40 = [
    "To Metaclass or Not to Metaclass",
    "The Downside of Helper Functions",  # matched loosely
    "Metaclasses Versus Class Decorators: Round 1",
    "The Metaclass Model",
    "Classes Are Instances of type",
    "Metaclasses Are Subclasses of type",
    "Class Statements Call a type",
    "Class Statements Can Choose a type",
    "Metaclass Method Protocol",
    "Coding Metaclasses",
    "A Basic Metaclass",
    "Customizing Construction and Initialization",
    "Other Metaclass Coding Techniques",
    "Managing Classes with Metaclasses and Decorators",
    "Inheritance: The Finale",
    "Metaclass Versus Superclass",
    "Metaclass Inheritance",
    "Python Inheritance Algorithm: The Simple Version",
    "Python Inheritance Algorithm: The Less Simple Version",
    "The Inheritance Wrap-Up",
    "Metaclass Methods",
    "Metaclass Methods Versus Class Methods",
    "Operator Overloading in Metaclass Methods",
    "Metaclass Methods Versus Instance Methods",
    "Chapter Summary",
    "Test Your Knowledge: Quiz",
    "Test Your Knowledge: Answers",
]


def ends_sentence(s: str) -> bool:
    s = s.rstrip()
    while s and s[-1] in "\"')]}”’":
        s = s[:-1]
    return bool(s) and s[-1] in ".!?"


def starts_cap(s: str) -> bool:
    s = s.lstrip()
    return bool(s) and (s[0].isupper() or s[0] in "\"'“‘*")


def join_frags(frags: list[str]) -> str:
    if not frags:
        return ""
    result = frags[0].strip()
    for p in frags[1:]:
        p = p.strip()
        if not p:
            continue
        if result.endswith("-") and p[:1].islower():
            result = result[:-1] + p
            continue
        if result[-1:] in "([{\"'“‘/" or p[:1] in ",.;:!?)]}'\"”’":
            result += p
            continue
        result += " " + p
    result = re.sub(r"[ \t]{2,}", " ", result)
    result = re.sub(r" +([,.;:!?])", r"\1", result)
    result = re.sub(r"\( ", "(", result)
    result = re.sub(r" \)", ")", result)
    result = re.sub(r"\b(\d)\s+\.\s+", r"\1. ", result)
    return result.strip()


def is_strong_code_start(line: str) -> bool:
    t = line.strip()
    if not t:
        return False
    if t.startswith(">>>") or t.startswith("..."):
        return True
    if t.startswith("$ "):
        return True
    if re.match(r"^(def|async def)\s+\w+\s*\(", t):
        return True
    if re.match(r"^class\s+[A-Za-z_][\w]*\s*[\(:]", t):
        return True
    if re.match(r"^import\s+\w+", t):
        return True
    if re.match(r"^from\s+[\w.]+\s+import\b", t):
        return True
    if re.match(r"^@\w+", t):
        return True
    if re.match(r"^Example\s+\d+-\d+", t):
        return True
    return False


def is_code_body_line(line: str) -> bool:
    """Continuation while inside a code run — still conservative."""
    if line.strip() == "":
        return True  # handled by peek logic
    s = line
    t = s.strip()
    if is_strong_code_start(s):
        return True
    if s.startswith(" ") or s.startswith("\t"):
        return True
    if t.startswith("#") and len(t) < 100:
        return True
    if t in {")", "]", "}", "),", "],", "},", "):", "(", "[", ":", "...", '"""', "'''", "pass", "..."}:
        return True
    if re.match(
        r"^(return|yield|raise|pass|break|continue|elif\b|else:|except\b|finally:|try:|with\b|for\b|while\b|if\b|print\(|self\.|cls\.|super\()",
        t,
    ):
        return True
    # assignment / call only if short and code-like
    if len(t) < 80 and re.match(r"^[A-Za-z_][\w.]*\s*=\s*\S", t) and not t.endswith((".", "?", "!")):
        if re.search(r"""['\"\[\](){}]|True|False|None|\d|property|lambda""", t):
            return True
    if len(t) < 80 and re.match(r"^[A-Za-z_][\w.]*\([^)]*\)\s*$", t):
        return True
    if t.startswith(("Traceback", "AttributeError", "TypeError", "ValueError", "SyntaxError")):
        return True
    if re.match(r"^[A-Za-z_][\w.]*: .*(Error|Exception)", t):
        return True
    # long capitalized sentence => prose
    if len(t) > 55 and t[0].isupper() and ends_sentence(t):
        if not re.search(r"\b(def|class|return|self\.)\b", t):
            return False
    if len(t) > 70 and re.search(
        r"\b(the|and|that|which|with|from|this|these|those|should|would|can|will|are|is)\b",
        t,
        re.I,
    ):
        if t.count("=") == 0 and "(" not in t:
            return False
    return False


def looks_like_prose_start(line: str) -> bool:
    t = line.strip()
    if not t:
        return False
    if is_strong_code_start(line):
        return False
    # sentence-like
    if t[0].isupper() and len(t) > 40:
        return True
    if t[0].isupper() and ends_sentence(t):
        return True
    starters = (
        "The ", "This ", "That ", "These ", "Those ", "When ", "While ", "Where ",
        "What ", "Why ", "How ", "If ", "In ", "On ", "At ", "As ", "For ", "To ",
        "By ", "With ", "Without ", "Because ", "Although ", "However ", "Moreover ",
        "Still ", "Next ", "Now ", "Here ", "There ", "After ", "Before ", "Once ",
        "Unlike ", "Like ", "Unlike ", "Note ", "Remember ", "Suppose ", "Of course",
        "Just ", "Although ", "And ", "But ", "Or ", "So ", "Yet ", "Finally ",
        "Up first", "Besides ", "Especially ", "Whatever ", "Despite ", "Probably ",
        "We ", "You ", "It ", "Its ", "Their ", "Our ", "A ", "An ", "Some ", "Any ",
        "None of", "All ", "Both ", "Each ", "Every ", "Such ", "Rather ", "Instead ",
    )
    return t.startswith(starters)


def reflow_lines(lines: list[str]) -> list[tuple[str, str]]:
    """Return list of ('prose'|'code', text). Blanks ignored inside prose."""
    blocks: list[tuple[str, str]] = []
    prose: list[str] = []
    i = 0
    n = len(lines)

    def flush_prose():
        nonlocal prose
        if prose:
            text = join_frags(prose)
            if text:
                blocks.append(("prose", text))
            prose = []

    while i < n:
        raw = lines[i].rstrip("\n")
        # strip form noise
        if re.match(r"^Chapter\s+\d+\.?$", raw.strip()):
            i += 1
            continue
        if raw.strip() in ("NOTE", "TIP", "WARNING"):
            flush_prose()
            blocks.append(("prose", raw.strip() + ":"))
            i += 1
            continue

        if is_strong_code_start(raw):
            flush_prose()
            code: list[str] = [raw]
            i += 1
            while i < n:
                nxt = lines[i].rstrip("\n")
                if not nxt.strip():
                    # peek
                    j = i + 1
                    while j < n and not lines[j].strip():
                        j += 1
                    if j >= n:
                        break
                    peek = lines[j].rstrip("\n")
                    if is_code_body_line(peek) and not looks_like_prose_start(peek):
                        code.append(nxt)
                        i += 1
                        continue
                    break
                if is_code_body_line(nxt) and not (
                    looks_like_prose_start(nxt) and not (nxt.startswith(" ") or nxt.startswith("\t"))
                    and not is_strong_code_start(nxt)
                    and len(nxt.strip()) > 55
                ):
                    # if clearly prose, stop
                    if looks_like_prose_start(nxt) and not nxt.startswith((" ", "\t")) and not is_strong_code_start(nxt):
                        if not re.match(r"^[A-Za-z_][\w.]*\s*=", nxt.strip()):
                            break
                    code.append(nxt)
                    i += 1
                    continue
                break
            # trim blanks
            while code and not code[-1].strip():
                code.pop()
            while code and not code[0].strip():
                code.pop(0)
            if code:
                blocks.append(("code", "\n".join(code)))
            continue

        # skip pure blanks in prose mode
        if not raw.strip():
            i += 1
            continue

        # paragraph break on sentence boundary
        if prose and ends_sentence(prose[-1]) and starts_cap(raw.strip()):
            flush_prose()
        prose.append(raw.strip())
        i += 1

    flush_prose()
    return blocks


def heading_regex(h: str) -> str:
    # loose: ignore quote chars, flexible whitespace
    h2 = h.replace("Helper Functions", "Helper” Functions")  # may not help
    # Build from words
    if "Helper" in h:
        return r"The\s+Downside\s+of\s+[“\"']?Helper[”\"']?\s+Functions"
    parts = re.split(r"\s+", h.strip())
    return r"\s+".join(re.escape(p) for p in parts)


def find_heading_spans(text: str, headings: list[str]) -> list[tuple[str, int, int]]:
    positions = []
    search_from = 0
    for h in headings:
        rx = heading_regex(h)
        m = re.search(rx, text[search_from:], flags=re.MULTILINE)
        if not m:
            print(f"  WARN missing: {h}")
            continue
        start = search_from + m.start()
        end = search_from + m.end()
        # canonical display name from matched text collapsed
        name = re.sub(r"\s+", " ", m.group(0)).strip()
        positions.append((name, start, end))
        search_from = end
    return positions


def split_sections(text: str, headings: list[str]) -> list[tuple[str, list[tuple[str, str]]]]:
    pos = find_heading_spans(text, headings)
    out: list[tuple[str, list[tuple[str, str]]]] = []

    def body_blocks(chunk: str) -> list[tuple[str, str]]:
        lines = chunk.splitlines()
        return reflow_lines(lines)

    if not pos:
        return [("_intro_", body_blocks(text))]

    intro = text[: pos[0][1]]
    intro = re.sub(r"^Chapter\s+\d+\.\s*", "", intro.strip(), count=1)
    intro = re.sub(r"^Managed Attributes\s*", "", intro, count=1)
    intro = re.sub(r"^Metaclasses and\s*Inheritance\s*", "", intro, count=1)
    ib = body_blocks(intro)
    if ib:
        out.append(("_intro_", ib))

    for i, (name, _s, e) in enumerate(pos):
        end = pos[i + 1][1] if i + 1 < len(pos) else len(text)
        # map display name back to logical key roughly
        key = name
        if "Downside" in name and "Helper" in name:
            key = 'The Downside of “Helper” Functions'
        out.append((key, body_blocks(text[e:end])))
    return out


def split_long(text: str, limit: int = 340) -> list[str]:
    if len(text) <= limit:
        return [text]
    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[]|__)", text)
    if len(parts) <= 1:
        return [text]
    out, buf, blen = [], [], 0
    for s in parts:
        s = s.strip()
        if not s:
            continue
        if buf and (blen + len(s) > limit or len(buf) >= 3):
            out.append(" ".join(buf))
            buf, blen = [s], len(s)
        else:
            buf.append(s)
            blen += len(s) + 1
    if buf:
        out.append(" ".join(buf))
    return out or [text]


def format_english(blocks: list[tuple[str, str]]) -> str:
    lines: list[str] = []
    for kind, text in blocks:
        if kind == "code":
            lines.append(">")
            lines.append("> ```python")
            for cl in text.splitlines():
                lines.append(f"> {cl}")
            lines.append("> ```")
            lines.append(">")
        else:
            # scrub any accidental fence leakage
            text = text.replace("```python", "").replace("```", "")
            for chunk in split_long(text.strip(), 340):
                if chunk.strip():
                    lines.append(f"> {chunk.strip()}")
                    lines.append(">")
    while lines and lines[-1] == ">":
        lines.pop()
    return "\n".join(lines)


# ---- Chinese maps (major sections) ----

ZH_38 = {
    "_intro_": (
        "本章扩展了前文已介绍的**属性拦截（attribute interception）**技术，再引入另一种，"
        "并把它们用在若干更大的示例中。与本书这一部分的其他内容一样，本章属于进阶主题、可选阅读——"
        "多数应用程序员不必深入：他们可以读写对象属性，而不关心属性如何实现。\n\n"
        "但对**工具构建者**而言，管理属性访问往往是灵活 API 的关键。理解本章的**描述符（descriptor）模型**，"
        "也能让 slots、property 等工具更可感；若你维护的代码用到了它们，本章甚至可能是必读。"
    ),
    "Why Manage Attributes?": (
        "对象属性是多数 Python 程序的核心——实体信息常常存放在属性里。"
        "通常属性只是对象的名字：例如 `person.name` 可能只是字符串，用基础语法读写即可。\n\n"
        "多数情况下，属性位于对象自身或由其类继承而来；这一模型对大多数程序已足够。\n\n"
        "但有时需要更多灵活性。若程序一开始直接使用 `name`，后来却要求访问时校验或变换，"
        "虽然可以写成 `getName`/`setName` 方法，却必须改遍所有调用点，并让客户端区分“名字 vs 方法”。\n\n"
        "若一开始就用方法接口，客户端可免疫变化；否则事后切换代价很高。"
        "电子表单元格从“离散值”变成“任意计算”就是典型例子——"
        "接口应允许未来演化而不破坏旧代码，因此“以后再改成方法”并不理想。"
    ),
    "Inserting Code to Run on Attribute Access": (
        "更好的做法是：在需要时，于属性访问时**自动运行代码**。"
        "这正是托管属性的主要角色——事后插入访问器逻辑，并支持超越简单存数据的用法。\n\n"
        "本章深入四类技术：\n\n"
        "1. 内建 `property`：管理**特定**属性的访问\n"
        "2. `__get__` / `__set__` 描述符：特定属性访问，也是 property、slots 等的基础\n"
        "3. `__getattr__` / `__setattr__`：未定义属性的读取，以及**所有**赋值\n"
        "4. `__getattribute__`：**所有**属性读取\n\n"
        "第 30、32 章曾简要提及。四者目标有重叠，但适用范围与复杂度不同："
        "property/描述符偏特定名；`__getattr__`/`__getattribute__` 更适合委托代理任意属性。\n\n"
        "文末案例可作自学示例；下一章装饰器也会用到这里的技术。"
    ),
    "Properties": (
        "property 协议把**某个具体属性**的 get/set/delete 路由到你提供的函数或方法，"
        "从而在访问时自动插入代码，并可拦截删除、提供文档字符串。\n\n"
        "property 用内建 `property` 创建并赋给**类属性**，可被继承；拦截函数收到 `self`。"
        "一个 property 只管理一个名字，不能泛化拦截所有属性，但能把简单数据升级为计算而不破坏调用方。\n\n"
        "property 本质是描述符的一种受限形式。"
    ),
    "Descriptors": (
        "描述符是更底层、更通用的托管属性机制；property 与 slots 等建立在描述符协议之上。\n\n"
        "实现 `__get__` / `__set__` / `__delete__` 的对象，在作为**类属性**被访问时，会接管该名的读写删。"
        "你是在独立类中显式编码协议，而不是调用 `property()`。"
    ),
    "__getattr__ and __getattribute__": (
        "`__getattr__` 与 `__getattribute__`（常配合 `__setattr__`）面向更广的属性访问，适合委托/代理。\n\n"
        "`__getattr__` 仅在正常查找失败后调用；`__getattribute__` 在每次读取时调用，必须小心避免递归。"
        "与 property/描述符的关键差别是**泛化 vs 具名**，以及 3.X 下许多内建运算不走实例 `__getattr__`。"
    ),
    "Example: Attribute Validations": (
        "下面用同一属性校验问题分别用四种技术实现，便于对比代码结构、状态存放与陷阱。"
        "目标相同：赋值时验证、读取时返回合法值——钩子机制各异。"
    ),
    "Chapter Summary": (
        "本章梳理了 `property`、描述符、`__getattr__`/`__setattr__`、`__getattribute__`。"
        "它们都能在访问时插入代码，但触发条件与复杂度不同。工具作者按需选型；应用作者读懂它们有助于理解框架中的属性魔法。"
    ),
    "Test Your Knowledge: Quiz": "请自测四种技术的拦截范围、描述符优先级、递归风险与内建运算限制。",
    "Test Your Knowledge: Answers": (
        "答案见原书。核心：property/描述符管特定名；`__getattr__` 仅未找到；"
        "`__getattribute__` 全拦截；数据描述符优先于实例字典；代理需注意内建运算路径。"
    ),
}

ZH_40 = {
    "_intro_": (
        "第 39 章研究了装饰器。作为全书最后一章技术章节，本章深入**元类（metaclasses）**——"
        "管理**类对象**而非实例的协议（第 32 章曾预告）。\n\n"
        "元类扩展装饰器的代码插入模型：在 `class` 语句结束时介入**类的创建**。"
        "还可通过单独继承树为类提供行为（普通实例通常看不到），从而使完整**继承**定义得以讲清。\n\n"
        "这是按需学习的进阶主题；粗通元类有助于理解 Python 类机制与使用元类的框架代码。"
    ),
    "To Metaclass or Not to Metaclass": (
        "元类可用于追踪、持久化、日志、按配置生成类成员、批量装饰方法、接口校验，乃至 ORM 等模式。"
        "类装饰器常能达到相近效果，但元类提供面向“造类”的正式模型。"
        "对本书读者，更大的收益是揭开类机制并理解完整继承故事。"
    ),
    'The Downside of “Helper” Functions': (
        "把类传给辅助函数也能增强类，但客户端必须记得调用。"
        "元类/装饰器提供更统一显式的结构，降低遗忘成本，并把定制逻辑集中到一处。"
        "方法若编码时已知可用继承；若取决于运行时配置，辅助函数仍偏“手工”，元类与类装饰器可进一步自动化。"
    ),
    "Metaclasses Versus Class Decorators: Round 1": (
        "类装饰器自动化“造类后再绑定”的步骤；元类把钩子放进创建协议。"
        "创建后修改类时二者常可互换；若必须在 `type` 构造阶段改命名空间，或需要元类方法/继承传播，选元类。"
    ),
    "The Metaclass Model": (
        "两件前提：**类也是对象**；**类由 type（或其子类）创建**。"
        "下文分别说明类是 `type` 的实例、元类是 `type` 的子类、`class` 如何调用 type，以及如何选择元类。"
    ),
    "Classes Are Instances of type": (
        "实例由类创建，类本身是 `type` 的实例。`type(Cls)` 通常是 `type`（除非自定义元类）。"
        "三参数 `type(name, bases, dict)` 可动态造类——即 `class` 语句背后的协议。"
    ),
    "Metaclasses Are Subclasses of type": (
        "自定义造类方式的途径是 subclass `type` 并重写 `__new__`/`__init__`/`__call__` 等。"
        "这样的类就是元类：它的实例是类，实例的实例才是普通对象。"
    ),
    "Class Statements Call a type": (
        "`class` 执行：建命名空间 → 执行类体 → 调用 `Type(name, bases, namespace)` → 绑定类名。"
        "元类只是替换这里的 `Type`。"
    ),
    "Class Statements Can Choose a type": (
        "通过 `metaclass=`（及基类带来的元类）选择构造所用的 type。"
        "元类声明可沿继承传播，多基类时也可能发生元类冲突。"
    ),
    "Metaclass Method Protocol": (
        "元类不仅在创建时运行，还可定义供**类对象**使用的方法；这些方法走与普通实例不同的继承路径。"
    ),
    "Coding Metaclasses": "从最小元类、定制构造/初始化，到其他写法，并与类装饰器对照。",
    "A Basic Metaclass": (
        "最小元类继承 `type`，在 `__new__`/`__init__` 接收 `name, bases, namespace`，处理后交给 `type`。"
        "客户端用 `metaclass=` 即可在定义时自动执行。"
    ),
    "Inheritance: The Finale": (
        "引入元类后必须区分：实例查找走类与超类 MRO；类对象还可从元类获得属性。两条路径合起来才是 3.X 完整故事。"
    ),
    "Metaclass Versus Superclass": (
        "超类服务**实例**；元类服务**类的创建与类级行为**。不要把实例行为塞进元类，也不要期望实例自动看见元类方法。"
    ),
    "Metaclass Inheritance": (
        "元类声明会传播；实例不会简单继承到元类方法，但经类对象访问时查找可进入元类。"
    ),
    "Python Inheritance Algorithm: The Simple Version": (
        "简单版：实例 `__dict__` → 类型 MRO 上的类/超类；描述符按规则介入。多数应用代码够用。"
    ),
    "Python Inheritance Algorithm: The Less Simple Version": (
        "完整版纳入数据/非数据描述符、`__getattr__`/`__getattribute__`，以及类对象相对元类的查找。"
    ),
    "The Inheritance Wrap-Up": "名字解析是多路径算法，不是简单的“往上找父类”。",
    "Metaclass Methods": "元类方法主要是类级 API；对比 `classmethod`、实例方法与运算符重载位置。",
    "Chapter Summary": (
        "元类介入类创建，与类装饰器交织，并补全含元类路径的继承图景。"
        "它是强力工具而非日常默认；更大收益是读懂 Python 对象模型。"
    ),
    "Test Your Knowledge: Quiz": "自测：类与 type、元类 vs 装饰器、实例能否见元类方法、继承两版差异。",
    "Test Your Knowledge: Answers": "答案见原书。应能画出实例→类→超类 与 类→元类 两条链。",
}


def translate_fallback(para: str) -> str:
    """Keyword guide + shortened English for sections without hand translation."""
    e = para.lower()
    tips = []
    mapping = [
        ("property", "property 机制"),
        ("descriptor", "描述符"),
        ("__getattr__", "`__getattr__`"),
        ("__getattribute__", "`__getattribute__`"),
        ("__setattr__", "`__setattr__`"),
        ("metaclass", "元类"),
        ("inherit", "继承"),
        ("decorator", "装饰器"),
        ("validat", "校验"),
        ("type(", "`type`"),
        ("class ", "`class` 语句"),
    ]
    for k, v in mapping:
        if k in e:
            tips.append(v)
    tip = "、".join(list(dict.fromkeys(tips))[:3]) if tips else "本节技术要点"
    short = re.sub(r"\s+", " ", para).strip()
    if len(short) > 180:
        short = short[:177] + "…"
    return f"【中文导读·{tip}】{short}"


def zh_section(title: str, blocks: list[tuple[str, str]], zmap: dict[str, str]) -> str:
    # fuzzy key
    key = title
    if title not in zmap:
        for k in zmap:
            if k in title or title in k:
                key = k
                break
    if key in zmap:
        text = zmap[key]
        parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        lines = []
        for i, p in enumerate(parts):
            for lp in p.split("\n"):
                lines.append(f"> {lp}")
            if i < len(parts) - 1:
                lines.append(">")
        while lines and lines[-1] == ">":
            lines.pop()
        return "\n".join(lines)

    lines = []
    prose = [t for k, t in blocks if k == "prose"]
    code_n = sum(1 for k, _ in blocks if k == "code")
    if not prose:
        return f"> 本节以代码为主（{code_n} 段）。请看英文原文代码块与「深度理解」。"
    for p in prose:
        zh = translate_fallback(p)
        for chunk in split_long(zh, 340):
            lines.append(f"> {chunk}")
            lines.append(">")
    if code_n:
        lines.append(f"> （另有 {code_n} 段代码示例，见英文原文。）")
    while lines and lines[-1] == ">":
        lines.pop()
    return "\n".join(lines)


def deep_note(chap: int, title: str) -> str:
    t = title.lower()
    if chap == 38:
        if title == "_intro_" or "why manage" in t:
            items = [
                "**核心概念**：托管属性 = 访问 `obj.attr` 时自动跑逻辑，客户端不必改成 getter/setter 调用。",
                "**四钩子**：property/描述符管具名；`__getattr__` 管未找到；`__getattribute__` 管一切读取；`__setattr__` 管赋值。",
                "**动机**：接口保持字段外观，内部可升级为校验/计算/日志。",
                "**场景**：ORM 字段、配置对象、懒加载、代理、只读视图。",
                "**误区**：以为属性只是 `__dict__` 键；忽略描述符优先级。",
            ]
        elif "property" in t:
            items = [
                "**核心概念**：`property` 把某一属性的读写删路由到函数，是描述符便利封装。",
                "**要点**：定义在类上；可用 `@property` / `@x.setter` / `@x.deleter`。",
                "**陷阱**：getter 里读同名属性会递归；通常用 `_name` 存真实值。",
            ]
        elif "descriptor" in t:
            items = [
                "**核心概念**：`__get__`/`__set__`/`__delete__`；数据描述符优先于实例字典。",
                "**地位**：函数作方法、property、slots 的共同基础。",
                "**状态**：描述符自身 vs 每实例 `__dict__`——校验器常用后者。",
            ]
        elif "getattr" in t or "getattribute" in t:
            items = [
                "**核心概念**：`__getattr__` 失败才调；`__getattribute__` 每次都调。",
                "**递归**：后者必须用 `object.__getattribute__` 取真实属性。",
                "**内建运算**：3.X 许多 `__X__` 在类上查找，不经实例 `__getattr__`。",
            ]
        elif "validat" in t:
            items = [
                "**核心概念**：同一校验，四种实现并排对比。",
                "**实践**：约束放写路径；测试非法赋值与继承。",
                "**选型**：复用多属性 → 描述符；快速单字段 → property。",
            ]
        else:
            items = [
                "**核心概念**：关注拦截点与状态存放位置。",
                "**建议**：对照英文示例跟打，观察 get/set 路径。",
                "**索引**：`Managed Attributes` / `descriptors` / `properties`。",
            ]
    else:
        if title == "_intro_" or "to metaclass" in t:
            items = [
                "**核心概念**：元类是类的类；参与 `class` 创建而非只包装成品。",
                "**调用**：`metaclass(name, bases, namespace)`，默认 `type`。",
                "**误区**：以为元类方法自动出现在普通实例上。",
            ]
        elif "helper" in t or "decorator" in t or "managing classes" in t:
            items = [
                "**核心概念**：辅助函数 / 类装饰器 / 元类都能改类，自动化与时机不同。",
                "**建议**：优先装饰器或 `__init_subclass__`；必要时再上元类。",
            ]
        elif "type" in t or "metaclass model" in t or "class statements" in t or "method protocol" in t:
            items = [
                "**核心概念**：类是 `type` 的实例；元类通常是 `type` 的子类。",
                "**分清**：`type(obj)` 查询 vs `type(name, bases, dict)` 构造。",
            ]
        elif "coding" in t or "basic metaclass" in t or "customizing" in t or "other metaclass" in t:
            items = [
                "**核心概念**：`class Meta(type)` + `__new__`/`__init__`。",
                "**要点**：记得调用 `type.__new__`/`super`；改命名空间要趁早。",
            ]
        elif "inheritance" in t or "superclass" in t:
            items = [
                "**核心概念**：实例→类→超类 MRO，外加类→元类路径。",
                "**分界**：实例一般不爬元类方法；类对象可以。",
            ]
        else:
            items = [
                "**核心概念**：造类时机 + 查找路径。",
                "**索引**：`Metaclasses` / `Metaclass Inheritance` / `type`。",
            ]
    return "\n".join(f"- {x}" for x in items)


def header_for(chap: int, n: int, title: str, last_major: str | None) -> tuple[str, str | None]:
    zh = {
        "_intro_": "开篇引言",
        "Why Manage Attributes?": "为什么要管理属性？",
        "Inserting Code to Run on Attribute Access": "在属性访问时插入代码",
        "Properties": "property",
        "The Basics": "基础",
        "A First Example": "第一个示例",
        "Computed Attributes": "计算属性",
        "Coding Properties with Decorators": "用装饰器编写 property",
        "Descriptors": "描述符",
        "Using State Information in Descriptors": "在描述符中使用状态",
        "How Properties and Descriptors Relate": "property 与描述符的关系",
        "__getattr__ and __getattribute__": "`__getattr__` 与 `__getattribute__`",
        "__getattr__ and __getattribute__ Compared": "二者对比",
        "Management Techniques Compared": "管理技术对比",
        "Intercepting Built-in Operation Attributes": "拦截内建运算属性",
        "Example: Attribute Validations": "示例：属性校验",
        "Using Properties to Validate": "用 property 校验",
        "Using Descriptors to Validate": "用描述符校验",
        "Using __getattr__ to Validate": "用 `__getattr__` 校验",
        "Using __getattribute__ to Validate": "用 `__getattribute__` 校验",
        "Chapter Summary": "本章小结",
        "Test Your Knowledge: Quiz": "测验",
        "Test Your Knowledge: Answers": "答案",
        "To Metaclass or Not to Metaclass": "用不用元类？",
        'The Downside of “Helper” Functions': "“辅助函数”的缺点",
        "Metaclasses Versus Class Decorators: Round 1": "元类 vs 类装饰器（1）",
        "The Metaclass Model": "元类模型",
        "Classes Are Instances of type": "类是 type 的实例",
        "Metaclasses Are Subclasses of type": "元类是 type 的子类",
        "Class Statements Call a type": "class 语句调用 type",
        "Class Statements Can Choose a type": "class 语句可选择 type",
        "Metaclass Method Protocol": "元类方法协议",
        "Coding Metaclasses": "编写元类",
        "A Basic Metaclass": "基本元类",
        "Customizing Construction and Initialization": "定制构造与初始化",
        "Other Metaclass Coding Techniques": "其他编写技巧",
        "Managing Classes with Metaclasses and Decorators": "用元类与装饰器管理类",
        "Inheritance: The Finale": "继承：终章",
        "Metaclass Versus Superclass": "元类 vs 超类",
        "Metaclass Inheritance": "元类继承",
        "Python Inheritance Algorithm: The Simple Version": "继承算法：简单版",
        "Python Inheritance Algorithm: The Less Simple Version": "继承算法：完整版",
        "The Inheritance Wrap-Up": "继承小结",
        "Metaclass Methods": "元类方法",
        "Metaclass Methods Versus Class Methods": "元类方法 vs 类方法",
        "Operator Overloading in Metaclass Methods": "元类中的运算符重载",
        "Metaclass Methods Versus Instance Methods": "元类方法 vs 实例方法",
    }
    majors = {
        "Why Manage Attributes?",
        "Inserting Code to Run on Attribute Access",
        "Properties",
        "Descriptors",
        "__getattr__ and __getattribute__",
        "Example: Attribute Validations",
        "Chapter Summary",
        "Test Your Knowledge: Quiz",
        "Test Your Knowledge: Answers",
        "To Metaclass or Not to Metaclass",
        "The Metaclass Model",
        "Coding Metaclasses",
        "Inheritance: The Finale",
        "Metaclass Methods",
    }
    new_major = title if title in majors else last_major
    if title == "_intro_":
        return f"## {chap}.{n} 开篇引言", new_major

    disp = title
    z = zh.get(title)
    if title in ("The Basics", "A First Example", "Computed Attributes") and last_major:
        disp = f"{title}（属 {last_major}）"
        z = f"{zh.get(title, title)}（{zh.get(last_major, last_major)}）"
    if z:
        return f"## {chap}.{n} {disp}（{z}）", new_major
    return f"## {chap}.{n} {disp}", new_major


def build_md(chap, en_title, zh_title, position, sections, zmap) -> str:
    parts = [
        f"# 第 {chap} 章：{en_title}（{zh_title}）",
        "",
        "> **原书**：《Learning Python》（6th Edition），作者 Mark Lutz",
        f"> **本章地位**：{position}",
        "",
        "---",
        "",
    ]
    last_major = None
    n = 0
    for title, blocks in sections:
        n += 1
        head, last_major = header_for(chap, n, title, last_major)
        parts.append(head)
        parts.append("")
        parts.append("### 英文原文")
        parts.append("")
        eng = format_english(blocks)
        parts.append(eng if eng.strip() else "> （本节无正文。）")
        parts.append("")
        parts.append("### 中文翻译")
        parts.append("")
        parts.append(zh_section(title, blocks, zmap))
        parts.append("")
        parts.append("### 深度理解")
        parts.append("")
        parts.append(deep_note(chap, title))
        parts.append("")
        codes = [t for k, t in blocks if k == "code" and len(t.strip()) > 5]
        if codes:
            parts.append("### 代码分析")
            parts.append("")
            parts.append("代表性代码（完整上下文见英文原文）：")
            parts.append("")
            for c in codes[:4]:
                if re.match(r"^Example\s+\d+", c.strip()) and c.count("\n") < 1:
                    continue
                parts.append("```python")
                parts.append(c.rstrip())
                parts.append("```")
                parts.append("")
            if len(codes) > 4:
                parts.append(f"> 其余 {len(codes)-4} 段见英文原文代码块。")
                parts.append("")
        parts.append("---")
        parts.append("")

    parts.append(f"## {chap}.{n+1} 学习建议（整理）")
    parts.append("")
    if chap == 38:
        parts.append(
            "- 顺序：Why Manage → Properties → Descriptors → getattr 系 → 校验对比。\n"
            "- 动手：同一字段四种技术做校验。\n"
            "- 索引：`index.md` 中 **Managed Attributes** 等词条与各 `##` 对应。"
        )
    else:
        parts.append(
            "- 顺序：To Metaclass → Model → Coding → Inheritance Finale → Metaclass Methods。\n"
            "- 动手：元类 vs 类装饰器实现子类注册。\n"
            "- 索引：`index.md` 中 **Metaclasses** 等词条与各 `##` 对应。"
        )
    parts.append("")
    text = "\n".join(parts)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text if text.endswith("\n") else text + "\n"


def eng_stats(md: str):
    long_q = short_q = 0
    in_eng = in_code = False
    for line in md.splitlines():
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
            in_code = body.startswith("```python") or (body == "```" and not in_code and False)
            if body.startswith("```") and not body.startswith("```python") and body != "```":
                pass
            if body == "```python":
                in_code = True
            elif body == "```":
                in_code = False
            continue
        if in_code or not body:
            continue
        if len(body) > 100:
            long_q += 1
        elif len(body) < 45:
            short_q += 1
    return long_q, short_q


def process(chap: int):
    raw = (CHAP / f"ch{chap:02d}.txt").read_text(encoding="utf-8")
    # light clean tabs already done
    headings = HEADINGS_38 if chap == 38 else HEADINGS_40
    print(f"ch{chap} raw={len(raw)}")
    sections = split_sections(raw, headings)
    print(f"  sections={len(sections)}")
    for t, b in sections[:8]:
        print(f"   {t!r}: p={sum(1 for k,_ in b if k=='prose')} c={sum(1 for k,_ in b if k=='code')}")
    print("   ...")

    if chap == 38:
        md = build_md(
            38, "Managed Attributes", "托管属性",
            "进阶核心章：property、描述符、`__getattr__`/`__setattr__`、`__getattribute__` 四套属性管理技术及校验对比。"
            "是 slots、绑定方法、ORM 字段与第 39–40 章的地基。",
            sections, ZH_38,
        )
    else:
        md = build_md(
            40, "Metaclasses and Inheritance", "元类与继承",
            "技术收官章：元类（创建类的类）、与类装饰器关系，以及 Python 完整继承算法（实例路径 + 元类路径）。",
            sections, ZH_40,
        )
    path = CHAP / f"ch{chap:02d}.md"
    path.write_text(md, encoding="utf-8")
    lq, sq = eng_stats(md)
    print(f"  wrote {path.name} len={len(md)} eng_long={lq} eng_short={sq}")


def main():
    process(38)
    process(40)
    # quick quality sample
    for chap in (38, 40):
        lines = (CHAP / f"ch{chap:02d}.md").read_text(encoding="utf-8").splitlines()
        print(f"---- ch{chap} sample ----")
        for i, line in enumerate(lines[:55]):
            print(f"{i+1:3d}|{line[:110]}")
    print("DONE")


if __name__ == "__main__":
    main()
