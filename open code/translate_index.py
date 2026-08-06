# -*- coding: utf-8 -*-
"""
Translate chapters/index.md so every entry has English（中文） pair form.
Primary source: section titles already bilingual in ch*.md / appendix*.md.
Secondary: large phrase + word glossary for Python/book terms.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")
INDEX = ROOT / "index.md"

try:
    from index_extra_gloss import EXTRA as EXTRA_GLOSS
except Exception:
    EXTRA_GLOSS = {}


def load_title_pairs() -> dict:
    """Map english section title lower -> chinese from existing md headings."""
    pairs = {}
    for p in list(ROOT.glob("ch*.md")) + list(ROOT.glob("appendix_*.md")) + list(ROOT.glob("about*.md")):
        for L in p.read_text(encoding="utf-8").splitlines():
            if not L.startswith("## "):
                continue
            t = L[3:].strip()
            t = re.sub(r"^\d+\.\d+\s+", "", t)
            # strip leading numbering like 22.4.1
            t = re.sub(r"^\d+(?:\.\d+)+\s+", "", t)
            m = re.match(r"^(.+?)（(.+?)）\s*$", t)
            if not m:
                continue
            a, b = m.group(1).strip(), m.group(2).strip()
            # drop markdown ticks for matching
            a_clean = a.replace("`", "")
            b_clean = b.replace("`", "")
            if re.search(r"[\u4e00-\u9fff]", a_clean) and re.search(r"[A-Za-z]", b_clean):
                pairs[norm(b_clean)] = a_clean
            elif re.search(r"[\u4e00-\u9fff]", b_clean) and re.search(r"[A-Za-z]", a_clean):
                pairs[norm(a_clean)] = b_clean
    return pairs


def norm(s: str) -> str:
    s = s.strip()
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    s = s.replace("–", "-").replace("—", "-").replace("…", "...")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*-\s*", "-", s)  # "built- in" -> "built-in" partially
    s = s.replace("- ", "-").replace(" -", "-")
    return s.lower()


# Comprehensive phrase glossary (english lower key -> zh). Longest match preferred.
# Includes index terms + common section titles not captured from md.
PHRASES = {
    # symbols / misc
    "# comments": "# 注释",
    "$ character in interactive coding": "交互式编程中的 $ 字符",
    "$ character": "$ 字符",
    "* (asterisk) use in code": "代码中 *（星号）的用法",
    "absolute imports": "绝对导入",
    "relative imports": "相对导入",
    "relative and absolute imports": "相对与绝对导入",
    "abstract superclasses": "抽象超类",
    "preview: abstract superclasses with library tools": "预览：用库工具实现抽象超类",
    "stream processors revisited": "再访流处理器",
    "library tools": "库工具",
    "access-by-key files": "按键访问文件",
    "other file tools": "其他文件工具",
    "aggregation": "聚合",
    "composition": "组合",
    'oop and composition: "has-a" relationships': "OOP 与组合：“有一个”关系",
    "oop and composition: “has-a” relationships": "OOP 与组合：“有一个”关系",
    'oop and delegation: "like-a" relationships': "OOP 与委托：“像一个”关系",
    "oop and delegation: “like-a” relationships": "OOP 与委托：“像一个”关系",
    "other ways to combine classes: composites": "组合类的其他方式：复合",
    "ai (artificial intelligence)": "AI（人工智能）",
    "artificial intelligence (ai)": "人工智能（AI）",
    "and more: ai, games, images, qa, excel, apps...": "还有更多：AI、游戏、图像、QA、Excel、应用…",
    "and more: ai, games, images, qa, excel, apps…": "还有更多：AI、游戏、图像、QA、Excel、应用…",
    "ajax (asynchronous javascript and xml)": "Ajax（异步 JavaScript 与 XML）",
    "internet and web scripting": "互联网与 Web 脚本",
    "aliasing": "别名（共享引用）",
    "arguments and shared references": "参数与共享引用",
    "__all__ variable": "__all__ 变量",
    "minimizing from * damage: _x and __all__": "尽量减少 from * 的破坏：_X 与 __all__",
    "android": "Android",
    "interactive coding and": "与交互式编程",
    "starting an interactive repl": "启动交互式 REPL",
    "python installation": "Python 安装",
    "installing python": "安装 Python",
    "python on": "上的 Python",
    "using python on android": "在 Android 上使用 Python",
    "using python on windows": "在 Windows 上使用 Python",
    "annotations, functions": "函数注解",
    "general function concepts": "函数通用概念",
    "function annotations and decorations": "函数注解与装饰",
    "function decorators alternative: preview": "函数装饰器替代方案：预览",
    "anonymous functions": "匿名函数",
    "lambda makes anonymous functions": "lambda 创建匿名函数",
    "aot (ahead-of-time) compilers": "AOT（提前）编译器",
    "aot (ahead-of-time)": "AOT（提前编译）",
    "ahead-of-time compilers for speed": "为速度而生的提前编译器",
    "python implementation alternatives": "Python 实现替代方案",
    "pythran": "PyThran",
    "shed skin": "Shed Skin",
    "arbitrary arguments, argument matching": "任意参数，参数匹配",
    "arbitrary arguments examples": "任意参数示例",
    "why arbitrary arguments?": "为什么需要任意参数？",
    "arbitrary arguments": "任意参数",
    "arbitrary expressions": "任意表达式",
    "sequence operations": "序列操作",
    "arbitrary scope nesting": "任意深度的作用域嵌套",
    "architecture": "架构",
    "python program architecture": "Python 程序架构",
    "argument matching": "参数匹配",
    "special argument-matching modes": "特殊参数匹配模式",
    "argument matching overview": "参数匹配概览",
    "argument matching syntax": "参数匹配语法",
    "argument ordering": "参数顺序",
    "calls ordering": "调用时的参数顺序",
    "definition ordering": "定义时的参数顺序",
    "boundary cases": "边界情况",
    "formal definition": "形式定义",
    "formal definitions": "形式定义",
    "argument passing": "参数传递",
    "argument-passing basics": "参数传递基础",
    "argument-matching basics": "参数匹配基础",
    "argument passing details": "参数传递细节",
    "keyword and default examples": "关键字与默认值示例",
    "combining keywords and defaults": "组合关键字与默认值",
    "simulating output parameters and multiple results": "模拟输出参数与多返回值",
    "avoiding mutable argument changes": "避免可变参数被修改",
    "immutable arguments": "不可变参数",
    "mutable arguments": "可变参数",
    "keyword-only arguments": "仅限关键字参数",
    "why keyword-only arguments?": "为什么需要仅限关键字参数？",
    "using keyword-only arguments": "使用仅限关键字参数",
    "using keyword- only arguments": "使用仅限关键字参数",
    "positional-only arguments": "仅限位置参数",
    "calls: unpacking arguments": "调用：解包参数",
    "definitions: collecting arguments": "定义：收集参数",
    "example: generalized set functions": "示例：通用集合函数",
    "testing the code": "测试代码",
    "example: the min wakeup call": "示例：min 的醒脑练习",
    "the punch line": "点睛之笔",
    "example: rolling your own print": "示例：自己实现 print",
    "example: validating function arguments": "示例：校验函数参数",
    "the goal": "目标",
    "a basic range-testing decorator for positional arguments": "针对位置参数的基础范围校验装饰器",
    "def statements": "def 语句",
    "part iv, functions and generators": "第 IV 部分：函数与生成器",
    "part iv": "第 IV 部分",
    "part i, getting started": "第 I 部分：入门",
    "part ii": "第 II 部分",
    "part iii": "第 III 部分",
    "part v": "第 V 部分",
    "part vi": "第 VI 部分",
    "part vii": "第 VII 部分",
    "decorator arguments": "装饰器参数",
    "adding decorator arguments": "添加装饰器参数",
    "descriptor method arguments": "描述符方法参数",
    "function design concepts": "函数设计概念",
    "the first-class object model": "一等对象模型",
    "scopes and argument defaults": "作用域与参数默认值",
    "loops require defaults, not scopes": "循环需要默认值，而非作用域",
    "same argument lists": "相同的参数列表",
    "lambda basics": "lambda 基础",
    "arithmeticerror exception class": "ArithmeticError 异常类",
    "arithmeticerror": "ArithmeticError",
    "built-in exception classes": "内置异常类",
    "arrays, associative": "关联数组",
    "dictionaries": "字典",
    "as clause": "as 子句",
    "the as extension for import and from": "import 与 from 的 as 扩展",
    "ascii": "ASCII",
    "character representations": "字符表示",
    "character encodings": "字符编码",
    "latin-1 and": "与 Latin-1",
    "utf-8 and": "与 UTF-8",
    "aspect-oriented programming": "面向切面编程",
    "why decorators?": "为什么要用装饰器？",
    "assert statement": "assert 语句",
    "the assert statement": "assert 语句",
    "as conditional raise statement": "作为有条件的 raise",
    "example: trapping constraints (but not errors!)": "示例：捕获约束（而非错误！）",
    "constraint trapping": "约束捕获",
    "assignments": "赋值",
    "assignment syntax forms": "赋值语法形式",
    "basic assignments": "基本赋值",
    "augmented assignments": "增强赋值",
    "augmented assignment and shared references": "增强赋值与共享引用",
    "extended-unpacking assignments": "扩展解包赋值",
    "extended unpacking in action": "扩展解包实战",
    "multiple-target assignments": "多目标赋值",
    "augmented": "增强赋值",
    "basic assignment": "基本赋值",
    "extended-unpacking": "扩展解包",
    "multiple-targets": "多目标",
    "implicit": "隐式",
    "class attributes": "类属性",
    "general syntax and usage": "一般语法与用法",
    "application to for loops": "应用于 for 循环",
    "function calls": "函数调用",
    "function definitions": "函数定义",
    "function headers": "函数头部",
    "from": "from",
    "import": "import",
    "changing mutables in modules": "在模块中修改可变对象",
    "lists": "列表",
    "module attribute creation": "模块属性的创建",
    "how files generate namespaces": "文件如何生成命名空间",
    "sequence assignments": "序列赋值",
    "advanced sequence-assignment patterns": "高级序列赋值模式",
    "advanced sequence- assignment patterns": "高级序列赋值模式",
    "name references, nested scopes": "名字引用与嵌套作用域",
    "nested scopes overview": "嵌套作用域概览",
    "common coding gotchas": "常见编码陷阱",
    "mutables": "可变对象",
    "__setitem__ method": "__setitem__ 方法",
    "intercepting item assignments": "拦截项赋值",
    "arguments": "参数",
    "defaults": "默认值",
    "keywords": "关键字",
    "syntax": "语法",
    "matching arguments": "匹配参数",
    "multiple results simulation": "多返回值模拟",
    "output parameter simulation": "输出参数模拟",
    "references, shared": "共享引用",
    "passing arguments": "传递参数",
    "passing": "传递",
    "passing functions as": "把函数当作参数传递",
    "positional": "位置式",
    "validation": "校验",
    "super function": "super 函数",
    "callables": "可调用对象",
    "arbitrary": "任意",
    "changes": "修改",
    "minimum value calculation": "最小值计算",
    "mins.py example": "mins.py 示例",
    "print function example": "print 函数示例",
    "collecting arguments": "收集参数",
    "unpacking arguments": "解包参数",
    "calls": "调用",
    "definitions": "定义",
    "generalized set functions example": "通用集合函数示例",
    "immutable": "不可变",
    "mutable": "可变",
    "keyword-only": "仅限关键字",
    "coupling": "耦合",
    "scopes": "作用域",
    "decorators": "装饰器",
    "class decorators": "类装饰器",
    "descriptors": "描述符",
    "descriptor": "描述符",
    "object": "对象",
    "objects": "对象",
    "composition": "组合",
    # platforms
    "windows": "Windows",
    "command prompt": "命令提示符",
    "idle": "IDLE",
    "wsl": "WSL",
    "wsl (windows subsystem for linux)": "WSL（Windows 的 Linux 子系统）",
    "directory paths": "目录路径",
    "files in action": "文件实战",
    "running files with command lines": "用命令行运行文件",
    "working directory, commands": "工作目录与命令",
    "other launch options": "其他启动选项",
    "other ides for python": "其他 Python IDE",
    "vscode": "VS Code",
    "wing": "Wing IDE",
    # unicode / files
    "utf-8 encoding": "UTF-8 编码",
    "utf-16 encoding": "UTF-16 编码",
    "utf-32 encoding": "UTF-32 编码",
    "coding unicode strings in python": "在 Python 中编写 Unicode 字符串",
    "escape sequences are special characters": "转义序列是特殊字符",
    "source-file encoding declarations": "源文件编码声明",
    "making boms in python": "在 Python 中制作 BOM",
    "bom (byte order marker)": "BOM（字节顺序标记）",
    "filenames in open and other filename tools": "open 中的文件名与其他文件名工具",
    "string literals": "字符串字面量",
    "other common string methods": "其他常用字符串方法",
    "wide-character strings": "宽字符字符串",
    "unicode": "Unicode",
    "byte strings": "字节字符串",
    "whitespace": "空白",
    "end of indentation is end of block": "缩进结束即代码块结束",
    # loops / control
    "while loops": "while 循环",
    "for loops": "for 循环",
    "examples": "示例",
    "break, continue, pass, and the loop else": "break、continue、pass 与循环 else",
    "the named-assignment alternative": "海象赋值替代方案",
    "the nested-code alternative": "嵌套代码替代方案",
    "the ellipsis-literal alternative": "省略号字面量替代方案",
    "a simple interactive loop": "简单交互循环",
    "sequence scans: while, range, and for": "序列扫描：while、range 与 for",
    "named assignment": "命名赋值（海象）",
    "nested code": "嵌套代码",
    "do until": "do-until 风格",
    "ellipsis": "省略号",
    "pass statement": "pass 语句",
    "break statement": "break 语句",
    "continue statement": "continue 语句",
    "break statements": "break 语句",
    "else clause": "else 子句",
    "loop else": "循环 else",
    "why the loop else?": "为什么要有循环 else？",
    "general format": "一般格式",
    "break statement, break-the named-assignment alternative": "break 语句——海象赋值替代",
    "continue statement, continue-the nested-code alternative": "continue 语句——嵌套代码替代",
    "pass statement, pass-the ellipsis-literal alternative": "pass 语句——省略号字面量替代",
    # exceptions / with
    "exceptions": "异常",
    "exception": "异常",
    "try statement": "try 语句",
    "raise statement": "raise 语句",
    "functions can signal conditions with raise": "函数可用 raise 发出条件信号",
    "the with statement and context managers": "with 语句与上下文管理器",
    "basic with usage": "with 基本用法",
    "multiple context managers": "多个上下文管理器",
    "the context-management protocol": "上下文管理协议",
    "termination actions": "终止动作",
    "termination handlers": "终止处理器",
    "the termination-handlers shoot-out": "终止处理器大比拼",
    "context managers": "上下文管理器",
    "context managers, multiple": "多个上下文管理器",
    "context-management protocol": "上下文管理协议",
    # iteration
    "iteration": "迭代",
    "iterations": "迭代",
    "iterables": "可迭代对象",
    "iterable": "可迭代对象",
    "iterators": "迭代器",
    "iterator": "迭代器",
    "iteration protocol": "迭代协议",
    "iteration protocol integration": "与迭代协议的集成",
    "user-defined iterables": "用户定义的可迭代对象",
    "multiple iterators with yield": "用 yield 实现多个迭代器",
    "coding alternative: __iter__ plus yield": "编码替代：__iter__ 加 yield",
    "generator functions": "生成器函数",
    "generator expressions": "生成器表达式",
    "generator objects": "生成器对象",
    "generators": "生成器",
    "the yield from extension": "yield from 扩展",
    "yield statement": "yield 语句",
    "yield function, generator objects": "yield 与生成器对象",
    "advanced function tools": "高级函数工具",
    "comprehensions": "推导式",
    "list comprehensions": "列表推导式",
    "dict comprehensions": "字典推导式",
    "set comprehensions": "集合推导式",
    "virtual sequences": "虚拟序列",
    "item iteration: for loops": "按项迭代：for 循环",
    "dictionary key/value/item view objects": "字典 key/value/item 视图对象",
    "parallel traversals: zip": "并行遍历：zip",
    "more zip roles: dictionaries": "zip 的更多角色：字典",
    "reprise: dictionaries, range, enumerate, and zip": "重温：字典、range、enumerate 与 zip",
    "example: emulating zip and map": "示例：模拟 zip 与 map",
    "coding your own zip and 2.x map": "自己实现 zip 与 2.X 的 map",
    "zip function": "zip 函数",
    "zip object": "zip 对象",
    "emulating": "模拟",
    # scopes / vars
    "python scopes basics": "Python 作用域基础",
    "variables, objects, and references": "变量、对象与引用",
    "running code interactively": "交互式运行代码",
    "variable name rules": "变量命名规则",
    "names have no type, but objects do": "名字无类型，对象有类型",
    "program design: minimize global variables": "程序设计：尽量减少全局变量",
    "segue: local variables": "过渡：局部变量",
    "preview: other python scopes": "预览：Python 的其他作用域",
    "scopes and comprehension variables": "作用域与推导式变量",
    "enclosing scopes and loop variables": "外层作用域与循环变量",
    "imports versus scopes": "导入与作用域",
    "from * can obscure the meaning of variables": "from * 可能模糊变量含义",
    "function attributes": "函数属性",
    "module filenames": "模块文件名",
    "variables": "变量",
    "creating": "创建",
    "global": "全局",
    "local": "局部",
    "static locals": "静态局部量",
    "loops": "循环",
    "names": "名字",
    "naming rules": "命名规则",
    "references": "引用",
    "types": "类型",
    "use": "用法",
    "program design": "程序设计",
    "from * statement": "from * 语句",
    "state, decorators": "状态与装饰器",
    "imports": "导入",
    "values method": "values 方法",
    "view objects": "视图对象",
    "visibility": "可见性",
    "the python virtual machine (pvm)": "Python 虚拟机（PVM）",
    "pvm (python virtual machine)": "PVM（Python 虚拟机）",
    "virtual machines (vms)": "虚拟机（VM）",
    "vms (virtual machines)": "虚拟机（VM）",
    "virtual machines (vms) (see vms (virtual machines)": "虚拟机（见 VMs）",
    # decorators / metaclasses / attrs
    "managed attributes": "管理属性",
    "metaclasses": "元类",
    "metaclass": "元类",
    "metaclasses and inheritance": "元类与继承",
    "metaclass methods": "元类方法",
    "metaclass versus superclass": "元类与超类",
    "metaclass inheritance": "元类继承",
    "inheritance": "继承",
    "multiple inheritance": "多重继承",
    "decorator nesting": "装饰器嵌套",
    "managing calls and instances": "管理调用与实例",
    "what should be wrapped": "应该包装什么",
    "pseudoprivate class attributes": "伪私有类属性",
    'using "__x" pseudoprivate names': "使用 “__X” 伪私有名",
    "using “__x” pseudoprivate names": "使用 “__X” 伪私有名",
    "_x prefix": "_X 前缀",
    "__x pseudoprivate name mangling": "__X 伪私有名称改写",
    "wrappers": "包装器",
    "call proxies": "调用代理",
    "layers": "层",
    "stacking": "堆叠",
    'wrapping code, "overwrapping-itis"': "包装代码，“过度包装症”",
    "wrapping code, “overwrapping-itis”": "包装代码，“过度包装症”",
    "code wrapping, “overwrapping-itis”": "代码包装，“过度包装症”",
    'code wrapping, "overwrapping-itis"': "代码包装，“过度包装症”",
    "user-defined function decorators": "用户定义的函数装饰器",
    "a first look at user-defined function decorators": "用户定义函数装饰器初探",
    "user-defined docstrings": "用户定义的文档字符串",
    "user-defined exceptions, nonerror conditions": "用户定义异常与非错误条件",
    "a first look at class decorators and metaclasses": "类装饰器与元类初探",
    # domains / slogans
    "it's powerful": "它很强大",
    "it’s powerful": "它很强大",
    "utilities": "工具",
    "library utilities": "库工具",
    "third-party": "第三方",
    "guis and uis": "GUI 与 UI",
    "component integration": "组件集成",
    "database access": "数据库访问",
    "web scripting": "Web 脚本",
    "web server scripts": "Web 服务器脚本",
    "webassembly": "WebAssembly",
    "webassembly for browsers": "浏览器中的 WebAssembly",
    "wasm (webassembly)": "Wasm（WebAssembly）",
    "xml-rpc": "XML-RPC",
    "zodb": "ZODB",
    "zope": "Zope",
    "wxpython": "wxPython",
    "test your knowledge: quiz": "知识测验：测验",
    "test your knowledge: answers": "知识测验：答案",
    "test your knowledge": "知识测验",
    "chapter summary": "本章小结",
    "what not to type: prompts and comments": "不要键入的内容：提示符与注释",
    # more common index leftovers
    "bounds": "边界",
    "bounds checking": "边界检查",
    "buffering": "缓冲",
    "extending": "扩展",
    "repetition": "重复",
    "repetition adds one level deep": "重复只增加一层深度",
    "formatting": "格式化",
    "executing": "执行",
    "step 3: run it": "第 3 步：运行它",
    "step 2: compile it (maybe)": "第 2 步：编译它（或许）",
    "magic number": "魔数",
    "ok, but what’s the downside?": "好，但缺点是什么？",
    "ok, but what's the downside?": "好，但缺点是什么？",
    "pypy": "PyPy",
    "character code conversion": "字符码转换",
    "character-code conversions": "字符码转换",
    "nested": "嵌套",
    "code folders": "代码目录",
    "colons": "冒号",
    "launchers": "启动器",
    "command-line launchers": "命令行启动器",
    "commas": "逗号",
    "completion certificate": "结业证书",
    "encore: print your own completion certificate!": "安可：打印你自己的结业证书！",
    "composites": "复合对象",
    "multiple-choice selection": "多选分支",
    "multiple-choice selections": "多选分支",
    "handling larger actions": "处理更大型动作",
    "if clause": "if 子句",
    "filter clauses: if": "过滤子句：if",
    "constraints": "约束",
    "constructors": "构造器",
    "customizing": "定制",
    "step 5: customizing constructors, too": "第 5 步：也定制构造器",
    "control language": "控制语言",
    'is python a "scripting language"?': "Python 是“脚本语言”吗？",
    "is python a “scripting language”?": "Python 是“脚本语言”吗？",
    "conversions": "转换",
    "copies": "拷贝",
    "cyclic data": "循环数据",
    "metafunctions": "元函数",
    "runtime declarations": "运行时声明",
    "runtime execution": "运行时执行",
    "def executes at runtime": "def 在运行时执行",
    "development implications": "对开发的影响",
    "directories": "目录",
    "pythonpath": "PYTHONPATH",
    "search-path components": "搜索路径组成部分",
    "configuring the search path": "配置搜索路径",
    "site-packages": "site-packages",
    "standards": "标准",
    "docstring standards": "文档字符串标准",
    "priorities": "优先级",
    "embedding": "嵌入",
    "concurrent tasks": "并发任务",
    "as_completed": "as_completed",
    "await": "await",
    "gather": "gather",
    "running concurrent tasks with “as_completed” and “gather”": "用 as_completed 与 gather 运行并发任务",
    'running concurrent tasks with "as_completed" and "gather"': "用 as_completed 与 gather 运行并发任务",
    "running concurrent tasks with “await” and “async def”": "用 await 与 async def 运行并发任务",
    'running concurrent tasks with "await" and "async def"': "用 await 与 async def 运行并发任务",
    "running serial tasks with normal blocking calls": "用普通阻塞调用运行串行任务",
    "how not to use async functions": "如何不要使用异步函数",
    "asynchronous functions: the short story": "异步函数：简短故事",
    "i/o (input/output) operations": "I/O（输入/输出）操作",
    "serial tasks": "串行任务",
    "tasks to avoid": "应避免的任务",
    "attribute accessors": "属性访问器",
    "api": "API",
    "boolean type": "布尔类型",
    "boolean values": "布尔值",
    "booleans": "布尔",
    "baseexception": "BaseException",
    "baseexception exception class": "BaseException 异常类",
    "beautiful soup": "Beautiful Soup",
    "beeware toga": "BeeWare Toga",
    "boost.python": "Boost.Python",
    "breaking out of multiple nested loops: “go to”": "跳出多层嵌套循环：“goto”",
    'breaking out of multiple nested loops: "go to"': "跳出多层嵌套循环：“goto”",
    "cffi": "CFFI",
    "cpython": "CPython",
    "csv module": "CSV 模块",
    "csv module, object storage": "CSV 模块与对象存储",
    "cwd (current working directory)": "CWD（当前工作目录）",
    "chaquopy": "Chaquopy",
    "cinder": "Cinder",
    "comprehensions versus type calls and generators": "推导式对比类型调用与生成器",
    "cython": "Cython",
    "dflr": "DFLR",
    "dflr (depth first, left to right)": "DFLR（深度优先、从左到右）",
    "dflr (depth first, then left to right)": "DFLR（深度优先、然后从左到右）",
    "django": "Django",
    "durus": "Durus",
    "excel": "Excel",
    "expressions": "表达式",
    "fifo (first in, first out), queues": "FIFO（先进先出）队列",
    "fifo (first-in-first-out)": "FIFO（先进先出）",
    "net framework for windows": ".NET Framework（Windows）",
    ".net framework for windows": ".NET Framework（Windows）",
    ".pth path-file": ".pth 路径文件",
    ".pth path-file directory": ".pth 路径文件目录",
    ".pyc files": ".pyc 文件",
    "-function attributes: changeable": "函数属性：可变",
    "are special characters": "是特殊字符",
    "alternatives": "替代方案",
    "bom headers": "BOM 头",
    # word-level essentials
    "class": "类",
    "classes": "类",
    "instance": "实例",
    "instances": "实例",
    "method": "方法",
    "methods": "方法",
    "function": "函数",
    "functions": "函数",
    "module": "模块",
    "modules": "模块",
    "package": "包",
    "packages": "包",
    "namespace": "命名空间",
    "namespaces": "命名空间",
    "attribute": "属性",
    "attributes": "属性",
    "property": "property（属性）",
    "properties": "properties（属性）",
    "slot": "slot",
    "slots": "slots（插槽）",
    "superclass": "超类",
    "superclasses": "超类",
    "subclass": "子类",
    "subclasses": "子类",
    "statement": "语句",
    "statements": "语句",
    "expression": "表达式",
    "operator": "运算符",
    "operators": "运算符",
    "operation": "操作",
    "operations": "操作",
    "protocol": "协议",
    "protocols": "协议",
    "model": "模型",
    "models": "模型",
    "tool": "工具",
    "tools": "工具",
    "file": "文件",
    "files": "文件",
    "string": "字符串",
    "strings": "字符串",
    "list": "列表",
    "tuple": "元组",
    "tuples": "元组",
    "set": "集合",
    "sets": "集合",
    "dict": "字典",
    "dictionary": "字典",
    "number": "数字",
    "numbers": "数字",
    "integer": "整数",
    "integers": "整数",
    "float": "浮点数",
    "floats": "浮点数",
    "boolean": "布尔",
    "none": "None",
    "true": "True",
    "false": "False",
    "sequence": "序列",
    "sequences": "序列",
    "mapping": "映射",
    "mappings": "映射",
    "byte": "字节",
    "bytes": "字节串",
    "bytecode": "字节码",
    "compiler": "编译器",
    "compilers": "编译器",
    "interpreter": "解释器",
    "script": "脚本",
    "scripts": "脚本",
    "program": "程序",
    "programs": "程序",
    "design": "设计",
    "concept": "概念",
    "concepts": "概念",
    "basic": "基本",
    "basics": "基础",
    "overview": "概览",
    "details": "细节",
    "example": "示例",
    "preview": "预览",
    "alternative": "替代方案",
    "extension": "扩展",
    "extensions": "扩展",
    "usage": "用法",
    "rule": "规则",
    "rules": "规则",
    "name": "名字",
    "type": "类型",
    "value": "值",
    "values": "值",
    "key": "键",
    "keys": "键",
    "item": "项",
    "items": "项",
    "reference": "引用",
    "shared references": "共享引用",
    "copy": "拷贝",
    "copying": "拷贝",
    "shallow copy": "浅拷贝",
    "deep copy": "深拷贝",
    "mutable": "可变",
    "immutable": "不可变",
    "immutability": "不可变性",
    "dynamic typing": "动态类型",
    "static typing": "静态类型",
    "type hints": "类型提示",
    "annotations": "注解",
    "docstring": "文档字符串",
    "docstrings": "文档字符串",
    "documentation": "文档",
    "comments": "注释",
    "comment": "注释",
    "indentation": "缩进",
    "prompt": "提示符",
    "prompts": "提示符",
    "interactive": "交互式",
    "interactive coding": "交互式编程",
    "repl": "REPL",
    "ide": "IDE",
    "ides": "IDE",
    "gui": "GUI",
    "ui": "UI",
    "database": "数据库",
    "persistence": "持久化",
    "serialization": "序列化",
    "debugging": "调试",
    "testing": "测试",
    "performance": "性能",
    "optimization": "优化",
    "memory": "内存",
    "speed": "速度",
    "portability": "可移植性",
    "productivity": "生产力",
    "quality": "质量",
    "readability": "可读性",
    "reuse": "复用",
    "polymorphism": "多态",
    "encapsulation": "封装",
    "delegation": "委托",
    "factory": "工厂",
    "proxy": "代理",
    "mixin": "混入",
    "interface": "接口",
    "abstract": "抽象",
    "concrete": "具体",
    "generic": "通用",
    "overloading": "重载",
    "overriding": "覆盖",
    "hook": "钩子",
    "hooks": "钩子",
    "callback": "回调",
    "state": "状态",
    "closure": "闭包",
    "closures": "闭包",
    "built-in": "内置",
    "built-ins": "内置",
    "user-defined": "用户定义",
    "standard library": "标准库",
    "library": "库",
    "installation": "安装",
    "installing": "安装",
    "running": "运行",
    "coding": "编码",
    "implementation": "实现",
    "implementations": "实现",
    "and": "与",
    "or": "或",
    "with": "带",
    "for": "用于",
    "in": "中的",
    "of": "的",
    "to": "到",
    "vs": "对比",
    "versus": "对比",
    "the": "",
    "a": "",
    "an": "",
}


def build_phrase_list(title_pairs: dict):
    d = dict(PHRASES)
    d.update(EXTRA_GLOSS)
    # title pairs override / extend (highest priority for section names)
    for k, v in title_pairs.items():
        d[k] = v
    # longest first
    return sorted(((norm(k), v) for k, v in d.items() if v is not None), key=lambda kv: (-len(kv[0]), kv[0]))


def lookup_exact(text: str, phrases) -> str | None:
    key = norm(text)
    key2 = re.sub(r"\s*-\s*", "-", key)
    key3 = key.rstrip(" .")
    for eng, zh in phrases:
        if key == eng or key2 == eng or key3 == eng:
            return zh
        # tolerate extra spaces around hyphen
        if key.replace(" ", "") == eng.replace(" ", ""):
            return zh
    return None


def translate_text(text: str, phrases) -> str | None:
    """Return Chinese gloss or None if cannot translate well."""
    if not text or not text.strip():
        return None
    raw = text.strip()
    if re.search(r"[\u4e00-\u9fff]", raw):
        return None  # already Chinese
    exact = lookup_exact(raw, phrases)
    if exact is not None:
        return exact if exact else None

    # Tokenize into words and separators
    tokens = re.findall(r"[A-Za-z0-9_]+(?:'[A-Za-z]+)?(?:\.[A-Za-z0-9_]+)*|__\w+__|_\w+|[^\sA-Za-z0-9_]+|\s+", raw)
    words = []
    widx = []
    for i, tok in enumerate(tokens):
        if re.match(r"^[A-Za-z0-9_]", tok) or tok.startswith("__") or (tok.startswith("_") and len(tok) > 1):
            words.append(tok.lower())
            widx.append(i)
    if not words:
        return None

    n = len(words)
    out_w = [None] * n
    i = 0
    matched_any = False
    while i < n:
        hit = False
        for L in range(min(10, n - i), 0, -1):
            span = " ".join(words[i : i + L])
            span_h = "-".join(words[i : i + L])
            for eng, zh in phrases:
                if span == eng or span_h == eng:
                    if zh:
                        out_w[i] = zh
                        for k in range(i + 1, i + L):
                            out_w[k] = ""
                        matched_any = True
                    else:
                        for k in range(i, i + L):
                            out_w[k] = ""
                    i += L
                    hit = True
                    break
            if hit:
                break
        if not hit:
            # keep code-like identifiers as-is
            out_w[i] = tokens[widx[i]]
            i += 1

    if not matched_any:
        return None

    out_tokens = list(tokens)
    for wi, ti in enumerate(widx):
        val = out_w[wi]
        if val is None:
            continue
        out_tokens[ti] = val
    result = "".join(out_tokens)
    result = re.sub(r"[ \t]{2,}", " ", result)
    result = re.sub(r" +([,.;:!?）】」/])", r"\1", result)
    result = re.sub(r"([（【「]) +", r"\1", result)
    # join Chinese with no space, but keep spaces around leftover english
    result = re.sub(r"([\u4e00-\u9fff])\s+([\u4e00-\u9fff])", r"\1\2", result)
    result = re.sub(r"([\u4e00-\u9fff])\s+([A-Za-z0-9_])", r"\1 \2", result)
    result = re.sub(r"([A-Za-z0-9_])\s+([\u4e00-\u9fff])", r"\1 \2", result)
    result = result.strip(" 、,; ")
    if not result or not re.search(r"[\u4e00-\u9fff]", result):
        return None
    # if result still has many raw english content words, accept mixed form
    return result


def pair_form(english: str, zh: str | None) -> str:
    if not zh:
        return english
    # Proper-noun identical gloss: still show Chinese marker only if different script
    if zh == english or norm(zh) == norm(english):
        # brand names: annotate as 专名 if pure latin and short
        if re.fullmatch(r"[A-Za-z0-9_.+/-]+", english) and len(english) <= 24:
            return f"{english}（{english}）" if False else english  # keep bare brand; refs may still translate
        return english
    if english.endswith(f"（{zh}）"):
        return english
    # collapse nested fullwidth parens duplication like AI（人工智能）（AI（人工智能））
    if f"（{zh}）" in english:
        return english
    return f"{english}（{zh}）"


ENTRY_RE = re.compile(r"^(\s*- \*\*)(.+?)(\*\*)(?:(：)(.*))?$")


def process(phrases):
    lines = INDEX.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("> **中文说明**"):
            out.append(
                "> **中文说明**：每条索引均为「**英文词条（中文）**」；"
                "位置名亦为「英文（中文）」——与原书术语一一对应，便于检索与阅读。"
            )
            continue
        if line.startswith("> **使用说明**"):
            out.append(
                "> **使用说明**：按字母顺序检索。词条与位置均中英对照；"
                "英文保留以对齐原书/代码，中文便于快速理解。"
            )
            continue
        if line.startswith("> 本页为原书"):
            out.append(
                "> 本页为原书书末索引（第 1806–1976 页）的逐条整理与中英对照："
                "每条索引按首字母分组，粗体为索引词条（附中文），其后为讨论位置（附中文）。"
            )
            continue
        if "索引词条与位置名保留英文原样" in line:
            continue  # drop old note, replaced above
        m = ENTRY_RE.match(line)
        if not m:
            out.append(line)
            continue
        indent, term, stars, colon, rest = m.groups()
        term_zh = translate_text(term, phrases)
        new_term = pair_form(term, term_zh)
        if not colon:
            out.append(f"{indent}{new_term}{stars}")
            continue
        refs = [r.strip() for r in (rest or "").split("；") if r.strip()]
        new_refs = []
        for r in refs:
            rz = translate_text(r, phrases)
            new_refs.append(pair_form(r, rz))
        out.append(f"{indent}{new_term}{stars}：{'；'.join(new_refs)}")

    text = "\n".join(out)
    if not text.endswith("\n"):
        text += "\n"
    # ensure group headers still bilingual
    text = re.sub(r"^## Symbols\s*$", "## Symbols（符号）", text, flags=re.M)
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        text = re.sub(rf"^## {ch}\s*$", rf"## {ch}（字母 {ch}）", text, flags=re.M)
    INDEX.write_text(text, encoding="utf-8")


def stats():
    lines = INDEX.read_text(encoding="utf-8").splitlines()
    entries = [L for L in lines if re.match(r"^\s*- \*\*", L)]
    with_cjk = sum(1 for L in entries if re.search(r"[\u4e00-\u9fff]", L))
    # term-level: has （ after **
    term_zh = 0
    for L in entries:
        m = re.match(r"^\s*- \*\*(.+?)\*\*", L)
        if m and re.search(r"[\u4e00-\u9fff]", m.group(1)):
            term_zh += 1
    print(f"entries={len(entries)} line_cjk={with_cjk} ({with_cjk/len(entries):.1%}) term_with_zh={term_zh} ({term_zh/len(entries):.1%})")
    print("samples:")
    for L in entries[:15]:
        print(" ", L[:170])
    no = [L for L in entries if not re.search(r"[\u4e00-\u9fff]", L)]
    print(f"\nstill no cjk: {len(no)}")
    for L in no[:20]:
        print(" ", L[:140])


def main():
    title_pairs = load_title_pairs()
    print("title pairs:", len(title_pairs))
    phrases = build_phrase_list(title_pairs)
    print("phrase entries:", len(phrases))
    process(phrases)
    stats()


if __name__ == "__main__":
    main()
