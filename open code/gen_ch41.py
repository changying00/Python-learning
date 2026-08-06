# -*- coding: utf-8 -*-
"""Generate chapters/ch41.md in FORMAT.md + ch01.md style from reflowed source text."""
from pathlib import Path

OUT = Path("chapters/ch41.md")

MD = r'''# 第 41 章：All Good Things（美好的终结）

> **原书**：《Learning Python》（6th Edition），作者 Mark Lutz
> **本章地位**：全书收官章——不再教新语法，而是回望 Python 的演化速度、工具箱膨胀与开源治理张力，并以一段轻松的结业证书脚本收尾。读完本章，你应能把“会写 Python”提升为“会判断版本与特性是否值得”。

---

## 41.1 开篇引言

### 英文原文

> Welcome to the end of the book! Now that you've made it this far, this chapter says a few words in closing about Python's evolution before turning you loose on the software field and then wraps up with a bit of fun.
>
> You've now had a chance to see the entire Python language yourself—including some advanced features that may seem at odds with a scripting language meant to be accessible to nonprofessionals. Though many users will understandably accept this as status quo, in an open source project, it's crucial that some ask the "why" questions too. Ultimately, the trajectory of the Python story—and its true conclusion—is at least in part up to you.
>
> Toward that end, this chapter begins by calling out what may be one of Python's biggest downsides: its rate of change. This topic is unavoidably subjective, and you should weigh its coverage here on whatever scale you bring to the table.

### 中文翻译

> 欢迎来到本书的结尾！既然你已经读到了这里，本章会先用几段话收束对 Python 演化的讨论，把你交还给软件开发领域，最后再用一点轻松的内容收尾。
>
> 你现在已经亲自接触过完整的 Python 语言——其中包括一些看起来似乎不太符合“应当让非专业人士也能使用的脚本语言”定位的高级特性。许多用户可以理解地把这些内容当作既成事实，但在开源项目中，必须有人继续追问“为什么”。最终，Python 故事的走向，以及它真正的结局，至少有一部分取决于你。
>
> 因此，本章先指出 Python 可能最大的缺点之一：变化速度太快。这个话题不可避免地带有主观性，你应当用自己的经验和标准来衡量下面的讨论。

### 深度理解

- **核心概念**：收官章把“会写 Python”提升为“能判断 Python 变化是否值得”。语言特性不是自动带来价值的清单，必须放在可读性、兼容性和维护成本中评估。
- **底层实现**：程序通常经解析、编译为字节码，再由实现（CPython、PyPy 等）执行；版本升级可能同时改变语法、标准库、字节码与运行时行为。“解释型”并不意味着升级没有运行时影响。
- **设计原因**：作者用收尾追问“为什么”，是因为开源语言会在长期演化中积累历史兼容与社区决策。理解设计背景，比机械记住某个新语法更能帮助工程师做版本选择。
- **实际问题**：维护项目时应记录支持的 Python 版本、锁定依赖、运行完整测试，并在升级前检查弃用警告与发布说明。
- **初学者误区**：不要把“最新”误认为“最好”，也不要把“旧代码能运行”误认为“永远不需要升级”。先掌握稳定核心，再按项目收益引入新特性。

---

## 41.2 The Python Tsunami（Python 海啸）

### 英文原文

> Twelve years ago, this book warned that Python was growing too convoluted and bloated—and then Python grew a lot more convoluted and bloated. Clearly, this message has not reached those behind the convoluting and bloating.
>
> Even so, this stuff still matters. To parrot the Preface, the last dozen years have hosted the rise of f-string literals, named-assignment expressions, match statements, type hinting, async coroutines, dictionary union, star-unpacking proliferation, underscore digit separators, module attribute hooks, exception groups, dictionary-key insertion order, positional-only function arguments, hash-based bytecode files, the sys.executable snub, and other superfluous additions, opinionated deprecations, and tangled mutations we've met along the way.
>
> Moreover, this tsunami of mods simply added to the flood of complexity and redundancy that came before it—including the oddly artificial MRO, the stunningly implicit super, and the horrifically convoluted inheritance algorithm of the preceding chapter, which elevates metaclasses and descriptors to prerequisites. The sum of these is an esoteric morass, which obfuscates the fundamental meaning of names in Python.
>
> Most of what should be said about these changes already has been said in this book, but their combined weight qualifies as problematic for a tool that promotes itself as simpler than others. To illustrate, Table 41-1 updates the prior edition's accounting of Python's largely unchecked growth so far—a partial but representative tally.

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
| 4 dictionary-merge options | `for` loops, `update` method, `**D` unpacking, `\|` union operator |
| 2 exception-handler models | `except` singles, `except*` groups |
| 4 statement-aping expressions | `if`/`else`, comprehensions, `lambda` functions, `:=` assignment |
| 8 starred collectors/unpackers | Assignment; function header, call; list, tuple, dict, set literal; `match` |

### 英文原文（续）

> If you care about Python, you should take a moment to browse this table. It reflects a virtual explosion of bifurcation, redundancy, and toolbox size—and 81 concepts that can all be required reading for both newcomers learning the language and experts reusing code written by others. Most of its categories began with just one original member in Python; many were added in part to imitate other languages; and none can be simplified today by pretending that the latest Python is the only Python that matters. Python 3.X now owns the flux in full.
>
> F-strings are a prime example in this category. This book's prior edition lamented the three redundant string-formatting tools of its time, but this set was subsequently expanded to a colossal four. While f-strings may be deemed a refinement by some, in truth they are a minor variation on a theme that adds yet another topic to the heap. More fundamentally, millions of programmers have written millions of programs using longer-lived options; while new code has the luxury of using new tools, pretending that the past didn't happen constitutes a break with reality.
>
> Even extensions perhaps more unique often come loaded with surplus complexity. The match statement, for example, couldn't simply provide a potentially useful multiple-choice option. It had to bolt on the conceptually tortuous and syntactically ad hoc structural pattern matching, which seems an answer to a question that nobody asked.
>
> Nor are additions the only user-unfriendly theme in Python. Its subjective changes and deprecations are now so common that they must be expected as an implicit cost of using the language. To be clear, your Python code will almost certainly break eventually when you upgrade to a new Python release—and only because a Python core developer's whim was made mandatory for everyone else.

### 中文翻译

> 十二年前，本书曾警告 Python 正变得过于纠缠、过于臃肿——然后 Python 又变得更加纠缠、更加臃肿。显然，这个消息并没有传到那些制造纠缠和臃肿的人那里。
>
> 即便如此，这些事情仍然重要。借用前言中的说法，过去十多年里出现了 f-string 字面量、命名赋值表达式、`match` 语句、类型提示（type hinting）、异步协程、字典并集、不断扩张的星号解包、下划线数字分隔符、模块属性钩子、异常组、字典键插入顺序、仅位置参数、基于哈希的字节码文件、对 `sys.executable` 的轻视，以及一路上遇到的其他多余添加、武断弃用和纠缠的变动。
>
> 更不用说，这场修改的“海啸”（tsunami）只是叠加到了更早以前已经存在的复杂性和冗余之上，其中包括人为感很强的 MRO、含义惊人地隐式的 `super`，以及上一章介绍的、极其纠缠的继承算法——后者甚至把元类（metaclass）和描述符（descriptor）提升成了先决知识。它们合在一起形成了一个深奥的泥潭，模糊了 Python 中名称的基本含义。
>
> 关于这些变化，大多数该说的话本书都已经说过了；但它们合在一起的重量，对于一个自称比其他工具更简单的工具而言，确实称得上是个问题。表 41-1 更新了上一版对 Python 至今几乎不受约束的增长所做的统计——这不是完整清单，但具有代表性。

**表 41-1　Python 中冗余与工具爆炸的抽样统计**（见上表，中英文对照）

> 如果你关心 Python，不妨花一点时间浏览这张表。它反映出分叉、冗余和工具箱规模的虚拟“爆炸”：多达 81 个概念可能同时成为学习语言的新手和复用他人代码的专家的必读内容。大多数类别在 Python 中最初只有一个成员；许多成员部分是为了模仿其他语言而加入的；如今也不能假装“只有最新版 Python 才重要”来简化问题。Python 3.X 已经完整地接管了这种流变。
>
> f-string 是其中一个典型例子。本书上一版曾批评当时已有的三种冗余字符串格式化工具，但后来又扩展成了庞大的四种。有人可以把 f-string 视为改进，但它本质上只是同一主题的轻微变体，又向知识堆里增加了一个主题。更根本的是，数百万程序员已经用寿命更长的旧选项写出了数百万个程序；新代码可以享受新工具，但假装过去从未发生过，就是脱离现实。
>
> 即使是更独特的扩展，也经常携带多余的复杂性。例如，`match` 语句本可以只提供一个有用的多路选择工具，却还要附加概念上曲折、语法上临时拼接的结构化模式匹配，看起来像是在回答一个没人提出的问题。
>
> 添加新特性也不是 Python 唯一不友好的主题。它的主观变化和弃用现在如此频繁，以至于使用这门语言就必须默认承担这种隐性成本。明确地说，当你升级到新的 Python 发行版时，代码几乎肯定最终会因为某个 Python 核心开发者的偏好被强制化而出现问题。

### 深度理解

- **核心概念**：批评的是“工具箱膨胀”和语义分叉，而不只是某一个语法。一个任务有多种等价写法，会增加阅读者必须掌握的上下文数量；表中的 81 个概念说明兼容性本身已经成为 Python 能力的一部分。
- **底层实现**：版本变化可能影响解析器、AST、编译出的字节码、导入系统和运行时对象协议。`match`、`except*` 等新语法使旧解释器无法解析，不能靠运行时兼容弥补。
- **设计原因**：新特性通常试图解决真实需求或吸收其他语言实践，但“能加入”不等于“应该加入”。保留旧工具是兼容性承诺，新增工具会扩大文档、培训、测试和维护的长期面积。
- **实际问题**：工程团队应在公共代码风格中选定一种格式化、导入、异常处理和数据合并方式；升级时用 CI 矩阵验证目标版本，并把 `DeprecationWarning` 当成待办。
- **初学者误区**：不要为了显得现代而把所有新语法塞进代码，也不要因为作者批评某特性就拒绝理解它。应知道特性的语义、适用版本和迁移成本，再按项目支持范围选择。

---

## 41.3 The Python Sandbox（Python 沙盒）

### 英文原文

> All of this stems from the fact that Python is, and probably always has been, a constantly morphing sandbox of ideas, which prioritizes its developers' egos over its users' needs. Playing in a sandbox can be fun, of course, but it's lousy for the millions of people downstream from its churn. These people are simply trying to write software that's reliable and durable. Like all engineering endeavors, that works best with a stable base, not constantly shifting sand.
>
> As a pathological example, Python's sandbox model seems to have hit its zenith in type hinting—the optional, unused, out-of-place, and embarrassingly academic subdomain we glanced in Chapter 6 but largely omitted here by design. This is unchecked convolution on parade, and leaves Python users to puzzle over the paradox of pointless type declarations in a dynamically typed language. Sadly, it's also likely to appeal to control freaks.
>
> As we've also seen regularly in this book, because the sandbox is oriented toward experts, it inevitably produces tools that assume that you have to already be an expert to use them. Classes and OOP, for example, are required skills for even simple exception handling. Python is not just for its developers, but the forward knowledge assumptions of many of its additions embed this message and raise the bar for newcomers unnecessarily and unkindly.
>
> To be fair, it's not just Python: the entire software field is permeated by a culture of change in which churn is an expected constant, and prowess often consists of flaunting the latest and greatest tools even when they are unwarranted. This doesn't prove intelligence (and often demos its absence), but annual and mandatory mods are now a norm. Whether one breaks your PC, smartphone, or Python code, it's difficult not to see this as divisive and rude.

### 中文翻译

> 这一切源于一个事实：Python 是，而且很可能一直都是，一个不断变形的思想“沙盒”（sandbox），它把开发者的自我满足置于用户需求之上。在沙盒里玩当然可能很有趣，但对于下游数百万只想写出可靠、持久软件的人来说，这种不断变化的状态非常糟糕。像所有工程工作一样，软件在稳定的基础（stable base）上运行得最好，而不是建在不断移动的沙地上。
>
> 一个极端例子是，Python 的沙盒模式似乎在类型提示（type hinting）上达到了顶峰——那是一个可选、通常不改变运行时、位置尴尬而且带有学术色彩的子领域；我们在第 6 章略有提及，但本书有意基本省略了它。这是未经约束的复杂化示范，让 Python 用户困惑于一个悖论：动态类型语言中，为什么要声明一些没有运行时用途的类型？它还很可能吸引喜欢绝对控制的人。
>
> 正如本书经常展示的那样，因为这个沙盒面向专家，它不可避免地制造出一些假设使用者已经是专家的工具。比如，即使是简单的异常处理，也被要求掌握类和 OOP。Python 不只是为它的开发者服务；许多新增内容对“前置知识”（forward knowledge）的预设也在传递同一个信息，并且不必要、不友好地抬高了新手的门槛。
>
> 公平地说，这不只是 Python 的问题：整个软件行业都浸泡在一种“变化文化”（culture of change）里，持续变化被视为常态，能力常常被表现为炫耀最新、最强的工具，即使那些工具并不必要。这不代表聪明，很多时候反而暴露了缺乏判断；但每年一次、强制性的修改如今已成为规范。无论它破坏的是电脑、手机还是 Python 代码，都很难不觉得这种做法具有分裂性，也不够尊重用户。

### 深度理解

- **核心概念**：沙盒比喻强调“语言可以实验”与“用户需要稳定”之间的张力。试验新工具的成本，往往由下游应用、培训材料和长期维护者承担。
- **底层实现**：类型注解在常规执行中主要保存在 `__annotations__` 中，由解释器与第三方工具按约定读取；静态检查器、运行时校验器和框架会赋予它不同语义。类型提示不会自动把动态类型 Python 变成静态类型语言。
- **设计原因**：专家工具可以扩展表达能力，但如果新特性依赖元类、描述符或复杂导入规则，就会把前置知识链条继续拉长。
- **实际问题**：生产项目应区分“运行时必需”的约束和“工具链可选”的检查；升级前要在隔离环境中验证编辑器、类型检查器、测试框架和部署镜像。
- **初学者误区**：类型提示是工具，不是运行时真相；不要把公共 API 设计成难以阅读的类型谜题。先建立清晰的运行时行为，再决定是否增加静态约束。

---

## 41.4 The Python Upside（Python 的优势）

### 英文原文

> All that being said, it's also difficult to deny that Python, despite its warts, is still more productive and pleasant to use than other programming languages. If you've coded other languages, you know that many come laden with extraneous syntax and rules, which seem to reflect an assumption that programmers cannot be trusted to do their jobs. By sharp contrast, Python's dynamic typing and innate flexibility make it more ally than obstacle.
>
> Python's rise in popularity seems to attest to this value proposition, though its impetus may be more practical than academic. Today's larger Python world may naturally be less concerned with the language's original and perhaps idealistic goals than with solving concrete problems. In the real world that hosts Python popularity, arcane language topics usually take a back seat to libraries, platforms, and schedules—calls that Python has always answered in full.
>
> Moreover, some change and complexity is warranted in software. Programming is a substantially challenging task (despite what you may have heard), and computer science is a field still young enough to be excused for some youthful thrashing. For Python specifically, though, complexity and thrashing should be modulated by broad appeal.
>
> In the end, the Python language remains a remarkably expressive tool that still fits both programming tasks and your brain as well as it ever did. Especially if you stick to its tried-and-true parts that propelled Python to the top of the language charts, you'll likely find it an enabling technology that makes coding as much fun as chore.
>
> Prudent engineers, though, would do well to exercise caution when upgrading to the leading edge, and give a pass to the sandbox's annual outflow except when clearly beneficial. Given that this is now an industry-wide requirement, it's hardly cause to dismiss an otherwise useful tool. Bad practice, however, does not justify bad practice.

### 中文翻译

> 话虽如此，也很难否认：尽管 Python 有各种缺点，它仍然比其他编程语言更高效、更令人愉快。如果你写过其他语言，就知道其中许多语言带着额外的语法和规则，仿佛默认程序员不值得信任。相比之下，Python 的动态类型和天生的灵活性更像盟友，而不是障碍。
>
> Python 受欢迎程度（popularity）的上升似乎证明了这一价值主张，不过它的推动力可能更多来自实践而非学术。如今更庞大的 Python 世界自然可能不太关心语言最初、也许更理想主义的目标，而更关心解决具体问题。在 Python 流行的现实世界里，晦涩的语言议题通常让位于库、平台和进度安排——而这些正是 Python 一直都能很好回应的需求。
>
> 此外，软件中的某些变化和复杂性是合理（warranted）的。编程本来就是一项相当有挑战的工作，计算机科学也还年轻到可以被原谅一些成长时期的摇摆。但对于 Python，复杂性和摇摆仍应受到“面向广泛用户”的目标调节。
>
> 归根结底，Python 仍是一种极具表达力的工具，仍然像过去一样同时贴合编程任务和人的思维。尤其是当你坚持使用那些可靠、成熟、曾把 Python 推到语言排行榜前列的部分时，你很可能会发现它是一种让编程更像乐趣而不是苦差事的赋能技术。
>
> 但谨慎的工程师在升级到最前沿版本时应保持警惕，除非新变化明确有益，否则可以跳过沙盒每年的产出。既然这已经成为整个行业的要求，它还不足以成为放弃这个有用工具的理由；不过，坏的实践不会因为行业普遍存在就变成好的实践。

### 深度理解

- **核心概念**：Python 的优势是开发者生产力和表达力，而不是“所有场景下运行最快”。承认复杂性成本，同时继续使用最成熟、最能减少样板代码的部分。
- **底层实现**：动态类型让名称在运行时绑定对象，缩短开发反馈回路，也把一部分错误推迟到测试或执行路径；跨平台能力依赖解释器、标准库和操作系统适配层。
- **设计原因**：复杂度并非绝对坏事，关键是收益是否覆盖学习、兼容和维护成本。核心价值来自少量一致的机制。
- **实际问题**：版本选择应结合依赖支持、部署平台、性能需求和团队熟悉度；长期维护项目先在兼容矩阵和预发布环境中验证。
- **初学者误区**：不要把“易学”理解为“只有简单功能”，也不要把“灵活”理解为可以随意牺牲可读性。

---

## 41.5 Closing Thoughts（收束思考）

### 英文原文

> So there you have it: some observations from the trenches, born of three decades using, teaching, and advocating Python, and grounded in a desire to improve the Python story.
>
> None of these concerns are entirely new. Indeed, the growth of this very book over the years seems a testament to that of Python itself—if not an ironic eulogy to a mission statement that once stressed simplification of programming, and accessibility to both experts and nonprofessionals alike. Judging by language heft alone, that dream seems to have been either neglected over time or abandoned entirely.
>
> But we can do better. A well-established tool like Python can afford to focus more on its users' needs than its changers' hubris. Per the old adage, we simply have to stop fixing what isn't broken. If we can, it will go far toward addressing the concerns of those vetting the language for projects that cannot afford to budget for shifting sands.
>
> More importantly, in an open source project like Python the answers to such questions must be formed anew by each wave of newcomers. Hopefully, the wave you ride in will have as much common sense as fun while plotting Python's future.

### 中文翻译

> 以上就是全部内容：这是一些来自一线的观察，源自三十年使用、教授和倡导 Python 的经历，也源于改进 Python 故事的愿望。
>
> 这些担忧并不完全是新问题。事实上，这本书多年来的增长似乎正是 Python 自身增长的见证——如果不是对那个曾经强调简化编程、让专家和非专业人士都能接触编程的使命宣言所作的讽刺性悼词的话。单从语言的重量来看，那个梦想似乎随着时间被忽视了，甚至被放弃了。
>
> 但我们可以做得更好。像 Python 这样已经建立起来的工具，完全可以把用户需求置于变更者的自负之上。按照那句老话，我们只需要停止修理没有坏掉的东西。如果做到这一点，就能大幅回应那些正在为无法承受持续变化成本的项目评估语言的人所提出的担忧。
>
> 更重要的是，在 Python 这样的开源项目中，这些问题的答案必须由一批又一批的新来者重新形成。希望你所乘的那一波浪潮，在规划 Python 未来时既有乐趣，也有足够的常识。

### 深度理解

- **核心概念**：把语言演化重新放回开源治理和用户责任中。Python 的未来不只取决于核心开发者，也取决于使用者是否提出稳定性、可读性和长期维护的要求。
- **底层实现**：兼容性由解释器、标准库、第三方包、构建工具、操作系统和部署镜像共同决定；任何一层升级都可能改变最终行为。
- **设计原因**：“不要修理没坏的东西”并非反对所有进步，而是要求变化有明确收益、迁移路径和回滚方案。
- **实际问题**：用支持策略、版本锁定、变更记录、回归测试和灰度发布把个人偏好转化为可审计决策。
- **初学者误区**：不要把作者批评当成 Python 官方结论；应区分原文立场、语言事实和自己的工程取舍。

---

## 41.6 Where to Go from Here（接下来去哪里）

### 英文原文

> And that's a wrap, folks. You've officially reached the end of this book. Now that you know Python inside and out, your next step, should you choose to take it, is to explore the libraries, techniques, and tools available in the application domains in which you will work.
>
> Because Python is so widely used, you'll find ample resources for using it in almost any domain you can think of—from GUIs, the web, and apps, to numeric programming, databases, and system administration. See Chapter 1 and your favorite web browser for pointers to popular tools and topics.
>
> This is where Python starts to become truly fun, but this is also where this book's story ends, and those of other resources begin. Good luck with your journey. And as always: code well!

### 中文翻译

> 好了，各位，这就是收尾。你已经正式读完本书。现在你已经从里到外了解了 Python，下一步（如果你愿意）就是探索你将工作的应用领域中可用的库、技术和工具。
>
> Python 被广泛使用，因此几乎任何你能想到的领域都有足够的资源——从 GUI、Web 和应用程序，到数值编程、数据库和系统管理。可以回看第 1 章，也可以使用你喜欢的浏览器查找热门工具和主题。
>
> Python 真正开始变得有趣的地方就在这里；但这也是本书故事结束、其他资源故事开始的地方。祝你的旅程顺利。也一如既往：写出好的代码！

### 深度理解

- **核心概念**：基础语言学习的终点是应用领域的起点。Python 的实际价值通常来自标准库和第三方生态。
- **底层实现**：GUI、Web、数值计算和系统工具会分别接触事件循环、网络协议、原生扩展、进程与文件系统等运行时边界。
- **设计原因**：统一的对象、模块和调用模型让学习成本可以跨库迁移。
- **实际问题**：进入新领域时先确认 Python 版本、平台、依赖许可证、性能约束和部署方式，再建立最小可运行样例。
- **初学者误区**：读完语言书不等于掌握某个领域；不要把库示例当作生产架构。

---

## 41.7 Encore: Print Your Own Completion Certificate!（加餐：打印自己的完成证书）

### 英文原文

> And one last thing: in lieu of exercises for this part of the book, Example 41-1 lists a bonus script for you to study and run on your own. A book can't directly provide completion certificates for its readers (and the certificates would be worthless if it could), but it can include an arguably cheesy Python script that does. This one creates a simple book completion certificate in both plain-text and HTML files, and auto-opens them in a web browser or other viewer where supported.

**Example 41-1. You-made-it.py**

### 中文翻译

> 最后还有一件事：本书这一部分不再安排练习，例 41-1 提供了一个可以自行研究和运行的加餐脚本。书本不能直接给读者发放完成证书（如果可以，证书也会失去价值），但可以提供一个虽然有点俗气、确实能生成证书的 Python 脚本。这个脚本会同时创建纯文本和 HTML 格式的简单读书完成证书，并在支持的环境中自动用浏览器或其他查看器打开它们。

### 代码分析

```python
"""
生成一个简单的课程完成证书：打印到控制台，
并保存到自动打开的文本和 HTML 文件中。
从控制台运行；如有需要可打印保存的输出文件。
适用于所有 PC，但在手机上可能需要手动打开文件。
"""
import time, sys, html, os

maxline = 60                 # 文本分隔线长度
browser = True               # 是否在浏览器中显示
saveto = 'Certificate'       # 输出文件名前缀

# 模板值
SEPT = '*' * maxline
DATE = time.strftime('%A, %b %d, %Y, %I:%M %p')
NAME = input('Please enter your name: ').strip() or 'An unknown reader'
BOOK = 'Learning Python, 6th Edition'
SITE = 'https://learning-python.com'  # 图标、图片和链接

# f-string 模板可读取代码中预先设置的引用
texttext = f"""
{SEPT}

 Official Certificate 

Date: {DATE}
This certifies that:
\t{NAME}
Has survived the massive tome:
\t{BOOK}
And is now entitled to all privileges thereof, including
the right to proceed on to learning how to develop websites,
desktop GUIs, scientific models, smartphone apps, and 
anything else that the future of computing may hold. 
--Your humble instructor
(Note: void where obtained by skipping ahead.)
{SEPT}
"""

# 交互与动画
for c in 'Congratulations!'.upper() + '\n' * 3:
    print(c, end=' ')
    sys.stdout.flush()       # 某些 shell 会等待换行
    time.sleep(0.25)         # 让消息逐字显示
print()
time.sleep(3)

# 创建文本文件
textto = saveto + '.txt'
fileto = open(textto, 'w', encoding='utf8')
print(texttext, file=fileto)
fileto.close()

# 创建 HTML：把文本标记替换为标签
htmltext = texttext.replace(SEPT, '<div class=cert>', 1)
htmltext = htmltext.replace(SEPT, '</div>')
htmltext = htmltext.replace('\n\n', '<h1 align=center>\n\n&nbsp;', 1)
htmltext = htmltext.replace(' \n\n', '&nbsp;\n\n</h1>')

# 逐行调整
linemods = []
for line in htmltext.split('\n'):
    if line == '':
        line = '<p>'
    elif line[:1] == '\t':
        line = f"<i>{'&nbsp;' * 4}{html.escape(line[1:])}</i>"  # 3.6+
    linemods.append(line)
htmltext = '\n'.join(linemods)

# HTML 外壳；f-string 中的花括号需要转义
preamble = f'''<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/x-icon" href="{SITE}/favicon.ico">
<style>
body {{font-family: Arial, Helvetica, sans-serif;}}
.cert {{background-color: cornsilk; padding: 16px; border: medium solid black;}}
</style>
<title>LP6E Completion Certificate</title>
</head>
'''
image, page = 'lp6e-large.jpg', 'about-lp.html'
footer = f'''
<table><tr>
<td><a href="{SITE}/{page}"><img src="{SITE}/{image}" hspace=10 height=50></a>
<td><a href="{SITE}/{page}" align=center><i>Book support site</i></a>
</tr></table>
'''

# 合并 HTML
htmltext = f'{preamble}<body bgcolor="#eee">{htmltext}{footer}</body></html>'
htmlto = saveto + '.html'
fileto = open(htmlto, 'w', encoding='utf8')
print(htmltext, file=fileto)
fileto.close()

# 在控制台显示文本结果
print(f'[File: {textto}]', end='')
print('\n' * 2, open(textto, encoding='utf8').read())

# 尝试打开文档
if browser:
    try:
        import webbrowser
        for doc in (textto, htmlto):
            webbrowser.open('file://' + os.path.abspath(doc))
    except Exception:
        print('Unable to auto-open docs: open manually.')
input('[Press Enter to close]')  # 点击运行时保持窗口
```

### 英文原文（运行说明）

> Run this script in a console or other interface on your own, and study its code for a review of some of the ideas we've covered in this book. Copy/paste from emedia or fetch it from this book's examples package as described in the Preface, but ignore its undocumented and out-of-scope HTML bits if you're not a web developer. You won't find any descriptors, decorators, metaclasses, or super calls in this code, but it's typical Python nonetheless:
>
> `$ python3 You-made-it.py`
>
> Please enter your name: Some Body
>
> C O N G R A T U L A T I O N S !
>
> …
>
> This script works in full on PCs (where code might also open files with `os.startfile`, or "open" or "xdg-open" commands in `os.system`), but on smartphones you'll probably need to open the output files manually in file-explorer apps. When run, it generates the web page captured in the fully gratuitous Figure 41-1. This could be much more grandiose, of course; see the web for pointers to Python support for PDFs and other document tools such as Sphinx surveyed in Chapter 15. But hey—if you've made it to the end of this book, you deserve another joke or two.
>
> *Figure 41-1. HTML doc created and opened by You-made-it.py*

### 中文翻译（运行说明）

> 请在控制台或其他界面自行运行这个脚本，并研读其代码，以回顾本书涵盖的一些思想。可从电子版复制粘贴，或按前言所述从本书示例包获取；若你不是 Web 开发者，可忽略其中未文档化、超出本书范围的 HTML 细节。这段代码里找不到描述符、装饰器、元类或 `super` 调用，但它仍然是典型的 Python：
>
> `$ python3 You-made-it.py`
>
> 请输入你的名字：Some Body
>
> C O N G R A T U L A T I O N S !
>
> …
>
> 该脚本在 PC 上可完整工作（也可用 `os.startfile`，或在 `os.system` 中调用 `open` / `xdg-open` 打开文件）；在手机上则很可能需要用文件管理器手动打开输出。运行后会生成图 41-1 所示的网页。当然还可以做得更华丽；可在网上查找 Python 对 PDF 等文档工具的支持，以及第 15 章介绍的 Sphinx。不过——如果你已经读到本书末尾，你值得再听一两个玩笑。
>
> *图 41-1. 由 You-made-it.py 创建并打开的 HTML 文档*

### 深度理解

- **核心概念**：证书脚本把“从语言走向工程”落到完整小程序：读输入、格式化、写文件、生成 HTML、调用平台能力、处理异常。
- **底层实现**：f-string 运行时求值生成 `str`；`open(..., encoding='utf8')` 保证文本编码不依赖平台默认；`webbrowser` 依赖 OS 默认应用关联。生产代码更宜用 `with open(...)`。
- **设计原因**：先建 `texttext` 再替换为 HTML，避免维护两份证书内容——数据与表现分离的简单示范。
- **实际问题**：用 `pathlib.Path` 管理路径；处理权限、编码、覆盖和平台差异；对用户姓名做 HTML 转义防注入。
- **初学者误区**：`html.escape` 只处理被调用的字符串；`time.sleep()` 会阻塞线程，只适合演示。

- 解释器先导入模块并创建配置；`'*' * maxline` 产生固定长度分隔线。
- `input().strip() or 默认` 处理空输入。
- 字符串替换 + `html.escape` 是教学级 HTML 生成；生产应优先模板库。
- `webbrowser.open` 的异常捕获保证自动打开失败时脚本不崩，但不保证所有系统都有浏览器。

---

# 本章总结

本章主线不是再增加语法清单，而是学习如何面对一门持续演化的语言：作者批评特性与弃用膨胀，同时承认 Python 仍凭借动态类型、表达力与生态提高生产力；加餐脚本则把“语言→工程”落到可运行示例。

## 技术拓展（Technical Expansion）

- **实际项目中的应用场景**：制定 Python 支持范围；用 venv 与锁定文件管理依赖；CI 矩阵验证多平台与多版本；把 `DeprecationWarning` 纳入升级计划。
- **与其他语言的区别**：

| 维度 | Python | Java | C++ |
|---|---|---|---|
| 类型与反馈 | 动态类型，运行时反馈快 | 静态类型，编译期约束强 | 静态类型，资源控制强 |
| 运行环境 | 解释器/实现与标准库 | JVM | 原生编译产物 |
| 典型优势 | 开发速度、胶水、生态 | 大型服务、跨平台运行时 | 性能、确定性、底层控制 |
| 主要工程成本 | 运行时错误、版本与依赖 | 构建与样板代码 | 编译复杂度、内存/ABI |

- **Python 发展历史背景**：本章强调长期演化与版本兼容压力；具体日期与 PEP 以官方发布记录为准。
- **高级开发者需要掌握**：导入系统、`sys.modules`、虚拟环境与打包、语义版本与弃用策略、CI/回归测试、PEP 流程。

## 学习建议（Learning Advice）

- **重要程度（4/5）**：收束章代码量不大，却直接影响版本选择、升级策略与工程判断。
- **应该掌握到什么程度**：能解释语言变化带来的兼容与维护成本；能区分解释器、模块、包、IDE、venv 与打包器；能在目标平台安装并运行示例。
- **后续应该学习哪些相关内容**：选一个应用领域读其生态文档；实践 venv、依赖锁定、CI、多平台测试与发布；再深入类型检查、异步、性能工具或原生扩展。

---

*本章完。全书正文至此结束；附录见 Appendix A / B。*
'''

OUT.write_text(MD, encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes, {MD.count(chr(10))+1} lines)")
