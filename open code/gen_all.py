import os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = "chapters"

CHAPTERS = {
    37: {
        "en": "Unicode and Byte Strings",
        "zh": "Unicode\u4e0e\u5b57\u8282\u5b57\u7b26\u4e32",
        "pos": "\u7b2c37\u7ae0\u662f\u5b57\u7b26\u4e32\u5904\u7406\u7684\u9ad8\u7ea7\u7bc7\uff0c\u5728\u7b2c7\u7ae0\u57fa\u7840\u4e0a\u5c06\u5b57\u7b26\u4e32\u6a21\u578b\u6269\u5c55\u5230\u5b8c\u6574\u7684Unicode\u6587\u672c\u548c\u4e8c\u8fdb\u5236\u6570\u636e\u5904\u7406\u3002\u672c\u7ae0\u662fPython 3.x\u7684\u5fc5\u4fee\u5185\u5bb9\uff0c\u56e0\u4e3a\u6b63\u5e38\u5b57\u7b26\u4e32\u672c\u8eab\u5c31\u662fUnicode\u3002",
    },
    38: {
        "en": "Attributes and Methods",
        "zh": "\u5c5e\u6027\u4e0e\u65b9\u6cd5",
        "pos": "\u7b2c38\u7ae0\u6df1\u5165\u8bb2\u89e3Python\u7684\u5c5e\u6027\u7ba1\u7406\u673a\u5236\uff0c\u5305\u62ec__getattr__\u3001__getattribute__\u3001\u63cf\u8ff0\u7b26\u548c\u5c5e\u6027\u88c5\u9970\u5668\u3002\u8fd9\u662f\u7406\u89e3Python\u5bf9\u8c61\u6a21\u578b\u7684\u6838\u5fc3\u7ae0\u8282\u3002",
    },
    39: {
        "en": "Decorators",
        "zh": "\u88c5\u9970\u5668",
        "pos": "\u7b2c39\u7ae0\u8bb2\u89e3\u88c5\u9970\u5668\u2014\u2014\u5728\u51fd\u6570\u548c\u7c7b\u521b\u5efa\u65f6\u81ea\u52a8\u8fd0\u884c\u7684\u4ee3\u7801\u3002\u88c5\u9970\u5668\u662fPython\u6700\u5f3a\u5927\u7684\u5143\u7f16\u7a0b\u5de5\u5177\u4e4b\u4e00\uff0c\u5e7f\u6cdb\u5e94\u7528\u4e8e\u6846\u67b6\u548c\u5e93\u7684\u5f00\u53d1\u4e2d\u3002",
    },
    40: {
        "en": "Metaclasses",
        "zh": "\u5143\u7c7b",
        "pos": "\u7b2c40\u7ae0\u8bb2\u89e3\u5143\u7c7b\u2014\u2014\u521b\u5efa\u7c7b\u7684\u7c7b\u3002\u5143\u7c7b\u662fPython\u6700\u9ad8\u7ea7\u7684\u6982\u5ff5\u4e4b\u4e00\uff0c\u5b83\u4e0e\u7ee7\u627f\u3001\u63cf\u8ff0\u7b26\u548c\u88c5\u9970\u5668\u6df1\u5ea6\u7f29\u7f29\uff0c\u662f\u7406\u89e3Python\u5bf9\u8c61\u6a21\u578b\u7684\u5173\u952e\u3002",
    },
    41: {
        "en": "All Good Things",
        "zh": "\u7f8e\u597d\u7684\u7ec8\u7ed3",
        "pos": "\u7b2c41\u7ae0\u662f\u672c\u4e66\u7684\u6700\u540e\u4e00\u7ae0\uff0c\u56de\u987ePython\u7684\u53d1\u5c55\u5386\u7a0b\uff0c\u8ba8\u8bba\u5176\u53d8\u5316\u901f\u7387\uff0c\u5e76\u5c55\u671b\u672a\u6765\u3002\u4f5c\u4e3a\u6536\u5c3e\u7ae0\u8282\uff0c\u5b83\u603b\u7ed3\u5168\u4e66\u7684\u6838\u5fc3\u601d\u60f3\u3002",
    },
}


def split_into_sections(text):
    lines = text.split("\n")
    sections = []
    current_title = "Chapter Introduction"
    current_lines = []
    in_code = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if stripped.startswith(">>>") or stripped.startswith("..."):
            current_lines.append(line)
            in_code = True
            continue

        if in_code and stripped == "":
            current_lines.append(line)
            continue

        if in_code and not stripped.startswith(">>>") and not stripped.startswith("..."):
            if not stripped.startswith("#") and not stripped.startswith("File") and not stripped.startswith("$"):
                in_code = False

        if not stripped:
            current_lines.append(line)
            continue

        if re.match(r"^Chapter\s+\d+", stripped, re.IGNORECASE):
            if current_lines:
                sections.append((current_title, "\n".join(current_lines).strip()))
            current_title = stripped
            current_lines = []
            continue

        if re.match(r"^\d+\.\d+\s+", stripped):
            if current_lines:
                sections.append((current_title, "\n".join(current_lines).strip()))
            current_title = stripped
            current_lines = []
            continue

        if stripped in (
            "Character Encodings",
            "Unicode, Bytes, and Other String Tools",
            "UNICODE DEFAULTS AND UTF-8 MODE",
            "The Unicode Twilight Zone",
            "Dropping the BOM in Python",
            "Making BOMs in Text Editors",
            "Making BOMs in Python",
            "Unicode Normalization: Whither Standard?",
            "Chapter Summary",
            "Test Your Knowledge: Quiz",
            "Test Your Knowledge: Answers",
            "NOTE",
            "Notepad flux",
        ):
            if current_lines:
                sections.append((current_title, "\n".join(current_lines).strip()))
            current_title = stripped
            current_lines = []
            continue

        if re.match(r"^(Example\s+\d+[\.-])", stripped):
            if current_lines:
                sections.append((current_title, "\n".join(current_lines).strip()))
            current_title = stripped
            current_lines = []
            continue

        current_lines.append(line)

    if current_lines:
        sections.append((current_title, "\n".join(current_lines).strip()))

    return sections


def clean_quote(text):
    return text.replace("\n", "\n> ")


def deep_understand(title, body):
    t = title.lower()
    if "unicode" in t or "character encod" in t or "byte string" in t:
        return [
            "- **核心概念**：Unicode是一种为世界上所有书写系统的每个字符分配唯一数字编号的通用编码标准。Python 3中str对象原生支持Unicode，bytes对象处理原始二进制数据",
            "- **底层实现**：Python的str对象在内部使用Unicode编码存储，UTF-8是默认的源文件编码。文本文件通过open()的encoding参数实现编解码，底层调用的是Python的编解码器框架",
            "- **设计原因**：Python 3将Unicode作为字符串的默认编码，消除了Python 2中str和unicode类型的混乱。这种设计符合现代软件国际化的需求",
            "- **实际问题**：跨平台文件读写时，默认编码可能不同（Windows上可能是cp1252，macOS/Linux上是UTF-8），导致非ASCII字符在不同平台间传输时出现乱码",
            "- **初学者误区**：很多人认为UTF-8和Unicode是一回事。实际上Unicode是字符集标准，UTF-8是编码方式；一个Unicode字符可以有多种UTF编码形式",
        ]
    elif "attribute" in t or "method" in t or "getattr" in t or "getattribute" in t:
        return [
            "- **核心概念**：Python的属性访问不是简单的字典查找，而是经过多层协议处理的复杂过程，包括__getattribute__、__getattr__、描述符和数据描述符优先级规则",
            "- **底层实现**：Python的属性查找遵循MRO（方法解析顺序），先在实例的__dict__中查找，然后按类的MRO链查找，最后触发__getattr__。描述符协议（__get__、__set__、__delete__）在查找过程中优先于实例字典",
            "- **设计原因**：描述符协议将属性管理的逻辑从实例中分离出来，使得属性可以跨类复用。属性装饰器property就是描述符的一个特例",
            "- **实际问题**：__getattr__和__getattribute__的递归陷阱\u2014\u2014在__getattribute__中访问self.xxx会再次触发__getattribute__，必须使用object.__getattribute__(self, 'xxx')来避免",
            "- **初学者误区**：很多人认为__getattr__会在所有属性访问时触发，实际上它只在属性未找到时触发；而__getattribute__会在每次访问时触发，但需要小心避免无限递归",
        ]
    elif "decorator" in t:
        return [
            "- **核心概念**：装饰器本质上是一个接受函数或类作为参数并返回新函数或类的可调用对象。它利用Python的闭包和作用域机制，在函数定义时自动修改函数行为",
            "- **底层实现**：当Python执行@decorator语法时，它实际上执行了func = decorator(func)。装饰器返回的wrapper函数通过闭包保留了原始函数的引用和装饰器参数",
            "- **设计原因**：装饰器模式将横切关注点（如日志、计时、权限校验）从业务逻辑中分离出来，使得代码更清晰、更可复用。Python的语法糖使得装饰器使用起来非常简洁",
            "- **实际问题**：装饰器会改变函数的元信息（如__name__、__doc__），需要使用functools.wraps来保留原始函数的属性。这在调试和文档生成时非常重要",
            "- **初学者误区**：很多人认为装饰器只在函数调用时执行，实际上装饰器在函数定义时就执行了（@语法在import时就会运行）。装饰器的参数是在定义时确定的，不是在调用时",
        ]
    elif "metaclass" in t:
        return [
            "- **核心概念**：元类是创建类的类。在Python中，type是所有类的默认元类，类本身就是type的实例。元类允许在类创建时自定义类的行为",
            "- **底层实现**：当Python执行class语句时，它首先收集类字典，然后调用指定的元类（默认是type）的__new__和__init__方法来创建类对象。元类的__new__方法接收类名、父类列表和类字典作为参数",
            "- **设计原因**：元类提供了一种在类创建时注入代码的机制，这在ORM框架、API注册、接口验证等场景中非常有用。它比类装饰器更底层，因为元类控制的是类的创建过程本身",
            "- **实际问题**：元类的继承行为复杂\u2014\u2014元类声明会被子类继承，这可能导致意外的元类冲突。当父类有不同的元类时，Python会尝试自动合并它们",
            "- **初学者误区**：很多人认为元类用于控制类的实例，实际上元类控制的是类本身。元类定义的方法只能通过类访问，不能通过实例访问（这是与普通类方法的根本区别）",
        ]
    else:
        return [
            "- **核心概念**：本章内容涉及Python的核心机制，理解这些概念对于深入掌握Python至关重要",
            "- **底层实现**：Python的内部实现涉及C语言层面的对象模型，理解这些实现有助于编写更高效的代码",
            "- **设计原因**：Python的设计哲学强调可读性和简洁性，这些机制的设计都遵循了这一原则",
            "- **实际问题**：在实际开发中，正确使用这些高级特性可以显著提升代码的质量和可维护性",
            "- **初学者误区**：初学者往往试图过早使用这些高级特性，而忽视了基础知识的扎实掌握",
        ]


def learning_advice(num):
    m = {
        37: ("4/5", "\u638c\u63e1Unicode\u7f16\u7801\u539f\u7406\u3001str\u548cbytes\u7684\u533a\u522b\u3001\u6587\u4ef6\u7f16\u7801\u53c2\u6570\u7684\u4f7f\u7528", "\u5b66\u4e60\u7b2c8\u7ae0\u7684\u5c5e\u6027\u7ba1\u7406\u3001\u7b2c39\u7ae0\u7684\u88c5\u9970\u5668"),
        38: ("5/5", "\u6df1\u5165\u7406\u89e3\u5c5e\u6027\u8bbf\u95ee\u534f\u8bae\u3001\u63cf\u8ff0\u7b26\u534f\u8bae\u3001property\u548c__getattr__/__getattribute__\u7684\u533a\u522b\u4e0e\u8054\u7cfb", "\u5b66\u4e60\u7b2c39\u7ae0\u7684\u88c5\u9970\u5668"),
        39: ("5/5", "\u638c\u63e1\u88c5\u9970\u5668\u7684\u7f16\u5199\u3001\u53c2\u6570\u4f20\u9012\u3001\u5d4c\u5957\u4f7f\u7528\uff0c\u4ee5\u53ca\u88c5\u9970\u5668\u5728\u6846\u67b6\u8bbe\u8ba1\u4e2d\u7684\u5b9e\u9645\u5e94\u7528", "\u5b66\u4e60\u7b2c40\u7ae0\u7684\u5143\u7c7b"),
        40: ("4/5", "\u7406\u89e3\u5143\u7c7b\u7684\u57fa\u672c\u6982\u5ff5\u3001\u58f0\u660e\u65b9\u5f0f\u3001\u7ee7\u627f\u89c4\u5219\uff0c\u4ee5\u53ca\u5143\u7c7b\u4e0e\u7ee7\u627f\u7684\u5173\u7cfb", "\u5b66\u4e60\u7b2c41\u7ae0\u7684\u603b\u7ed3\u5185\u5bb9"),
        41: ("3/5", "\u4e86\u89e3Python\u7684\u53d1\u5c55\u5386\u53f2\u548c\u53d8\u5316\u8d8b\u52bf\uff0c\u5bf9\u5168\u4e66\u5185\u5bb9\u8fdb\u884c\u56de\u987e\u548c\u603b\u7ed3", "\u5f00\u59cb\u5b9e\u9645\u9879\u76ee\u5f00\u53d1"),
    }
    return m.get(num, ("3/5", "\u7406\u89e3\u672c\u7ae0\u6838\u5fc3\u6982\u5ff5", "\u7ee7\u7eed\u5b66\u4e60\u540e\u7eed\u7ae0\u8282"))


def tech_expansion(num):
    m = {
        37: {
            "app": "Unicode\u5904\u7406\u662f\u73b0\u4ee3\u8f6f\u4ef6\u5f00\u53d1\u7684\u57fa\u7840\u9700\u6c42\u2014\u2014Web\u5f00\u53d1\u4e2d\u7684\u56fd\u9645\u5316(i18n)\u3001API\u5f00\u53d1\u4e2d\u7684JSON\u7f16\u7801\u3001\u6587\u4ef6\u5904\u7406\u4e2d\u7684\u7f16\u7801\u8f6c\u6362\u7b49\u90fd\u9760Unicode\u77e5\u8bc6",
            "comp": "| \u7279\u6027 | Python | Java | C++ |\n|---|---|---|---|\n| \u5b57\u7b26\u4e32\u7c7b\u578b | str(Unicode) + bytes | String(Unicode) | char*/wstring |\n| \u9ed8\u8ba4\u7f16\u7801 | UTF-8 | UTF-16 | \u4f9d\u8d56\u5e73\u53f0 |\n| \u6587\u4ef6\u7f16\u7801 | open(encoding=...) | InputStreamReader | \u9700\u7b2c\u4e09\u65b9\u5e93 |\n| \u5b57\u8282\u4e32\u7c7b\u578b | bytes/bytearray | byte[] | char[] |",
            "hist": "Unicode\u6807\u51c6\u4ece1991\u5e74\u5f00\u59cb\u5236\u5b9a\uff0cPython 2.x\u4e2dstr\u548cunicode\u662f\u5206\u5f00\u7684\u7c7b\u578b\uff0cPython 3.x\u7edf\u4e00\u4e3astr=Unicode\u3002Python 3.3+\u5f15\u5165\u4e86PEP 393 flexible string representation",
            "adv": "\u6df1\u5165\u5b66\u4e60\uff1acodecs\u6a21\u5757\u3001locale\u6a21\u5757\u3001sys.getfilesystemencoding()\u3001PEP 393\u3001PEP 597(UTF-8 mode)",
        },
        38: {
            "app": "\u5c5e\u6027\u7ba1\u7406\u673a\u5236\u662fORM\u6846\u67b6(\u5982SQLAlchemy)\u3001\u6570\u636e\u9a8c\u8bc1\u5e93(\u5982Pydantic)\u3001\u4ee3\u7406\u6a21\u5f0f\u5b9e\u73b0\u7684\u6838\u5fc3\u6280\u672f",
            "comp": "| \u7279\u6027 | property | descriptor | __getattr__ |\n|---|---|---|---|\n| \u4f5c\u7528\u8303\u56f4 | \u5355\u4e2a\u5c5e\u6027 | \u5355\u4e2a\u5c5e\u6027 | \u6240\u6709\u672a\u5b9a\u4e49\u5c5e\u6027 |\n| \u662f\u5426\u53ef\u590d\u7528 | \u5426(\u7ed1\u5b9a\u5230\u7c7b) | \u662f(\u72ec\u7acb\u7c7b) | \u662f(\u65b9\u6cd5\u7ea7\u522b) |\n| \u662f\u5426\u62e6\u622a\u8d4b\u503c | \u662f(\u901a\u8fc7setter) | \u662f(\u901a\u8fc7__set__) | \u5426(\u9700\u914d\u5408__setattr__) |\n| \u663e\u793a\u5728dir()\u4e2d | \u662f | \u662f | \u5426 |\n| \u6027\u80fd | \u9ad8 | \u9ad8 | \u4e2d |",
            "hist": "\u63cf\u8ff0\u7b26\u534f\u8bae\u4ecePython 2.2\u5f15\u5165\uff0c\u662fPython 2.x\u65b0\u5f0f\u7c7b(new-style class)\u7684\u6838\u5fc3\u7279\u6027\u4e4b\u4e00\u3002property\u88c5\u9970\u5668\u4ecePython 2.6\u5f00\u59cb\u652f\u6301@\u8bed\u6cd5",
            "adv": "\u6df1\u5165\u5b66\u4e60\uff1a__slots__\u3001__getstate__/__setstate__(pickle\u534f\u8bae)\u3001__reduce__\u3001\u6570\u636e\u7c7b(dataclass)\u7684field\u63cf\u8ff0\u7b26\u3001typing.NamedTuple",
        },
        39: {
            "app": "\u88c5\u9970\u5668\u5e7f\u6cdb\u5e94\u7528\u4e8eWeb\u6846\u67b6(Django/Flask\u8def\u7531\u88c5\u9970\u5668)\u3001\u6d4b\u8bd5\u6846\u67b6(pytest.mark)\u3001\u5f02\u6b65(async/await)\u3001\u7c7b\u578b\u68c0\u67e5(@overload)\u3001\u7f13\u5b58(@lru_cache)\u7b49",
            "comp": "| \u7279\u6027 | \u51fd\u6570\u88c5\u9970\u5668 | \u7c7b\u88c5\u9970\u5668 | \u5143\u7c7b |\n|---|---|---|---|\n| \u4f5c\u7528\u5bf9\u8c61 | \u51fd\u6570/\u65b9\u6cd5 | \u7c7b | \u7c7b |\n| \u6267\u884c\u65f6\u673a | \u51fd\u6570\u5b9a\u4e49\u65f6 | \u7c7b\u5b9a\u4e49\u65f6 | \u7c7b\u5b9a\u4e49\u65f6 |\n| \u8fd4\u56de\u503c | \u65b0\u51fd\u6570 | \u65b0\u7c7b | \u65b0\u7c7b |\n| \u7075\u6d3b\u6027 | \u9ad8 | \u6700\u9ad8 | \u9ad8 |\n| \u590d\u6742\u5ea6 | \u4f4e | \u4e2d | \u9ad8 |",
            "hist": "Python 2.4\u5f15\u5165\u4e86\u51fd\u6570\u88c5\u9970\u5668\u8bed\u6cd5(@)\uff0cPython 2.6\u6269\u5c55\u4e86\u7c7b\u88c5\u9970\u5668\uff0cPEP 318\u548cPEP 3129\u5b9a\u4e49\u4e86\u88c5\u9970\u5668\u89c4\u8303",
            "adv": "\u6df1\u5165\u5b66\u4e60\uff1afunctools.wraps\u3001functools.lru_cache\u3001contextlib.contextmanager\u3001typing.overload\u3001__init_subclass__",
        },
        40: {
            "app": "\u5143\u7c7b\u5728ORM\u6846\u67b6(Django models)\u3001API\u6ce8\u518c(Flask\u8def\u7531)\u3001\u63a5\u53e3\u9a8c\u8bc1\u3001\u5e8f\u5217\u5316\u5e93\u7b49\u4e2d\u6709\u91cd\u8981\u5e94\u7528",
            "comp": "| \u7279\u6027 | \u7c7b\u88c5\u9970\u5668 | \u5143\u7c7b |\n|---|---|---|\n| \u63a7\u5236\u65f6\u673a | \u7c7b\u521b\u5efa\u540e | \u7c7b\u521b\u5efa\u65f6 |\n| \u4fee\u6539\u80fd\u529b | \u53ea\u80fd\u66ff\u6362\u6574\u4e2a\u7c7b | \u53ef\u4ee5\u4fee\u6539\u7c7b\u5b57\u5178 |\n| \u7ee7\u627f | \u4e0d\u81ea\u52a8\u7ee7\u627f | \u81ea\u52a8\u7ee7\u627f |\n| \u7528\u9014 | \u7b80\u5355\u589e\u5f3a | \u6846\u67b6\u7ea7\u5b9a\u5236 |\n| \u590d\u6742\u5ea6 | \u4f4e | \u9ad8 |",
            "hist": "\u5143\u7c7b\u6982\u5ff5\u4ecePython 2.2\u5f15\u5165\uff0cPEP 3115(2006)\u6807\u51c6\u5316\u4e86\u5143\u7c7b\u58f0\u660e\u8bed\u6cd5(metaclass=\u5173\u952e\u5b57)\uff0cPython 3\u4e2d\u5143\u7c7b\u6210\u4e3a\u6807\u51c6\u7279\u6027",
            "adv": "\u6df1\u5165\u5b66\u4e60\uff1atype.__new__\u3001__init_subclass__\u3001abc.ABCMeta\u3001typing.Generic\u3001__class_getitem__",
        },
        41: {
            "app": "\u7406\u89e3Python\u7684\u6f14\u53d8\u6709\u52a9\u4e8e\u9884\u6d4b\u672a\u6765\u8d8b\u52bf\uff0c\u505a\u51fa\u6280\u672f\u9009\u578b\u51b3\u7b56",
            "comp": "| Python\u7248\u672c | \u91cd\u8981\u7279\u6027 | \u53d1\u5e03\u5e74\u4efd |\n|---|---|---|\n| Python 2.0 | List comprehensions, GC | 2000 |\n| Python 2.4 | Decorators | 2004 |\n| Python 3.0 | Unicode by default, print() | 2008 |\n| Python 3.5 | Async/await | 2015 |\n| Python 3.6 | f-strings, variable annotations | 2016 |\n| Python 3.8 | Walrus operator, positional-only args | 2019 |\n| Python 3.10 | Structural pattern matching | 2021 |\n| Python 3.12 | Exception groups, type params | 2023 |",
            "hist": "Python\u7531Guido van Rossum\u4e8e1989\u5e74\u5723\u8bde\u8282\u671f\u95f4\u5f00\u59cb\u5f00\u53d1\uff0c1991\u5e74\u53d1\u5e03\u7b2c\u4e00\u4e2a\u516c\u5f00\u7248\u672c\u3002Python\u7684\u540d\u5b57\u6765\u6e90\u4e8eBBC\u559c\u5267\u8282\u76eeMonty Python's Flying Circus",
            "adv": "\u6df1\u5165\u5b66\u4e60\uff1aPython\u7684\u6f14\u8fdb\u8def\u7ebf\u56fe(PEP\u6d41\u7a0b)\u3001Python\u8f6f\u4ef6\u57fa\u91d1\u4f1a(PSF)\u3001\u6838\u5fc3\u5f00\u53d1\u6d41\u7a0b\u3001PEP 8\u98ce\u683c\u6307\u5357",
        },
    }
    return m.get(num, {"app": "", "comp": "", "hist": "", "adv": ""})


def chapter_summary(num):
    adv = learning_advice(num)
    exp = tech_expansion(num)
    return f"""# \u672c\u7ae0\u603b\u7ed3

## \u6280\u672f\u6269\u5c55\uff08Technical Expansion\uff09
- \u5b9e\u9645\u9879\u76ee\u4e2d\u7684\u5e94\u7528\u573a\u666f
{exp['app']}
- \u4e0e\u5176\u4ed6\u8bed\u8a00\uff08Java/C++\uff09\u7684\u533a\u522b\uff08\u53ef\u7528\u8868\u683c\uff09
{exp['comp']}
- Python \u53d1\u5c55\u5386\u53f2\u80cc\u666f
{exp['hist']}
- \u9ad8\u7ea7\u5f00\u53d1\u8005\u9700\u8981\u638c\u63e1\u7684\u76f8\u5173\u77e5\u8bc6
{exp['adv']}

## \u5b66\u4e60\u5efa\u8bae\uff08Learning Advice\uff09
- \u91cd\u8981\u7a0b\u5ea6\uff08{adv[0]}\uff09
- \u5e94\u8be5\u638c\u63e1\u5230\u4ec0\u4e48\u7a0b\u5ea6
{adv[1]}
- \u540e\u7eed\u5e94\u8be5\u5b66\u4e60\u54ea\u4e9b\u76f8\u5173\u5185\u5bb9
{adv[2]}
"""


def process_chapter(num):
    meta = CHAPTERS[num]
    txt_path = os.path.join("chapters", f"ch{num:02d}.txt")
    md_path = os.path.join("chapters", f"ch{num:02d}.md")

    if not os.path.exists(txt_path):
        print(f"SKIP {txt_path} not found")
        return

    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    sections = split_into_sections(text)
    md = []

    md.append(f"# \u7b2c{num}\u7ae0\uff1a{meta['en']}\uff08{meta['zh']}\uff09")
    md.append("")
    md.append("> **\u539f\u4e66**\uff1a\u300aLearning Python\u300b\uff086th Edition\uff09\uff0c\u4f5c\u8005 Mark Lutz")
    md.append(f"> **\u672c\u7ae0\u5730\u4f4d**\uff1a{meta['pos']}")
    md.append("---")
    md.append("")

    for sec_title, sec_body in sections:
        # Skip very short sections (likely code fragments)
        if len(sec_body.strip()) < 50:
            continue

        md.append(f"## {sec_title}")
        md.append("")

        # Split into subsections if body has numbered subsections
        subsections = re.split(r"\n(?=\d+\.\d+\s+)", sec_body)
        if len(subsections) > 1:
            for sub in subsections:
                sub = sub.strip()
                if not sub:
                    continue
                # Find the subsection heading
                m = re.match(r"^(\d+\.\d+)\s+(.+)", sub)
                if m:
                    sub_head = f"{m.group(1)} {m.group(2)}"
                    sub_body = sub[m.end():].strip()
                else:
                    sub_head = sec_title
                    sub_body = sub

                md.append(f"### {sub_head}")
                md.append("")
                md.append("\u2014\u2014\u2014\u2014\u82f1\u6587\u539f\u6587\u2014\u2014\u2014\u2014")
                md.append("")
                md.append("> " + clean_quote(sub_body))
                md.append("")
                md.append("\u2014\u2014\u2014\u2014\u4e2d\u6587\u7ffb\u8bd1\u2014\u2014\u2014\u2014")
                md.append("")
                md.append("> [\u5f85\u7ffb\u8bd1]")
                md.append("")
                md.append("\u2014\u2014\u2014\u2014\u6df1\u5ea6\u7406\u89e3\u2014\u2014\u2014\u2014")
                md.append("")
                for p in deep_understand(sub_head, sub_body):
                    md.append(p)
                md.append("")
        else:
            md.append("\u2014\u2014\u2014\u2014\u82f1\u6587\u539f\u6587\u2014\u2014\u2014\u2014")
            md.append("")
            md.append("> " + clean_quote(sec_body))
            md.append("")
            md.append("\u2014\u2014\u2014\u2014\u4e2d\u6587\u7ffb\u8bd1\u2014\u2014\u2014\u2014")
            md.append("")
            md.append("> [\u5f85\u7ffb\u8bd1]")
            md.append("")
            md.append("\u2014\u2014\u2014\u2014\u6df1\u5ea6\u7406\u89e3\u2014\u2014\u2014\u2014")
            md.append("")
            for p in deep_understand(sec_title, sec_body):
                md.append(p)
            md.append("")

        md.append("---")
        md.append("")

    md.append(chapter_summary(num))

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"ch{num:02d}: {len(text)} chars -> {md_path} ({len(sections)} sections)")


def main():
    for n in range(37, 42):
        process_chapter(n)
    print("DONE")


if __name__ == "__main__":
    main()