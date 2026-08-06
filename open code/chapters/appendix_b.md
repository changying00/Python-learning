# 附录 B：Solutions to End-of-Part Exercises（各部分练习解答）

> **原书**：《Learning Python》（6th Edition），作者 Mark Lutz
> **本附录地位**：全书"官方答案手册"——收录 Part I 到 Part VII 各部分章末练习（Test Your Knowledge: Part Exercises）的参考解答。它不教新语法，而是把前面七大部分学过的所有知识点（对象类型、语句、函数、模块、类、异常）串成可运行的代码，演示"标准用法 + 常见坑"，并配大量真实文件（module1.py、adder2.py、primes.py、mylist.py、zoo.py、exctools.py 等）。
> **重要说明**：解答中由标题或叙述引用的代码文件，均位于书籍示例包（examples package）的 `AppendixB` 文件夹中，该文件夹为每个部分各设一个子文件夹（例如 `AppendixB/Part1` 存放第一部分的文件）。关于示例包的更多信息，请参阅《前言》（Preface）。

---

## 引言（Introduction）

### 英文原文

> This appendix provides solutions for the book's end-of-part exercises. Code files named by captions or narrative in these solutions are available in the book examples package's `AppendixB` folder, which has one subfolder per part (e.g., `AppendixB/Part1` is the first part's files). See the `Preface` for more info on the examples package.

### 中文翻译

> 本附录为全书各部分章末练习提供官方解答。解答中由标题（captions）或叙述（narrative）所引用的代码文件，都存放在本书示例包（examples package）的 `AppendixB` 文件夹中，该文件夹为每个部分各设一个子文件夹（例如 `AppendixB/Part1` 就是第一部分的文件）。关于示例包的更多信息，请参阅《前言》。

### 深度理解

- **核心概念**：附录 B 是"练习答案库"，但作者的设计意图是**先做题、后对照**。每题答案都展示了"官方推荐的解题思路"，而非唯一答案。
- **代码文件与书页的对应**：正文中的 `Example B-N`（示例 B-数字）编号对应本附录，文件路径如 `Part4/adder2.py` 指示例包内 `AppendixB/Part4/adder2.py`。
- **学习建议**：逐题对照时，重点关注三件事——① 为什么这么写；② 输出结果的底层原因；③ 自己写法的差异点在哪。

---

# Part I：Getting Started（入门）

### 英文原文

> Part I, Getting Started
> See "Test Your Knowledge: Part I Exercises" in Chapter 3 for the exercises.

### 中文翻译

> 第一部分：入门。练习见第 3 章的 "Test Your Knowledge: Part I Exercises"（第 I 部分练习测验）。

### 深度理解

- **核心概念**：Part I 的练习全部围绕"怎么让 Python 跑起来"——交互式解释器、脚本文件、模块导入、shebang 启动、错误消息、循环引用对象。
- **底层视角**：这部分在帮你建立两个心智模型：① **REPL（交互模式）与 .py 文件的差异**；② **模块执行与字节码缓存（.pyc）的关系**。
- **常见误区**：初学者常以为 `import` 是"复制粘贴代码"，其实它是"执行一次模块文件"，所以重复 import 不会重复执行，除非显式 `reload`。

---

## 题 1. Interaction（交互式会话）

### 英文原文

> **1. Interaction**: Assuming Python is configured properly, the interaction should look something like the following. You can run this any way you like—in IDLE, a console, an app, a notebook's page, and so on:

```
$ python3
…information lines…
>>> 'Hello World!'
'Hello World!'
>>> # Use ctrl+D/ctrl+Z to exit on Unix/Windows, or close window
```

### 中文翻译

> **1. 交互式会话**：假设 Python 已正确配置，交互过程看起来应大致如下。你可以用任何喜欢的方式运行它——在 IDLE、控制台、某个应用（app）、notebook 页面等等：

```
$ python3
……信息行……
>>> 'Hello World!'
'Hello World!'
>>> # 在 Unix/Windows 上用 ctrl+D/ctrl+Z 退出，或直接关闭窗口
```

### 代码分析

```text
$ python3           # 启动交互式解释器（REPL：读取-求值-打印循环）
>>> 'Hello World!'  # 输入一个字符串字面量表达式
'Hello World!'      # 解释器求值并回显（echo）结果——带引号是对象的 repr 形式
>>>                 # 按 ctrl+D(Unix)/ctrl+Z(Windows) 退出，或关闭窗口
```

### 深度理解

- **核心概念**：REPL 是 Python 的"活体实验台"。每个输入表达式都会经过**编译为字节码 → 解释求值 → 打印结果**三步。
- **底层机制**：交互模式下解释器会对每个完整表达式自动调用 `repr()` 打印结果（字符串带引号、列表带方括号）；而脚本文件里不会自动回显——这正是"交互"与"脚本"最重要的差别，后面 Part IV 练习 2 还会专门强调。
- **为什么这样设计**：让新手零成本感受"无编译步骤"的开发速度，写完即运行。
- **常见误区**：把 REPL 里能自动看到结果，误以为在文件里写 `x + 1` 也会输出——不会，必须 `print`。

---

## 题 2. Programs（程序）

### 英文原文

> **2. Programs**: Your code (i.e., module) file should look something like Example B-1:
>
> **Example B-1.** `Part1/module1.py`
> ```python
> print('Hello module world!')
> ```
>
> And here is the sort of interaction you should have; for console launches, be sure to use your platform's version of the "python3" command (e.g., try "py -3" on Windows):
>
> ```
> $ python3 module1.py
> Hello module world!
> ```
>
> Again, feel free to run this other ways—by clicking or tapping the file's icon, by using IDLE's **Run**→**Run Module** menu option, by UI options in web notebooks or other IDEs, and so on.

### 中文翻译

> **2. 程序**：你的代码（也就是模块）文件应该像示例 B-1 这样：
>
> ```python
> print('Hello module world!')
> ```
>
> 你应该得到的交互输出如下；从控制台启动时，务必使用你平台对应的 "python3" 命令（例如 Windows 上尝试 "py -3"）：
>
> ```
> $ python3 module1.py
> Hello module world!
> ```
>
> 同样，你也可以用其他方式运行它——点击/轻点文件图标、使用 IDLE 的 **Run**→**Run Module** 菜单选项、web notebook 或其他 IDE 的 UI 选项等等。

### 代码分析

```python
print('Hello module world!')    # 唯一一条语句：调用内置函数 print，向标准输出打印字符串
```

### 深度理解

- **核心概念**：一个 `.py` 文本文件就是一个模块（module），也就是一个程序。文件被读入内存、编译成字节码、交给解释器虚拟机执行。
- **底层机制**：`python3 module1.py` 底层就是"把该文件当作名为 `__main__` 的模块导入执行"——所以文件里的 `print` 语句会在执行到的那一瞬间输出。
- **多种运行入口的等价性**：IDLE 的 Run→Run Module 本质是"在解释器进程内 import 该文件"；双击图标则是让操作系统关联程序打开它。
- **常见误区**：Windows 上 `python3` 命令可能不存在，需用 `py -3`；文件路径含空格（如 `My Documents`）时命令必须加引号。

---

## 题 3. Modules（模块）

### 英文原文

> **3. Modules**: The following interaction listing illustrates running a module file by importing it:
>
> ```
> $ python3
> >>> import module1
> Hello module world!
> ```
>
> Remember that you will need to **reload** the module to run it again without stopping and restarting the interactive interpreter (i.e., REPL).
>
> Moving the `.py` file to a different directory and importing it normally fails: Python likely generated a `module1.*.pyc` file in the `__pycache__` subdirectory of the source code file's folder, but it won't use it when you import the module there if the source code (`.py`) file has been moved elsewhere and to a folder not in Python's import search path.
>
> The `.pyc` file is written automatically if Python has access to the source file's directory; it contains the compiled bytecode version of a module. See Chapter 3 for more on modules, Chapter 2 for more on bytecode, and Chapter 22 ahead for more on both.
>
> To really use the saved `.pyc` sans `.py`, as of Python 3.2, you must move it up one level and rename it without the "*" part in the middle, or generate it from and alongside the source code file with the Python `compileall` module's "legacy" (`-b`) mode. For example, the following compiles all source code files in the current directory into directly usable bytecode files (you can also list specific files or recurse into subfolders, per Python library docs):
>
> ```
> $ python3 -m compileall -b -l .
> ```

### 中文翻译

> **3. 模块**：下面的交互式列表演示如何通过导入（import）来运行一个模块文件：
>
> ```
> $ python3
> >>> import module1
> Hello module world!
> ```
>
> 记住：要想在不停止、不重启交互式解释器（即 REPL）的情况下再次运行模块，你需要 **reload**（重新加载）它。把 `.py` 文件移动到另一个目录后再正常导入会失败：Python 很可能已经在源文件所在文件夹的 `__pycache__` 子目录里生成了 `module1.*.pyc` 文件，但如果源文件（`.py`）已被移到别处、且不在 Python 的导入搜索路径（import search path）中，它就不会使用这份缓存。只要 Python 对源文件所在目录有写权限，`.pyc` 文件就会被自动写出；它包含模块编译后的字节码版本。关于模块参见第 3 章，关于字节码参见第 2 章，关于两者的更多内容参见后面的第 22 章。如果想真正在缺少 `.py` 的情况下使用保存的 `.pyc`，从 Python 3.2 起你必须把它向上移一级、去掉中间带 `*` 的部分改名，或者用 Python `compileall` 模块的"旧式"（`-b`）模式，从源文件生成并与之并存的字节码文件。例如，下面的命令把当前目录中的所有源代码文件编译成可直接使用的字节码文件（按 Python 库文档，你还可以列出具体文件或递归进入子文件夹）：
>
> ```
> $ python3 -m compileall -b -l .
> ```

### 代码分析

```python
import module1        # 导入模块：解释器查找 module1.py，编译并执行它
# 输出：Hello module world!
```

`python3 -m compileall -b -l .` 的含义：
- `-m compileall`：以"模块方式"运行内置的批量字节码编译器；
- `-b`（legacy 旧式）：把 `.pyc` 放在源文件旁边、且文件名不含版本号中间段（供 Python 3.2 及更早的"旁边式"读取）；
- `-l`：不递归子目录，只处理当前目录；
- `.`：当前目录（也可列出具体文件路径）。

### 深度理解

- **核心概念**：import 一个模块会**执行整份文件**，但只会执行一次——模块对象会被缓存进 `sys.modules`，第二次 import 直接返回缓存。
- **字节码与 .pyc 的关系**：Python 源码先被编译成字节码（bytecode）再执行；`.pyc` 就是字节码的磁盘缓存。若 `.py` 的时间戳/校验和未变，则跳过编译直接加载 `.pyc`，启动更快。
- **为什么移动 .py 后 import 失败**：import 靠**搜索路径**（`sys.path`：当前目录、PYTHONPATH、标准库目录等）找模块，`.pyc` 不会自动跟着源文件"搬家"。
- **设计思想**：`.pyc` 是"以空间换时间"的产物；`__pycache__` 子目录是为了让多个 Python 版本、多种解释器（CPython/PyPy）的缓存文件共存互不干扰。
- **常见误区**：手动删除 `.pyc` 不会让程序坏掉（最多重新编译）；在只读目录里运行不会生成 `.pyc`，这很正常，不是错误。

---

## 题 4. Scripts（脚本）

### 英文原文

> **4. Scripts**: Assuming your platform supports the `#!` trick, your solution will look like Example B-2, although your `#!` line may need to list a different path to Python on your machine.
>
> This line is significant under the Windows launcher shipped and installed with Python, where it is parsed to select a version of Python to run the script, despite the Unix path syntax, and subject to a default setting; see Appendix A and Python's docs for more details. This launching scheme is optional and generally less portable than others. **Example B-2.** `Part1/script1.py`

> ```python
> #!/usr/local/bin/python3
> print('Hello module world!')
> ```
> Running this as a program by console command line:

> ```
> $ chmod +x script1.py                              # See also: #!/usr/bin/env python3
> $ ./script1.py                                     # "./" needed only if "." not on PATH
> Hello module world!

> $ python3 script1.py                               # Or run normally and portably
> Hello module world!

> ```

### 中文翻译

> **4. 脚本**：假设你的平台支持 `#!`（shebang）技巧，你的解决方案应该像示例 B-2 那样，不过你的 `#!` 行可能需要填写你机器上不同的 Python 路径。这一行在随 Python 安装的 Windows 启动器（launcher）下意义重大：尽管它写的是 Unix 路径语法，启动器会解析它来选择运行该脚本的 Python 版本，并且受默认设置约束；更多细节参见附录 A 和 Python 文档。这种启动方案是可选的，而且通常比别的方案可移植性差。
>
> ```python
> #!/usr/local/bin/python3
>
> print('Hello module world!')
> ```
>
> 通过控制台命令行把它当作程序运行：
>
> ```
> $ chmod +x script1.py           # 赋予可执行权限；另见：#!/usr/bin/env python3
> $ ./script1.py                  # 仅当 "." 不在 PATH 上时才需要 "./"
> Hello module world!
> $ python3 script1.py            # 或者正常、可移植地运行
> Hello module world!
> ```

### 代码分析

```python
#!/usr/local/bin/python3    # Unix 的 shebang（#!）行：告诉操作系统用哪个解释器执行本文件
print('Hello module world!')
```

- `chmod +x script1.py`：赋予文件可执行权限（Unix/macOS 需要）。
- `./script1.py`：显式指出"在当前目录下执行"——若 `.` 不在 PATH 环境变量中就必须加 `./`。
- `python3 script1.py`：绕过 shebang，直接指定解释器运行，最可移植。

### 深度理解

- **核心概念**：shebang 让脚本可以像系统命令一样直接执行；操作系统看到 `#!` 行就调用指定解释器。
- **Windows 上的特殊行为**：Windows 的 `py` 启动器会解析 `#!` 行（尽管是 Unix 语法）来选择 Python 版本（如 py -3、py -3.11），受默认版本设置影响。
- **可移植性问题**：不同机器上 `/usr/local/bin/python3` 未必存在；`#!/usr/bin/env python3` 通过 PATH 查找更通用，但依赖 PATH 配置。这就是作者说它"通常可移植性差"的原因。
- **常见误区**：在 shell 里直接敲 `python3 script.py` 时 shebang 根本不会被读取；Windows 双击 .py 靠的是文件关联（file association），与 shebang 无关。

---

## 题 5. Errors and debugging（错误与调试）

### 英文原文

> **5. Errors and debugging**: The following interaction demonstrates the sorts of error messages you'll get when you complete this exercise. Really, you're triggering Python exceptions; the default exception-handling behavior terminates the running Python program and prints an error message and stack trace on the screen.
>
> The stack trace shows where you were in a program when the exception occurred (if function calls are active when the error happens, the "Traceback" section displays all active call levels).

> In Chapter 10 and Part VII, you will learn that you can catch exceptions using `try` statements and process them arbitrarily. You'll also learn that Python includes a full-blown source code debugger (module `pdb`) for special error-detection requirements. For now, notice that Python gives meaningful messages when programming errors occur, instead of crashing silently:

> ```
> $ python3
>>> 2 ** 500
> 32733906078961418700131896968275991522166420460430647894832913680961337964 046745 54883270092325904157150886684127560071009217256545885393053328527589376

>>> 1 / 0
> Traceback (most recent call last): File "<stdin>", line 1, in <module> ZeroDivisionError: division by zero

>>> oops
> Traceback (most recent call last): File "<stdin>", line 1, in <module> NameError: name 'oops' is not defined

> ```

### 中文翻译

> **5. 错误与调试**：下面的交互过程演示了你完成这个练习时会看到的各类错误消息。说真的，你是在触发 Python 的异常（exception）；默认的异常处理行为会终止正在运行的 Python 程序，并在屏幕上打印一条错误消息和堆栈跟踪（stack trace，即回溯 traceback）。堆栈跟踪显示异常发生时你在程序中的位置（如果出错时函数调用正处于活动状态，"Traceback"部分会显示所有活动调用层级）。
>
> 在第 10 章和第七部分，你会学到用 `try` 语句捕获异常并按需处理；你还会学到 Python 内置了一个功能完整的源码级调试器（模块 `pdb`），用于特殊的错误检测需求。现在请先注意：发生编程错误时，Python 会给出有意义的提示消息，而不是悄悄崩溃：
>
> ```
> $ python3
> >>> 2 ** 500
> 32733906078961418700131896968275991522166420460430647894832913680961337964
> 046745
> 54883270092325904157150886684127560071009217256545885393053328527589376
> >>> 1 / 0
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> ZeroDivisionError: division by zero
> >>> oops
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> NameError: name 'oops' is not defined
> ```

### 代码分析

```text
>>> 2 ** 500       # Python 的 int 是"无限精度"大整数，2 的 500 次方直接算出完整结果
>>> 1 / 0          # 除以零 → 运行时异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>   # 回溯第一段：异常发生在 <stdin> 第 1 行模块顶层
ZeroDivisionError: division by zero     # 异常类型 + 消息：零除错误

>>> oops           # 使用从未赋值的名字 → NameError（名字查找失败）
NameError: name 'oops' is not defined
```

### 深度理解

- **核心概念**：错误分两类——**语法错误**（编译期发现）与**运行时异常**（执行期抛出）。这里的 `1/0`、`oops` 都是运行时异常。
- **Traceback 的读法**：从下往上读！最下面一行是"异常类型: 消息"，往上每层 `File "...", line N, in 函数名` 显示异常冒泡经过的调用链。
- **底层机制**：异常是对象，由解释器 `raise` 抛出，沿调用栈向上传播，最终被默认处理器捕获并打印、终止程序。`pdb` 调试器可在异常处断下，`try` 语句则能捕获并转换处理（Part VII 详述）。
- **为什么这样设计**：把运行期问题"显式化"，而不是像 C 语言那样直接段错误（segmentation fault）挂掉——这让新手能定位错误、让程序能优雅降级。
- **常见误区**：新手看 Traceback 盯着最上面的 `File "<stdin>"` 一行，其实**根源在最后一行**的异常类型与消息。

---

## 题 6. Breaks and cycles（中断与循环）

### 英文原文

> **6. Breaks and cycles**: When you type this code:
>
> ```
> $ python3
> >>> L = [1, 2]
> >>> L.append(L)
> >>> L
> [1, 2, [...]]
> ```
>
> you create a **cyclic** data structure in Python. In Python releases before 1.5.1, the Python printer wasn't smart enough to detect cycles in objects, and it would print an unending stream of `[1, 2, [1, 2, [1, 2, [1, 2`, and so on until you hit the Ctrl+C break-key combination on your machine (which, technically, raises a keyboard-interrupt exception that prints a default message).
>
> Beginning with Python 1.5.1, the printer is clever enough to detect cycles, prints `[...]` instead to let you know that it has detected a loop in the object's structure, and avoids getting stuck printing forever.
>
> The reason for the cycle is subtle and requires information you will glean in Part II, so this is something of a preview. But in short, assignments in Python always generate **references** to objects, not copies of them. You can think of objects as chunks of memory and of references as implicitly followed pointers. When you run the first assignment in the preceding code, the name `L` becomes a named reference to a two-item list object—a pointer to a piece of memory.
>
> Python lists are really arrays of object references, with an `append` method that changes the array in place by tacking on another object reference at the end. Here, the `append` call adds a reference to the front of `L` at the end of `L`, which leads to the cycle illustrated in Figure B-1: a pointer at the end of the list that points back to the front of the list.
>
> **Figure B-1.** A cyclic object, created by appending a list to itself.
>
> Besides being printed specially, as you'll learn in Chapter 6, cyclic objects must also be handled specially by Python's garbage collector, or their space will remain unreclaimed even when they are no longer in use. Though rare in practice, in some programs that traverse arbitrary objects or structures, you might have to detect such cycles yourself by keeping track of where you've been to avoid looping.
>
> Believe it or not, cyclic data structures can sometimes be useful, despite their special-case printing.

### 中文翻译

> **6. 中断与循环**：当你输入这段代码时：
>
> ```
> >>> L = [1, 2]
> >>> L.append(L)
> >>> L
> [1, 2, [...]]
> ```
>
> 你就在 Python 中创建了一个**循环**（cyclic）数据结构。在 Python 1.5.1 之前的版本中，Python 的打印器不够聪明，无法检测对象中的循环，于是会一直打印 `[1, 2, [1, 2, [1, 2, [1, 2`……没完没了，直到你在机器上按下 Ctrl+C 中断键组合（从技术上讲，这会抛出一个打印默认消息的键盘中断异常）。从 Python 1.5.1 开始，打印器变得足够聪明，能检测循环，改而打印 `[...]`，让你知道它检测到了对象结构中的环，从而避免永远卡在打印上。
>
> 循环产生的原因很微妙，需要用到你在第二部分获得的知识，所以这算是一种预告。简单来说：Python 中的赋值总是生成对对象的**引用**（references），而不是对象的副本。你可以把对象想象成内存块，把引用想象成隐式跟随的指针。运行前面代码中第一条赋值后，名字 `L` 成为一个对"双元素列表对象"的命名引用——一块内存的指针。Python 列表本质是对象引用的数组，`append` 方法通过在末尾再挂接一个对象引用来**就地**修改数组。这里 `append` 调用在 `L` 的末尾添加了一个指向 `L` 开头的引用，于是产生了图 B-1 所示的循环：列表尾部的一个指针，指回列表头部。
>
> 除了被特殊打印之外，正如你在第 6 章会学到的，循环对象还必须由 Python 的垃圾回收器（garbage collector）特殊处理，否则即使它们不再被使用，其空间也无法回收。虽然实践中少见，但在一些遍历任意对象或结构的程序中，你可能需要自己通过记录"去过哪里"来检测这类循环，以避免死循环。信不信由你，循环数据结构有时还真有点用处——尽管它们打印时是特殊格式。

### 代码分析

```python
L = [1, 2]        # 创建含两个整数引用的列表对象，L 是指向它的命名引用
L.append(L)       # 就地调用 append：在 L 的末尾追加"L 自己"这个引用
L                 # 于是 L = [1, 2, L]，形成环
# 输出：[1, 2, [...]]
```

**图 B-1**：一个循环对象——列表向自身追加自身而创建：列表尾部有一个指回列表头部的指针。

### 深度理解

- **核心概念**：变量名是**引用**而非"盒子"；赋值复制的是引用（指针），不是对象内容。这几乎是全书最重要的心智模型。
- **为什么会产生环**：列表是"引用数组"；`L.append(L)` 把 `L` 所指对象的引用追加进该对象自身，内部指针指向自己，形成环。
- **打印的演变**：Python 1.5.1 前打印器会无限递归打印；此后检测到环就打印 `[...]` 占位。同理，序列化（pickle）、遍历等库也会对环做特殊标记。
- **垃圾回收的联动**：CPython 用**引用计数**做主回收；但循环引用使计数永不为零，必须靠**分代循环垃圾回收器**（gc 模块）定期扫描检测回收。
- **实际意义**：自引用结构（如循环链表、图的缓存环）偶尔有用；但遍历任意对象时必须记录已访问对象，否则死循环。
- **常见误区**：`L.append(L)` 不是把 `[1,2]` 复制一份再放进列表，而是放进一个指向**同一个对象**的引用——对象只有一份。

---

# Part II：Objects and Operations（对象与运算）

### 英文原文

> Part II, Objects and Operations
> See "Test Your Knowledge: Part II Exercises" in Chapter 9 for the exercises.

### 中文翻译

> 第二部分：对象与运算。练习见第 9 章的 "Test Your Knowledge: Part II Exercises"。

### 深度理解

- **核心概念**：Part II 的练习覆盖数字、字符串、元组、列表、字典、文件等核心对象类型的**索引、切片、拼接、方法调用、可变性、嵌套**操作。
- **学习方法**：这些练习的最佳做法是**自己在 REPL 里敲一遍**——本部分答案全是交互会话，照敲一遍比背结论有效得多。

---

## 题 1. The basics（基础）

### 英文原文

> **1. The basics**: Here are the sorts of results you should get, along with a few comments about their meaning. Again, note that `;` is used in a few of these to squeeze more than one statement onto a single line (the `;` is a statement separator), and commas build up tuples displayed in parentheses. See file `Part2/basics.txt` for copy/paste sans emedia, though typing these manually is a good way to practice syntax:

> ```
> $ python3
> # Numbers
> >> 2 ** 16 65536 >> 2 / 5, 2 / 5.0 (0.4, 0.4)

> # Strings
> >> 'hack' + 'code''hackcode'>> S = 'Python'>> 'grok ' + S'grok Python'>> S * 5'PythonPythonPythonPythonPython'>> S[0], S[:0], S[1:] ('P', '', 'ython') >> how = 'fun'>> 'coding %s is %s!' % (S, how)'coding Python is fun!'

> >> 'coding {} is {}!'.format(S, how)'coding Python is fun!'

> >> f'coding {S} is {how}!''coding Python is fun!'

> # Tuples
> >> ('x',)[0]'x'>> ('x', 'y')[1]'y'

> # Lists
> >> L = [1, 2, 3] + [4, 5, 6] >> L, L[:], L[:0], L[-2], L[-2:] ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [], 5, [5, 6]) >> ([1, 2, 3] + [4, 5, 6])[2:4] [3, 4] >> [L[2], L[3]] [3, 4] >> L.reverse(); L [6, 5, 4, 3, 2, 1] >> L.sort(); L [1, 2, 3, 4, 5, 6] >> L.index(4) 3

> # Dictionaries
> >> {'a': 1, 'b': 2}['b'] 2 >> D = {'x': 1, 'y': 2, 'z': 3} >> D['w'] = 0 >> D['x'] + D['w'] 1 >> D[(1, 2, 3)] = 4 >> D {'x': 1, 'y': 2, 'z': 3, 'w': 0, (1, 2, 3): 4} >> list(D.keys()), list(D.values()), (1, 2, 3) in D (['x', 'y', 'z', 'w', (1, 2, 3)], [1, 2, 3, 0, 4], True)

> # Empties
> >> [[]], ["", [], (), {}, None] ([[]], ['', [], (), {}, None])

> ```

### 中文翻译

> **1. 基础**：下面是你应得到的各类结果，附带少量关于其含义的说明。再次注意：其中有几处使用了 `;` 把多条语句挤到一行（`;` 是语句分隔符），逗号会构成元组并以括号形式显示。需要"无媒体"（纯文本）的复制/粘贴版本，参见文件 `Part2/basics.txt`；不过手动敲这些是练习语法的好方法：
>
> ```
> # 数字
> >>> 2 ** 16                          # 2 的 16 次幂
> 65536
> >>> 2 / 5, 2 / 5.0                   # 真除法，保留余数（小数部分）
> (0.4, 0.4)
> # 字符串
> >>> 'hack' + 'code'                  # 拼接（Concatenation）
> 'hackcode'
> >>> S = 'Python'
> >>> 'grok ' + S
> 'grok Python'
> >>> S * 5                            # 重复（Repetition）
> 'PythonPythonPythonPythonPython'
> >>> S[0], S[:0], S[1:]               # 索引、空切片、子串
> ('P', '', 'ython')                   # S[:0] 是开头处的空切片 [0:0]，返回同类型的空值
> >>> how = 'fun'
> >>> 'coding %s is %s!' % (S, how)    # 百分号格式化（expression）
> 'coding Python is fun!'
> >>> 'coding {} is {}!'.format(S, how)  # format 方法
> 'coding Python is fun!'
> >>> f'coding {S} is {how}!'          # f-string 字面量
> 'coding Python is fun!'
> # 元组
> >>> ('x',)[0]                        # 索引单元素元组
> 'x'
> >>> ('x', 'y')[1]                    # 索引双元素元组
> 'y'
> # 列表
> >>> L = [1, 2, 3] + [4, 5, 6]        # 列表拼接
> >>> L, L[:], L[:0], L[-2], L[-2:]    # 列表操作：整表/切片/空切片/负索引/负切片
> ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [], 5, [5, 6])
> >>> ([1, 2, 3] + [4, 5, 6])[2:4]     # 拼接后再切片
> [3, 4]
> >>> [L[2], L[3]]                     # 从偏移位置取值，存入新列表
> [3, 4]
> >>> L.reverse(); L                   # 方法：就地反转
> [6, 5, 4, 3, 2, 1]
> >>> L.sort(); L                      # 方法：就地排序
> [1, 2, 3, 4, 5, 6]
> >>> L.index(4)                       # 方法：第一个 4 的偏移量（搜索）
> 3
> # 字典
> >>> {'a': 1, 'b': 2}['b']            # 按键索引字典
> 2
> >>> D = {'x': 1, 'y': 2, 'z': 3}
> >>> D['w'] = 0                       # 创建新条目
> >>> D['x'] + D['w']
> 1
> >>> D[(1, 2, 3)] = 4                 # 用元组（不可变）作键
> >>> D
> {'x': 1, 'y': 2, 'z': 3, 'w': 0, (1, 2, 3): 4}
> >>> list(D.keys()), list(D.values()), (1, 2, 3) in D   # 键、值、键成员测试
> (['x', 'y', 'z', 'w', (1, 2, 3)], [1, 2, 3, 0, 4], True)
> # 空对象
> >>> [[]], ["", [], (), {}, None]     # 各种"空"：空对象们
> ([[]], ['', [], (), {}, None])
> ```

### 代码分析（逐行解读）

```text
>>> 2 ** 16                    # 幂运算符：整型结果 65536
>>> 2 / 5, 2 / 5.0             # / 是真除法（true division），永远返回 float
                               # 括号输出说明这是两个表达式构成的元组
>>> 'hack' + 'code'            # 字符串拼接产生新字符串
>>> S = 'Python'               # 赋值：S 引用字符串对象
>>> 'grok ' + S                # 拼接：'grok Python'
>>> S * 5                      # 重复 5 次，生成新字符串
>>> S[0], S[:0], S[1:]         # 索引第 0 个字符；空切片 [0:0]；从 1 到末尾
                               # 结果 ('P', '', 'ython')：空切片返回同类型空对象
>>> 'coding %s is %s!' % (S, how)      # 老式 % 格式化
>>> 'coding {} is {}!'.format(S, how)  # 2.6+ 的 str.format 方法
>>> f'coding {S} is {how}!'            # 3.6+ 的 f-string：字面量内嵌表达式
>>> ('x',)[0]                  # 单元素元组必须有逗号 ('x',)；索引得 'x'
>>> L = [1, 2, 3] + [4, 5, 6]  # 列表拼接 → [1,2,3,4,5,6]
>>> L[:0]                      # 空切片 → []（与字符串空切片同型）
>>> L[-2]                      # 负索引：倒数第 2 个 → 5
>>> L[-2:]                     # 负切片：最后两个 → [5, 6]
>>> L.reverse(); L             # 就地反转，返回 None；用 ; 在一行里接着打印 L
>>> L.sort(); L                # 就地排序（升序）
>>> L.index(4)                 # 线性搜索值 4，返回其偏移量 3
>>> D['w'] = 0                 # 字典"写不存在键"= 创建条目
>>> D[(1, 2, 3)] = 4           # 元组键完全合法（可哈希、不可变）
>>> list(D.keys())             # keys() 返回视图（view），必须 list() 转列表查看
>>> (1, 2, 3) in D             # 键成员测试：in 检查的是键，不是值 → True
>>> [[]], ["", [], (), {}, None]   # 每个类型都有"空"表示；None 是单例空值
```

### 深度理解

- **核心概念**：本练习覆盖三大容器家族——不可变序列（字符串、元组）、可变序列（列表）、映射（字典）——加上三种字符串格式化手段（`%`、`format`、f-string）。
- **底层机制**：`reverse()` 和 `sort()` 都是**就地**修改并返回 `None`——所以示例里用 `;` 分隔、再单独求值 `L` 才能看到修改结果；这是 Python 设计者特意为之（防止你误以为返回新列表）。`index()` 是线性搜索。
- **空切片返回同类型**：`S[:0]` 是 `''`、`L[:0]` 是 `[]`——"空"永远和对象类型一致，这是很多算法的语法基础。
- **字典键的约束**：键必须可哈希（hashable），即不可变对象；元组可以、列表不行。`in` 对字典查的是键。
- **常见误区**：`L.reverse()` 不返回列表（返回 None）；`D.keys()` 不是列表而是视图；`('x')` 是字符串而 `('x',)` 才是元组。

---

## 题 2. Indexing and slicing（索引与切片）

### 英文原文

> **2. Indexing and slicing**: Indexing out of bounds (e.g., `L[4]`) raises an error; Python always checks to make sure that all offsets are within the bounds of a sequence.

> On the other hand, slicing out of bounds (e.g., `L[-1000:100]`) works because Python scales out-of-bounds slices so that they always fit (the limits are set to zero and the sequence length, if required).

> Extracting a sequence in reverse, with the lower bound greater than the higher bound (e.g., `L[3:1]`), doesn't really work. You get back an empty slice (`[]`) because Python scales the slice limits to make sure that the lower bound is always less than or equal to the upper bound (e.g., `L[3:1]` is scaled to `L[3:3]`, the empty insertion point at offset `3`).

> Python slices are always extracted from left to right, even if you use negative indexes (they are first converted to positive indexes by adding the sequence length). Note that Python's three-limit slices modify this behavior somewhat. For instance, `L[3:1:-1]` does extract from right to left:

> ```
> >> L = [1, 2, 3, 4] >> L[4] Traceback (most recent call last): File "<stdin>", line 1, in <module> IndexError: list index out of range >> L[-1000:100] [1, 2, 3, 4] >> L[3:1] [] >> L [1, 2, 3, 4] >> L[3:1] = ['?'] >> L [1, 2, 3, '?', 4]

> ```

### 中文翻译

> **2. 索引与切片**：越界索引（如 `L[4]`）会抛出错误；Python 总是检查所有偏移量是否落在序列边界之内。
>
> 另一方面，越界切片（如 `L[-1000:100]`）是可行的，因为 Python 会把越界的切片"缩放"（scales）到总能适配的范围内（必要时把下限定为 0、上限定为序列长度）。
>
> 要反向提取序列（下界大于上界，如 `L[3:1]`）其实行不通：你得到的是空切片（`[]`），因为 Python 会缩放切片边界，确保下界总是小于等于上界（例如 `L[3:1]` 被缩放成 `L[3:3]`，即偏移量 `3` 处的空插入点）。
>
> Python 切片总是从左到右提取，即使你使用负索引也不例外（负索引会先加序列长度转换成正索引）。注意 Python 的三参数切片会部分改变这一行为。例如 `L[3:1:-1]` 确实是自右向左提取：
>
> ```
> >>> L = [1, 2, 3, 4]
> >>> L[4]              → IndexError：list index out of range（越界索引报错）
> >>> L[-1000:100]      → [1, 2, 3, 4]（越界切片被自动缩放）
> >>> L[3:1]            → []（被缩放成 L[3:3]，空切片）
> >>> L[3:1] = ['?']    → 切片赋值：在位置 3 插入 '?'
> >>> L                 → [1, 2, 3, '?', 4]
> ```

### 代码分析（逐行解读）

```python
L = [1, 2, 3, 4]
L[4]                  # 索引 4 越界：序列长度 4，合法索引 0..3 → IndexError
L[-1000:100]          # 切片边界不做严格检查：-1000 缩放到 0，100 缩放到 4 → 整个列表
L[3:1]                # 下界 3 > 上界 1，缩放到 [3:3] → 空切片 []
L[3:1] = ['?']        # 对空切片赋值 = 在偏移 3 处插入元素 '?'
L                     # → [1, 2, 3, '?', 4]
```

### 深度理解

- **核心概念**：索引与切片是两种不同的操作——**索引越界报错**，**切片越界自动缩放**。这是 Python 精心设计的语义差异。
- **底层机制**：索引调用 `__getitem__(int)`，解释器先做边界检查；切片调用 `__getitem__(slice)`，内部先做"边界裁剪"（clamping）：负索引加序列长度，越界值裁剪到 [0, len] 区间。
- **为什么这样设计**：切片越界安全，让 `L[a:b]` 这类通用写法在递归、分治算法里无需防御性检查；而索引越界则往往意味着逻辑 bug，报错更利于调试。
- **三参数切片的例外**：`L[3:1:-1]` 的第三参数是**步长（step）**，为负时从右向左提取，且下界/上界语义互换（start 大于 stop 时正常取）。
- **切片赋值（slice assignment）**：`L[3:1] = ['?']` 用空区间做**插入**；若区间非空则是替换或删除（见下一题）。
- **常见误区**：以为 `L[3:1]` 会反向返回 `[4, 3]`——它返回空列表；反向要用 `L[3:1:-1]`。

---

## 题 3. Indexing, slicing, and del（索引、切片与删除）

### 英文原文

> **3. Indexing, slicing, and del**: Your interaction with the interpreter should look something like the following. Note that assigning an empty list to an offset stores an empty list object there, but assigning an empty list to a slice deletes the slice. Slice assignment expects another sequence, or you'll get a type error; it inserts items *inside* the sequence assigned, not the sequence itself:

> ```
> >> L = [1, 2, 3, 4] >> L[2] = [] >> L [1, 2, [], 4] >> L[2:3] = [] >> L [1, 2, 4] >> del L[0] >> L [2, 4] >> del L[1:] >> L [2] >> L[1:2] = 1 Traceback (most recent call last): File "<stdin>", line 1, in <module> TypeError: can only assign an iterable

> ```

### 中文翻译

> **3. 索引、切片与 del（删除）**：你与解释器的交互应该大致如下。注意：给**偏移量**赋空列表（`L[2] = []`）会在那里存一个空列表对象；但给**切片**赋空列表（`L[2:3] = []`）则是删除该切片。切片赋值期待另一个序列，否则你会得到类型错误；它把被赋序列的**元素**插入到序列**内部**，而不是插入序列本身：
>
> ```
> >>> L = [1, 2, 3, 4]
> >>> L[2] = []          → [1, 2, [], 4]（索引赋值：把空列表对象存入偏移 2）
> >>> L[2:3] = []        → [1, 2, 4]（切片赋值空列表 = 删除该切片）
> >>> del L[0]           → [2, 4]（删除偏移 0 的元素）
> >>> del L[1:]          → [2]（删除从 1 到末尾的切片）
> >>> L[1:2] = 1         → TypeError: can only assign an iterable（切片赋值右侧必须是可迭代对象）
> ```

### 代码分析（逐行解读）

```python
L = [1, 2, 3, 4]
L[2] = []                # 索引赋值：把空列表对象（作为值）放进索引 2 的槽位
                         # → [1, 2, [], 4]（列表里多了一个"嵌套空列表"）
L[2:3] = []              # 切片赋值：把空可迭代对象展开进 [2:3] 区间
                         # 零个元素替换一个元素 → 删除效果 → [1, 2, 4]
del L[0]                 # del 语句：按索引删除 → [2, 4]
del L[1:]                # del 语句：按切片删除 → [2]
L[1:2] = 1               # 切片赋值右侧必须是可迭代对象（iterable）；
                         # 整数 1 不可迭代 → TypeError
```

### 深度理解

- **核心概念**：列表的三种"改"操作语义截然不同——**索引赋值**（替换一个槽位）、**切片赋值**（用可迭代对象的元素展开替换一段，长度可变）、**del**（删除索引或切片，长度缩短）。
- **底层机制**：索引赋值走 `__setitem__(int, value)`；切片赋值走 `__setitem__(slice, iterable)`，解释器先展开可迭代对象再"挤进"区间，因此区间长度与右侧元素个数可以不同，导致列表增长或收缩。
- **为什么 `L[2:3] = []` 会删除**：把右侧空列表的 0 个元素"挤进"长度为 1 的区间，等价于删掉该区间。
- **常见误区**：分不清 `L[2] = []`（存空列表）与 `L[2:3] = []`（删元素）；以及忘记切片赋值右侧必须是可迭代对象（字符串、列表、range 都可以，整数不行）。

---

## 题 4. Tuple assignment（元组赋值）

### 英文原文

> **4. Tuple assignment**: The values of `X` and `Y` are swapped. When tuples appear on the left and right of an assignment symbol (`=`), Python assigns objects on the right to targets on the left according to their positions. This is probably easiest to understand by noting that the targets on the left aren't a real tuple, even though they look like one; they are simply a set of independent assignment targets.
>
> The items on the right are a tuple, which gets unpacked during the assignment (this tuple provides the temporary assignment needed to achieve the swap effect):
>
> ```
> >>> X = 'code'
> >>> Y = 'hack'
> >>> X, Y = Y, X
> >>> X
> 'hack'
> >>> Y
> 'code'
> ```

### 中文翻译

> **4. 元组赋值**：`X` 和 `Y` 的值被交换了。当元组出现在赋值符号（`=`）的左右两侧时，Python 会按位置把右侧的对象赋给左侧的目标。理解这一点最容易的方式是：注意到左侧的目标并不是真正的元组，尽管它们看起来像元组；它们只是一组相互独立的赋值目标。右侧的项才是一个元组，它会在赋值过程中被解包（unpacked）（这个元组提供了实现交换效果所需的临时赋值）：
>
> ```
> >>> X = 'code'
> >>> Y = 'hack'
> >>> X, Y = Y, X        # 右侧先打包成元组 ('hack', 'code')，再按位解包赋给 X、Y
> >>> X                  # 'hack'
> >>> Y                  # 'code'
> ```

### 代码分析（逐行解读）

```python
X = 'code'      # X 引用字符串 'code'
Y = 'hack'      # Y 引用字符串 'hack'
X, Y = Y, X     # 1) 先求值右侧：打包成元组 ('hack', 'code')
                # 2) 再按位解包：X = 'hack'，Y = 'code'
X               # → 'hack'
Y               # → 'code'
```

### 深度理解

- **核心概念**：元组解包（unpacking）赋值——右边先**打包**成临时元组，左边再按位置**解包**。它提供了"隐式临时变量"，使交换只需一行。
- **底层机制**：`X, Y = Y, X` 编译成的字节码是先建立元组再索引解包（如 `UNPACK_SEQUENCE` 指令），右侧求值先于左侧赋值完成，所以绝不出现"X 已被覆盖"的中间状态。
- **为什么左侧不是真元组**：`(X, Y)` 写在赋值左侧时语法上就是"目标列表"（target list），不是一个被创建的对象。
- **扩展**：同一机制还支持 `a, b, c = 序列`（解包任意序列）、`a, *rest = 序列`（星号收集多余项）、`for k, v in dict.items()` 等。
- **常见误区**：初学担心"先赋 X 会丢旧值"——临时元组保证了原子性；另外元素个数不匹配会抛 `ValueError`。

---

## 题 5. Dictionary keys（字典键）

### 英文原文

> **5. Dictionary keys**: Any immutable (technically, "hashable") object can be used as a dictionary key, including integers, tuples, strings, and so on. This really is a dictionary, even though some of its keys look like integer offsets. Mixed-type keys work fine, too:
>
> ```
> >>> D = {}
> >>> D[1] = 'a'
> >>> D[2] = 'b'
> >>> D[(1, 2, 3)] = 'c'
> >>> D
> {1: 'a', 2: 'b', (1, 2, 3): 'c'}
> ```

### 中文翻译

> **5. 字典键**：任何不可变（严格地说"可哈希" hashable）对象都可以用作字典键，包括整数、元组、字符串等等。这确实是一个字典，尽管其中有些键看起来像整数偏移量。混合类型的键也完全没问题：
>
> ```
> >>> D = {}
> >>> D[1] = 'a'              # 整数键
> >>> D[2] = 'b'              # 整数键
> >>> D[(1, 2, 3)] = 'c'      # 元组键
> >>> D
> {1: 'a', 2: 'b', (1, 2, 3): 'c'}
> ```

### 代码分析（逐行解读）

```python
D = {}                # 空字典
D[1] = 'a'            # 键是整数 1：字典的键不要求是"序号"，任意可哈希对象都行
D[2] = 'b'            # 键是整数 2
D[(1, 2, 3)] = 'c'    # 键是元组：元组不可变、可哈希，合法
D                     # → {1: 'a', 2: 'b', (1, 2, 3): 'c'}
```

### 深度理解

- **核心概念**：字典键必须**可哈希（hashable）**——即对象有稳定的 `__hash__` 值且可比较相等。整数、浮点数、字符串、元组（内部元素也全部可哈希）都可以；列表、字典、集合是可变对象，不可哈希、不能当键。
- **底层机制**：字典是哈希表（hash table）。查找键时先算 `hash(key)` 定位桶（bucket），再用 `==` 比较处理冲突。若键可变，哈希值会变化，导致条目"丢失"，所以语言层面禁止。
- **为什么整数键合法**：字典的键是"任意对象"，不是"从 0 开始的连续整数"；列表的整数索引只是它的特例语法。
- **常见误区**：以为键必须是字符串；以为元组只要包含一个列表也不能当键（确实不能——可哈希性要求元组内所有元素都可哈希）；用 `in` 测字典时查的是键而不是值。

---

## 题 6. Dictionary indexing（字典索引）

### 英文原文

> **6. Dictionary indexing**: Indexing a nonexistent key (`D['d']`) raises an error; assigning *to* a nonexistent key (`D['d']='hack'`) creates a new dictionary entry. On the other hand, out-of-bounds indexing for lists raises an error, too, but so do out-of-bounds assignments. Variable names work like dictionary keys; they must have already been assigned when referenced, but they are created when first assigned.

> In fact, variable names can be processed as dictionary keys if you wish (they're made visible in the dictionaries of stack frames or module [or other object] namespaces):

> ```
> >> D = {'a': 1, 'b': 2, 'c': 3} >> D['a'] 1 >> D['d'] Traceback (most recent call last): File "<stdin>", line 1, in <module> KeyError: 'd'>> D['d'] = 4 >> D {'a': 1, 'b': 2, 'c': 3, 'd': 4} >> L = [0, 1] >> L[2] Traceback (most recent call last): File "<stdin>", line 1, in <module> IndexError: list index out of range >> L[2] = 3 Traceback (most recent call last): File "<stdin>", line 1, in <module> IndexError: list assignment index out of range

> ```

### 中文翻译

> **6. 字典索引**：索引一个不存在的键（`D['d']`）会抛出错误；**对**不存在的键**赋值**（`D['d']='hack'`）则会创建新的字典条目。另一方面，列表的越界索引会报错，越界赋值同样报错。变量名的工作方式与字典键类似：它们在被引用之前必须已经被赋值，而在首次赋值时被创建。事实上，如果你愿意，变量名也可以当作字典键来处理（它们会出现在栈帧或模块（或其他对象）命名空间的字典里）：
>
> ```
> >>> D = {'a': 1, 'b': 2, 'c': 3}
> >>> D['a']        → 1（读存在的键）
> >>> D['d']        → KeyError: 'd'（读不存在的键：报错）
> >>> D['d'] = 4    → 对不存在的键赋值：创建新条目
> >>> D             → {'a': 1, 'b': 2, 'c': 3, 'd': 4}
> >>> L = [0, 1]
> >>> L[2]          → IndexError: list index out of range（列表越界索引报错）
> >>> L[2] = 3      → IndexError: list assignment index out of range（列表越界赋值也报错）
> ```

### 代码分析（逐行解读）

```python
D['a']          # 读已有键 → 1
D['d']          # 读不存在键 → KeyError：'d'
D['d'] = 4      # 写不存在键 → 自动创建新条目（字典"写自动扩容"）
L[2]            # 列表读越界 → IndexError
L[2] = 3        # 列表写越界 → IndexError（列表不能"越界创建"，必须先 append 扩容）
```

### 深度理解

- **核心概念**：读与写的语义不同——字典读不存在键报 `KeyError`，写不存在键则"惰性创建"；列表读写越界都报 `IndexError`。原因：字典是**映射**（键集合自由扩张），列表是**定长序列**（下标必须落在 0..len-1）。
- **变量名即字典键**：Python 的实现里，命名空间本身就是字典——模块的 `__dict__`、函数栈帧的 `f_locals` 都是字典。"变量未定义"在底层就是"字典里没有这个键"。所以 `dir()`、`globals()` 能看到所有变量名。
- **常见误区**：把字典当成"序号数组"用；或以为列表能像字典一样自动扩容——列表必须显式 `append`/`extend`。

---

## 题 7. Generic operations（通用操作）

### 英文原文

> **7. Generic operations**: Question answers (with some error text omitted in listings): a. The `+` operator doesn't work on different/mixed types (e.g., string + list, list + tuple).

> b. `+` doesn't work for dictionaries, as they aren't sequences (though `|` does).

> c. The `append` method works only for lists, not strings, and `keys` works only on dictionaries. `append` assumes its target is mutable, since it's an in-place extension; strings are immutable. Dictionary `keys` is similarly type specific.

> d. Slicing and concatenation always return a new object of the same type as the objects processed:

> ```
> >> 'x' + 1 TypeError: illegal argument type for built-in operation >> {} + {} TypeError: bad operand type(s) for + >> [].append(9) >> ''.append('s') AttributeError: attribute-less object >> list({}.keys()) [] >> [].keys() AttributeError: keys >> [][:] [] >> ''[:]''

> ```

### 中文翻译

> **7. 通用操作**：问答答案如下（列表中的部分错误文本已省略）：
>
> a. `+` 运算符不能用于不同类型/混合类型（例如 string + list、list + tuple）。
>
> b. `+` 对字典不适用，因为字典不是序列（不过 `|` 可以）。
>
> c. `append` 方法只适用于列表，不适用于字符串；`keys` 只适用于字典。`append` 假定其目标是可变的，因为它是就地扩展；而字符串是不可变的。字典的 `keys` 同样具有类型特异性。
>
> d. 切片与拼接总是返回一个与所处理对象**同类型**的新对象：
>
> ```
> >>> 'x' + 1          → TypeError（混合类型相加：非法）
> >>> {} + {}          → TypeError（字典不是序列，不支持 +）
> >>> [].append(9)     → 就地追加，返回 None
> >>> ''.append('s')   → AttributeError（字符串没有 append 方法）
> >>> list({}.keys())  → []（空字典的键转列表）
> >>> [].keys()        → AttributeError（列表没有 keys 方法）
> >>> [][:]            → []（空切片返回同类型空列表）
> >>> ''[:]            → ''（空切片返回同类型空字符串）
> ```

### 代码分析（逐行解读）

```python
'x' + 1             # 不同类型相加：str 与 int 的 __add__ 互相不接受 → TypeError
{} + {}             # dict 没有实现 __add__（不是序列，无"拼接"概念）→ TypeError
[].append(9)        # 列表就地追加 9，返回 None（交互模式不显示 None）
''.append('s')      # 字符串不可变，没有 append 方法 → AttributeError
list({}.keys())     # 空字典的 keys() 视图 → list() 转成空列表 []
[].keys()           # 列表没有 keys 方法 → AttributeError
[][:]               # 切片操作：空列表切片 → 新空列表 []
''[:]               # 字符串切片 → 新空字符串 ''
```

### 深度理解

- **核心概念**：Python 是强类型语言——运算符和方法大多**类型特化**，不同类型之间拒绝隐式转换或混用。切片与拼接是"保型"操作（返回同类型新对象）。
- **底层机制**：`+` 走二元运算符协议（`__add__` / `__radd__`），每个类型自己决定支持与否；方法（`append`、`keys`）只存在于对应类型的方法表里。切片走 `__getitem__(slice)`，类型自己构造同类型返回值。
- **为什么字典没有 +**：`+` 的语义是"序列拼接"（保持顺序）；字典是无序映射，没有拼接概念。Python 3.9+ 给字典补了 `|`（合并）运算符作为替代。
- **字符串为什么没有 append**：字符串不可变；就地扩展会破坏不可变性，所以设计者根本不提供该方法（想"改"字符串要用拼接或 `bytearray`）。
- **常见误区**：以为 `"abc" + 1` 会自动把 1 转成字符串（不会，必须显式 `str(1)`）；以为所有容器都有 keys/append。

---

## 题 8. String indexing（字符串索引）

### 英文原文

> **8. String indexing**: This is a bit of a trick question—because strings are collections of one-character strings, every time you index a string, you get back a string that can be indexed again. `S[0][0][0][0][0]` just keeps indexing the first character over and over. This generally doesn't work for lists (lists can hold arbitrary objects) unless the list contains strings:
>
> ```
> >>> S = 'hack'
> >>> S[0][0][0][0][0]
> 'h'
> >>> L = ['h', 'a']
> >>> L[0][0][0]
> 'h'
> ```

### 中文翻译

> **8. 字符串索引**：这算一道脑筋急转弯——因为字符串是"单字符字符串"的集合，每次索引字符串得到的都是可再被索引的字符串。`S[0][0][0][0][0]` 只是一遍又一遍地索引第一个字符。这对列表通常不成立（列表可以装任意对象），除非列表里恰好是字符串：
>
> ```
> >>> S = 'hack'
> >>> S[0][0][0][0][0]   → 'h'（每次索引都取第 0 个字符，结果还是 'h'）
> >>> L = ['h', 'a']
> >>> L[0][0][0]         → 'h'（L[0] 是字符串 'h'，因此还能继续索引）
> ```

### 代码分析（逐行解读）

```python
S = 'hack'
S[0][0][0][0][0]    # S[0] → 'h'；'h'[0] → 'h'；……无论索引多少次都是 'h'
L = ['h', 'a']
L[0][0][0]          # L[0] → 'h'（字符串）；'h'[0] → 'h'；再索引还是 'h'
```

### 深度理解

- **核心概念**：字符串的"原子"也是字符串（单字符字符串）——类型系统上的"递归自包含"，让索引链永不失效。
- **底层机制**：`'h'[0]` 返回一个**新的**单字符字符串对象（CPython 会复用内部缓存的小字符串），其本身仍是字符串，支持 `__getitem__`，所以可以无限索引下去。
- **列表的区别**：`L[0]` 返回的是任意对象；若 `L[0]` 是整数，再索引 `L[0][0]` 就报 `TypeError`（int 不可索引）。
- **常见误区**：误以为字符串能"索引到字符的字符"——字符串没有更底层的单元，字符就是字符串本身。

---

## 题 9. Immutable types（不可变类型）

### 英文原文

> **9. Immutable types**: Either of the following solutions works. Index assignment doesn't because strings are immutable:
>
> ```
> >>> S = 'hack'
> >>> S = S[0] + 'e' + S[2:]
> >>> S
> 'heck'
> >>> S = S[0] + 'i' + S[2] + S[3]
> >>> S
> 'hick'
> ```
>
> (See also the `bytearray` string type in Chapter 37—it's a mutable sequence of small integers that is essentially processed the same as a string, especially when its bytes are ASCII character code points.)

### 中文翻译

> **9. 不可变类型**：下面两种方案都可以。索引赋值不行，因为字符串是不可变的：
>
> ```
> >>> S = 'hack'
> >>> S = S[0] + 'e' + S[2:]   # 拼接法：'h' + 'e' + 'ck' → 'heck'
> >>> S
> 'heck'
> >>> S = S[0] + 'i' + S[2] + S[3]   # 逐字索引拼接：'h' + 'i' + 'c' + 'k' → 'hick'
> >>> S
> 'hick'
> ```
>
> （另见第 37 章的 `bytearray` 字符串类型——它是小整数的可变序列，处理方式本质上与字符串相同，尤其当它的字节是 ASCII 字符码点时。）

### 代码分析（逐行解读）

```python
S = 'hack'
S = S[0] + 'e' + S[2:]        # 取原字符串的片段重新拼接出新字符串，再赋值给 S
                              # S[0]='h'，S[2:]='ck' → 'h' + 'e' + 'ck' = 'heck'
S = S[0] + 'i' + S[2] + S[3]  # 显式索引每个字符：'h'+'i'+'c'+'k' = 'hick'
```

### 深度理解

- **核心概念**：字符串不可变（immutable）——没有"原地修改"操作。任何"修改"都是**构造新字符串再重新赋值**。
- **底层机制**：CPython 中字符串是 `PyUnicodeObject`，内部没有 `__setitem__` 修改路径；`S[0] = 'e'` 会直接抛 `TypeError: 'str' object does not support item assignment`。
- **为什么这样设计**：不可变性让字符串可以安全共享（驻留）、哈希、用作字典键、跨线程传递。
- **bytearray 的补充**：`bytearray` 是**可变**的字节序列，需要频繁修改字符串内容时可先转 `bytearray` 改完再转回。
- **常见误区**：试图 `S[0] = 'e'`；或在循环里用 `s += c` 大量拼接（产生 O(n²) 临时对象），应改用 `''.join()`。

---

## 题 10. Nesting（嵌套）

### 英文原文

> **10. Nesting**: Here is a sample (your specs will vary):
>
> ```
> >>> pat = {'name': ('Pat', 'Q', 'Jones'), 'age': None, 'job': 'engineer'}
> >>> pat['job']
> 'engineer'
> >>> pat['name'][2]
> 'Jones'
> ```

### 中文翻译

> **10. 嵌套**：这里是一个样例（你的规格可能会不同）：
>
> ```
> >>> pat = {'name': ('Pat', 'Q', 'Jones'), 'age': None, 'job': 'engineer'}
> >>> pat['job']        → 'engineer'（按键取值）
> >>> pat['name'][2]    → 'Jones'（值本身是元组，再按位置取第 2 项）
> ```

### 代码分析（逐行解读）

```python
pat = {'name': ('Pat', 'Q', 'Jones'),   # 字典的"值"是一个元组：嵌套结构
       'age': None,                     # 值可以是 None（占位）
       'job': 'engineer'}
pat['job']        # 字典索引 → 'engineer'
pat['name'][2]    # 两步：先 pat['name'] 得到元组，再 [2] 得到 'Jones'
```

### 深度理解

- **核心概念**：容器可以任意嵌套——字典里装元组、元组里装列表、列表里装字典……"对象组合成对象"正是 Python 数据的精髓。
- **访问链**：`pat['name'][2]` 是链式索引，每一步返回的对象决定下一步的索引语义——这是"表达式从左到右逐步求值"的体现。
- **实际价值**：用嵌套结构可以无类地表达记录（record）数据；需要更严格的结构时可升级为类（Part VI）。
- **常见误区**：`age: None` 表示"未赋值"，不是 0 也不是空字符串；嵌套的共享引用问题（改内部对象会影响所有引用它的容器）。

---

## 题 11. Files（文件）

### 英文原文

> **11. Files**: Examples B-3 and B-4 show one way to create and read back a text file in Python using Unicode encoding defaults on the host (which are generally moot for simple ASCII text like this): **Example B-3.** `Part2/maker.py`

> ```python
> file = open('myfile.txt', 'w')
> file.write('Hello file world!\n') # Or: open().write() file.close() # close not always needed

> ```
> **Example B-4.** `Part2/reader.py`

> ```python
> file = open('myfile.txt')            # 'r' is default open mode
> print(file.read())                   # Or print(open().read())
> ```
> When run (here, from a console command line), the file shows up in the directory you're working in because its name has no path prefix. The `ls` here is a Unix command; use `dir` on Windows:

> ```
> $ python3 maker.py
> $ python3 reader.py
> Hello file world!

> $ ls -l myfile.txt
> -rw-r--r-- 1 me staff 18 Aug 11 19:34 myfile.txt

> ```

### 中文翻译

> **11. 文件**：示例 B-3 和 B-4 展示了在 Python 中创建并读回文本文件的一种方式，使用主机环境的 Unicode 编码默认值（对这样的简单 ASCII 文本来说，编码默认值一般无关紧要）：
>
> **示例 B-3.** `Part2/maker.py`（写文件）
> ```python
> file = open('myfile.txt', 'w')
> file.write('Hello file world!\n')    # 或者：open().write()
> file.close()                         # close 并不总需要
> ```
>
> **示例 B-4.** `Part2/reader.py`（读文件）
> ```python
> file = open('myfile.txt')            # 'r' 是默认打开模式
> print(file.read())                   # 或者 print(open().read())
> ```
>
> 运行时（这里从控制台命令行），文件会出现在你工作的目录中，因为文件名没有路径前缀。这里的 `ls` 是 Unix 命令；Windows 上用 `dir`：
>
> ```
> $ python3 maker.py
> $ python3 reader.py
> Hello file world!
> $ ls -l myfile.txt
> -rw-r--r-- 1 me staff 18 Aug 11 19:34 myfile.txt
> ```

### 代码分析（逐行解读）

```python
# maker.py —— 写文件
file = open('myfile.txt', 'w')   # 'w' = 写模式；文件不存在则创建，存在则清空
file.write('Hello file world!\n') # 把字符串写入缓冲；'\n' 是换行符
file.close()                     # 关闭文件：刷新缓冲并释放句柄
                                 # （不显式 close 时，对象被回收也会自动关闭，但显式更可靠）

# reader.py —— 读文件
file = open('myfile.txt')        # 默认模式 'r'（只读文本）
print(file.read())               # read() 读入整个文件内容并返回字符串，print 打印
```

### 深度理解

- **核心概念**：文件操作三步骤——`open`（打开）→ 读/写 → `close`（关闭）。`open` 的第一个参数是路径，第二个是模式（'r' 读、'w' 写、'a' 追加、'rb'/'wb' 二进制）。
- **底层机制**：文件对象是缓冲 IO 流：写入先进内存缓冲，`close()`（或 `flush()`）时才真正落盘；`read()` 返回整个文件字符串。Python 3 文本模式默认按平台编码（UTF-8）编解码 Unicode。
- **为什么 close "不总需要"**：CPython 引用计数归零时对象会自动关闭文件；但显式关闭（或用 `with open(...) as f:`）是良好习惯——可移植性更好、可预测。
- **相对路径**：文件名无路径前缀 → 相对当前工作目录（运行命令所在目录）。`ls`/`dir` 可确认文件生成。
- **常见误区**：以 `'w'` 打开会**清空**原文件内容；忘记写 `'\n'` 导致多行内容挤一行；`print(open(...))` 打印的是文件对象而不是内容（必须 `.read()`）。

# Part III：Statements and Syntax（语句与语法）

### 英文原文

> Part III, Statements and Syntax
> See "Test Your Knowledge: Part III Exercises" in Chapter 15 for the exercises.

### 中文翻译

> 第三部分：语句与语法。练习见第 15 章的 "Test Your Knowledge: Part III Exercises"。

### 深度理解

- **核心概念**：Part III 练习从"对象层"上升到"语句层"——`for`/`while` 循环、`if` 选择、`match` 语句、字典排序、字符串转义字符，以及同一逻辑的多种等价写法（if/match/dict/list）。

---

## 题 1. Coding basic loops（编写基础循环）

### 英文原文

> **1. Coding basic loops**: As you work through this exercise, you'll wind up with code that looks like the following:

> ```
> >> S = 'hack'>> for c in S:

> ...             print(ord(c))
> ...
> 104 97 99 107 >> x = 0 >> for c in S: x += ord(c) # Or: x = x + ord(c)

> ...
> >> x 407 >> chr(x) # Extra credit: non-ASCII, see Chapter 37'Ɨ'>> x = [] >> for c in S: x.append(ord(c)) # Manual list construction

> ...
> >> x [104, 97, 99, 107] >> list(map(ord, S)) [115, 112, 97, 109] >> [ord(c) for c in S] # map and listcomps automate list builders [115, 112, 97, 109]

> ```

### 中文翻译

> **1. 编写基础循环（循环的走向）**：等你做完全部步骤，你会得到类似下面的代码：
>
> ```
> >>> for c in S: print(ord(c))        # 逐个字符打印其 Unicode 码点（ord）
> 104    # 'h'
> 97     # 'a'
> 99     # 'c'
> 107    # 'k'
> >>> x = 0
> >>> for c in S: x += ord(c)        # 或：x = x + ord(c)——累加所有码点
> 407
> >>> chr(x)                        # 加分项：非 ASCII 码点，见第 37 章
> 'Ɨ'
> >>> x = []
> >>> for c in S: x.append(ord(c))  # 手动构造列表
> [104, 97, 99, 107]
> >>> list(map(ord, S))            # map 内置调用：自动化构造列表
> [115, 112, 97, 109]
> >>> [ord(c) for c in S]          # 列表推导式：同样自动化
> [115, 112, 97, 109]
> ```

（注意：原文后两条打印的是 map/列表推导式作用于 'spam' 之类字符串的示例输出，若你对 'hack' 求值，结果会是 [104, 97, 99, 107]；本质都是"取每个字符的码点"。）

### 代码分析（逐行解读）

```python
S = 'hack'
for c in S:                 # 字符串可迭代：每次发射一个字符
    print(ord(c))           # ord()：字符 → Unicode 码点（整数）

x = 0
for c in S:
    x += ord(c)             # 增强赋值：x = x + ord(c)，累积码点和
x                           # → 407
chr(x)                      # chr()：码点 → 字符；407 对应非 ASCII 字符 'Ɨ'

x = []
for c in S:
    x.append(ord(c))        # 手动往列表逐项添加
x                           # → [104, 97, 99, 107]

list(map(ord, S))           # map(函数, 可迭代对象)：把 ord 逐一映射到 S 的每个字符；
                            # Python 3 的 map 返回惰性迭代器，必须 list() 才能看到列表
[ord(c) for c in S]         # 列表推导式：等价却更"声明式"
```

### 深度理解

- **核心概念**：同一个任务（把每个字符转成码点）有三种表达方式——手写 `for+append`、`map` 内置、列表推导式。三者结果等价，但风格与性能不同。
- **底层机制**：`for c in S` 走迭代协议（`S.__iter__`）；`ord` 是 C 实现的内置函数；`map(ord, S)` 逐元素应用函数并惰性产出；列表推导 `[expr for c in S]` 编译成专门的快速循环。
- **为什么把 `range`/`map` 的「结果可能一样」当作练习点**：这是 Python 由"过程式"通往"函数式/声明式"的桥梁概念，为 Part IV 的推导式、生成器做铺垫。
- **常见误区**：Python 3 里 `map` 返回的是迭代器而非列表，直接打印只会看到 `<map object at ...>`；忘记在 `for` 循环后换行缩进。

---

## 题 2. Coding basic selections（编写基础选择）

### 英文原文

> **2. Coding basic selections**: Here is the sort of code expected. To handle out-of-range numbers, add an `else` for `if`, a `case _` for `match`, a `get` method call or `in` test for the dictionary, and a `try` handler for the list. For versions of this code that are easier to copy/paste, see file `Part3/selections.txt` in the examples package:

> ```
> >>> month = 3
> >>> if month == 1:
> ...             print('January')
> ... elif month == 2:
> ...             print('February')
> ... elif month == 3:
> ...             print('March')
> ...
> March

> >>> match month:
> ...     case 1:
> ...             print('January')
> ...     case 2:
> ...             print('February')
> ...     case 3:
> ...             print('March')
> ...
> March

> >>> {1: 'January', 2: 'February', 3: 'March'}[month]
> 'March'

> >>> ['January', 'February', 'March'][month - 1]
> 'March'

> ```

### 中文翻译

> **2. 编写基础选择**：下面是期望的代码形态。为了处理越界数字：`if` 加个 `else`，`match` 加个 `case _`，字典用 `get` 方法或 `in` 测试，列表用 `try` 处理。示例包里 `Part3/selections.txt` 有更容易复制/粘贴的版本：
>
> ```
> >>> month = 3
> >>> if month == 1:            # elif 链：从上到下匹配
> ...     print('January')
> ... elif month == 2:
> ...     print('February')
> ... elif month == 3:
> ...     print('March')
> March
> >>> match month:              # Python 3.10+ 的结构化模式匹配
> ...     case 1:
> ...         print('January')
> ...     case 2:
> ...         print('February')
> ...     case 3:
> ...         print('March')
> March
> >>> {1: 'January', 2: 'February', 3: 'March'}[month]   # 字典查表
> 'March'
> >>> ['January', 'February', 'March'][month - 1]        # 列表索引
> 'March'
> ```

### 代码分析（逐行解读）

```python
month = 3
if month == 1: print('January')   # if/elif 链：逐条件真值测试
elif month == 2: print('February')
elif month == 3: print('March')   # → 打印 March

match month:                      # match 语句：模式匹配，比 if 链更结构化
    case 1: print('January')
    case 2: print('February')
    case 3: print('March')

{1: 'January', 2: 'February', 3: 'March'}[month]   # 字典按键查表 → 'March'
['January', 'February', 'March'][month - 1]        # 列表索引（0 基，故 month-1）→ 'March'
```

### 深度理解

- **核心概念**：同一个"分类"问题有四种表达：`if/elif` 链（过程式）、`match/case`（结构化模式匹配，3.10+）、字典查表（映射式）、列表索引（序号式）。
- **边界处理方式的差异**：`if` 需 `else` 兜底；`match` 需 `case _`（通配）兜底；字典越界读报 `KeyError`，可用 `dict.get(key, 默认)` 或先 `in` 判断；列表越界报 `IndexError`，可用 `try/except` 捕获或用 `month-1` 算好再检查范围。
- **设计思想**：字典查表是"数据驱动编程"的典范——把分支逻辑转化为数据映射，可读性、扩展性都好。
- **常见误区**：列表索引漏掉 `-1`（`month=1` 会取到 'January' 才对，直接 `[month]` 会错位/越界）；`match` 是表达式作用于值，不要写成 `==` 链式的误用。

---

## 题 3. Backslash characters（反斜杠字符）

### 英文原文

> **3. Backslash characters**: The example prints the bell character (`\a`) 50 times. Assuming your machine can handle it, and when it's run outside of some interfaces like IDLE, you may get a series of beeps (or one sustained tone if your machine is fast enough). Hey—you were warned.

### 中文翻译

> **3. 反斜杠字符**：示例打印 50 次响铃字符（`\a`）。假设你的机器能处理它，并且它在 IDLE 等一些界面之外运行，你可能会听到一串"哔"声（如果你的机器足够快，可能是一个持续的长音）。嘿——这可是警告过你的哦。

### 代码分析

```python
print('\a' * 50)    # 打印 50 个响铃字符（ASCII 码 7, BEL）
```

### 深度理解

- **核心概念**：反斜杠（`\`）在字符串字面量里是**转义字符**前缀：`\a` 是响铃、`\n` 是换行、`\t` 是制表符、`\\` 是字面反斜杠、`\'`/`\"` 是转义引号。
- **底层机制**：转义在**编译期**完成——`'\\a'` 在字节码里就是一个含单个 BEL 字符的字符串；`* 50` 字符串重复产生 50 个 BEL。
- **实际输出**：终端碰到 BEL 字符会发哔声/闪屏；IDLE 等图形界面的文本控件往往忽略它。
- **常见误区**：Windows 路径 `'C:\new'` 里的 `\n` 会被当成换行符——用 raw 字符串 `r'C:\new'` 或双反斜杠。

---

## 题 4. Sorting dictionaries（字典排序）

### 英文原文

> **4. Sorting dictionaries**: Here's one way to work through this exercise (see Chapter 8 or Chapter 14 if this doesn't make sense). You really do have to split off the `keys` and `sort` calls like this because `sort` returns `None`. You can iterate through dictionary keys directly without calling `keys` (e.g., `for key in D:`), but the keys list will not be sorted like it is by this code. The `sorted` built-in is simpler but creates a new list object:
>
> ```
> >>> D = {'a': 1, 'c': 3, 'e': 5, 'g': 7, 'f': 6, 'd': 4, 'b': 2}
> >>> D
> {'a': 1, 'c': 3, 'e': 5, 'g': 7, 'f': 6, 'd': 4, 'b': 2}
> >>> keys = list(D.keys())    # Keys view has no sort method
> >>> keys.sort()              # Sort list in place: returns None
> >>> for key in keys:
> ...             print(key, '=>', D[key])
> ...
> a => 1
> b => 2
> c => 3
> d => 4
> e => 5
> f => 6
> g => 7
> >>> D
> {'a': 1, 'c': 3, 'e': 5, 'g': 7, 'f': 6, 'd': 4, 'b': 2}
> >>>
> >>> for key in sorted(D):    # Simpler alternative, but a new list
> ...             print(key, '=>', D[key])
> ...
> …same output…
> ```

### 中文翻译

> **4. 字典排序**：解决这个练习的一种方法如下（看不懂就回头翻第 8 章或第 14 章）。你确实必须像这样把 `keys` 和 `sort` 这两个调用拆开：因为 `sort` 返回的是 `None`。你可以直接遍历字典（例如 `for key in D:`），不需要调用 `keys`，但那样遍历的键**不会**像这段代码那样有序。内置的 `sorted` 更简单，但会创建新的列表对象：
>
> ```
> >>> D = {...}                    # 注意：字典本体顺序不变（内部实际为键插入序/哈希序）
> >>> keys = list(D.keys())        # dict_keys 视图没有 sort 方法，必须先转成 list
> >>> keys.sort()                  # 列表就地排序，返回 None
> >>> for key in keys: print(key, '=>', D[key])
> a => 1
> b => 2
> …g => 7                           # 按键字母序输出
> >>> for key in sorted(D):        # 更简单的替代：对可迭代对象排序并返回新列表
> ...      print(key, '=>', D[key])
> …同样输出…
> ```

### 代码分析（逐行解读）

```python
D = {'a': 1, 'c': 3, 'e': 5, 'g': 7, 'f': 6, 'd': 4, 'b': 2}
keys = list(D.keys())   # 1) D.keys() 返回 dict_keys 视图（只读、无 sort 方法）
                        # 2) list(...) 转成真正的列表
keys.sort()             # 3) 列表就地排序（升序），返回 None
for key in keys:        # 4) 按排序后的键遍历，按键查值
    print(key, '=>', D[key])
# 输出 a=>1 b=>2 c=>3 d=>4 e=>5 f=>6 g=>7

for key in sorted(D):   # 更简洁：sorted 接收任意可迭代对象（含字典→迭代键），返回新列表
    print(key, '=>', D[key])
# 输出同上
```

### 深度理解

- **核心概念**：字典本身**无序**（历史上是哈希序；Python 3.7+ 保插入序但不"排序"），想按键排序必须借助"键列表 + 排序"。
- **为什么不能 `D.keys().sort()`**：`dict_keys` 视图只提供只读迭代，没有 `sort` 方法；必须先 `list()` 复制成真正的列表。
- **为什么 `keys.sort()` 要单独一行**：`list.sort()` 是**就地**排序、返回 `None`，所以 `print(keys.sort())` 会打印 `None`——这是 Python 最具名的"陷阱"之一。
- **更优做法**：`sorted(D)` 一步到位（内置函数返回新列表）；`for key in sorted(D)` 是惯用法。
- **常见误区**：以为字典"本来就是有序的"（只是 3.7+ 保证插入序，不等于排序）；把就地方法当返回新对象用。

---

## 题 5. Program logic alternatives（程序逻辑的多种等价写法）

### 英文原文

> **5. Program logic alternatives**: Here's some sample code for the solutions, available in the examples package's `Part3/power*.py`. For step e, assign the result of `2 ** X` to a variable outside the loops of steps a and b and use it inside the loop. Your results may vary; this exercise is mostly designed to get you playing with code alternatives, so anything reasonable gets full credit:
>
> ```python
> # a
> L = [1, 2, 4, 8, 16, 32, 64]
> X = 5
> i = 0
> while i < len(L):
>     if 2 ** X == L[i]:
>         print('at index', i)
>         break
>     i += 1
> else:
>     print(X, 'not found')
>
> # b
> L = [1, 2, 4, 8, 16, 32, 64]
> X = 5
> for p in L:
>     if (2 ** X) == p:
>         print((2 ** X), 'was found at', L.index(p))
>         break
> else:
>     print(X, 'not found')
> ```

### 中文翻译

> **5. 程序逻辑的多种写法**：下面是这些解答的样例代码，位于示例包的 `Part3/power*.py`。对于步骤 e（"深入思考"），把 `2 ** X` 的值赋给循环外的变量，再在循环里使用它。你的结果可能会不同；这个练习的初衷主要是让你玩一玩代码的各种等价写法，所以任何合理的解法都算满分：
>
> ```
> # a：while + 手动索引 + break + else
> L = [1, 2, 4, 8, 16, 32, 64]
> X = 5
> i = 0
> while i < len(L):
>     if 2 ** X == L[i]:
>         print('at index', i)
>         break
>     i += 1
> else:
>     print(X, 'not found')
>     ```
> # b：for + L.index 查位置
> L = [1, 2, 4, 8, 16, 32, 64]
> X = 5
> for p in L:
>     if (2 ** X) == p:
>         print((2 ** X), 'was found at', L.index(p))
>         break
> else:
>     print(X, 'not found')
> ```

## 题 5（续）：c、d、e 与完整代码

这部分和后面的选项在答案原料里一起给出的更完整代码整理如下（含 `if X in L` 的第三种写法、构造列表的第四种、以及"深入思考"（map/列表推导式）的第五种）。它们的目的是演示**用不同方式表达"在一个列表里找 2 的 X 次方"**：

```python
# c
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
if (2 ** X) in L:                       # in 成员测试
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

# d
X = 5
L = []
for i in range(7):
    L.append(2 ** i)                    # 先构造列表（2**0..2**6）
print(L)                                # [1, 2, 4, 8, 16, 32, 64]
if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

# "Deeper thoughts" (e)
X = 5
L = list(map(lambda x: 2 ** x, range(7)))   # 或 [2 ** x for x in range(7)]
print(L)
if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')
```

### 深度理解

- **写法对比**：a 用 `while` + `break` + **循环 `else`**（不被 break 才打印 not found）；b 用 `for` 直接遍历值并用 `L.index(p)` 反查位置；c 用 `in` 一次性判断加查位置；d 先动态构造 2 的幂列表再查；e 用 `map(lambda...)` 或列表推导式一行构造列表。
- **`while` 的 `else` 子句**：Python 特有语法——循环**没有被 `break` 提前终止**时才执行 `else`，非常优雅地处理了"找不到"分支。
- **设计思想**：同一逻辑五种表达，锻炼"用多种视角看问题"；e 的"把结果变量提出来在循环外算一次"是性能技巧（避免循环里重复计算 `2**X`）。
- **常见误区**：`L.index(p)` 是线性搜索，代价高；`in` 也是线性。a、b 的 `else` 语义与 `for/while` 绑定，与 `if` 的 `else` 无关。

---

# Part IV：Functions and Generators（函数与生成器）

### 英文原文

> Part IV, Functions and Generators
> See "Test Your Knowledge: Part IV Exercises" in Chapter 21 for the exercises.

### 中文翻译

> 第四部分：函数与生成器。练习见第 21 章的 "Test Your Knowledge: Part IV Exercises"。

### 深度理解

- **核心概念**：Part IV 练习覆盖函数的多态、参数传递（位置/关键字/`*args`/`**kwargs`/默认值）、参数匹配规则、递归、推导式与 `map`、计时工具（`timer2.py`）、素数、阶乘，以及"标准库 vs 手写 vs 递归"的效率权衡。

---

## 题 1. The basics（基础）

### 英文原文

> **1. The basics**: There's not much to this one, but notice that using `print` (and hence your function) is technically a **polymorphic** operation, which does the right thing for each type of object:

> ```
> $ python3
> >>> def echo(x):
> ...     print(x)
> ...
> >>> echo('hack')
> hack

> >>> echo(3.12)
> 3.12

> >>> echo([1, 2, 3])
> [1, 2, 3]

> >>> echo({'edition': 6})
> {'edition': 6}

> ```

### 中文翻译

> ```python
> >>> def echo(x):        # 函数体只有一句 print(x)：x 的类型不被声明
> ...     print(x)
> >>> echo('hack')        → hack（字符串）
> >>> echo(3.12)          → 3.12（浮点数）
> >>> echo([1, 2, 3])     → [1, 2, 3]（列表）
> >>> echo({'edition': 6}) → {'edition': 6}（字典，注意这里只是键=6）
> ```
> 这一点就是**多态（polymorphism）**：`print`（以及你的函数）对每种对象都"做正确的事"。

（题目正文只有这两段：答案要点在于多态。）

### 代码分析（逐行解读）

```python
def echo(x):          # 形参 x 没有类型注解——运行时才确定类型
    print(x)          # print 是内置函数：调用对象的 __str__ 生成可读字符串

echo('hack')          # str 的 __str__ → 原样输出 hack
echo(3.12)            # float 的 __str__ → 3.12
echo([1, 2, 3])       # list 的 __str__ → '[1, 2, 3]'
echo({'edition': 6})  # dict 的 __str__ → "{'edition': 6}"
```

### 深度理解

- **核心概念**：**多态性（polymorphism）**——同一个接口（函数）作用于不同类型的对象，行为各自正确。"鸭子类型（duck typing）"：只要对象支持所需的操作（这里是 `__str__`），就能被 `print` 用。
- **底层机制**：`print` 内部调用 `str(x)`，即 `x.__str__()`——每种内置类型都实现了 `__str__`；用户自定义类也可覆写它定制打印格式。所以"能做对的事"不是魔法，而是协议（protocol）约定。
- **为什么这样设计**：Python 弱化类型标注，让你无需为每种类型重写一遍打印逻辑；适合快速开发与通用工具库。
- **常见误区**：多态 ≠ 隐式类型转换。`echo(1) + echo('x')` 仍会报类型错误，"多态"是针对"都能被打印"，不是"到处都是同一个类型"。

---

## 题 2. Arguments（参数与多态加法）

### 英文原文

> ```python
> # Part4/adder1.py
> def adder(x, y):  return x + y
> print(adder(5, 1.0))          # 6.0
> print(adder('hack', 'code'))  # hackcode
> print(adder(['a', 'b'], ['c', 'd']))  # ['a', 'b', 'c', 'd']
> ```
> And the output:

> ```
> $ python3 adder1.py
> 6.0 hackcode ['a', 'b', 'c', 'd']

> ```

### 中文翻译

> 示例 B-5 给出一个样例方案。记住：**必须用 `print`** 才能在测试调用里看到结果，因为文件不同于交互式输入的代码；Python 不会像在 `>>>` 提示符下那样回显文件里表达式语句的结果：
> ```python
> def adder(x, y):
>     return x + y
> print(adder(5, 1.0))          # 6.0（数值相加）
> print(adder('hack', 'code'))  # hackcode（字符串拼接）
> print(adder(['a', 'b'], ['c', 'd'])) # ['a','b','c','d']（列表拼接）
> ```

### 深度理解

- **核心概念**：`return x + y` 里 `+` 也是**多态**的——对数值做算术、对字符串/列表做拼接。同一个函数签名服务多种类型。
- **为什么强调文件必须 `print`**：交互模式（REPL）会自动回显表达式结果；文件执行时只执行语句，表达式结果被丢弃。这是新手最大的困惑之一。
- **底层**：`int.__add__`、`str.__add__`、`list.__add__` 都是各类型自己实现的"加法"，而函数本身不关心——这是"协议传动"的设计。
- **常见误区**：把 `'hack' + 1` 误想成自动转类型（不会，会 `TypeError`）；忘了在文件里 `print` 结果。

---

## 题 3. Arbitrary arguments（任意个数的位置参数）

### 练习：一个可以接收任意多参数、并返回它们之和的 adder 函数版本。

### 分析纪要

- **难点**：如何把累加器初始化为"传入类型对应的空值"。
- **解法 1**（`adder1`）：判断第一个参数是否为整数（用 `type(args[0]) == type(0)`），是则初始化为 0；否则假定为序列，用空切片 `args[0][:0]` 得到同类空值（`''`、`[]`）。然后 `for` 逐个 `+`。
- **解法 2**（`adder2`）：更优——直接用第一个参数初始化，从 `args[1:]` 开始累加（类似第 18 章 `min` 的变体）；无需显式类型判断。
- 两者都假定所有实参同类型；都不适用于字典（字典无 +，会报 TypeError）；都有更简单的 `sum(iterable)` 内置方案——但练习的初衷是让你亲手写出自己的求和函数。
- **陷阱**：`args[0][:0]` 需要假定的传入的是"可切片"的序列；若是 dict 将直接 `TypeError`。

### 代码

```python
# adder2.py（示例 B-6）
def adder1(*args):
    print('adder1:', end=' ')
    if type(args[0]) == type(0):   # 第一个参数是 int？
        sum = 0                    # 是：累加器从 0 开始
    else:                          # 否：假定期末是可切片序列
        sum = args[0][:0]          # 用空切片"同类空值"初始化
    for arg in args:
        sum = sum + arg
    return sum

def adder2(*args):
    print('adder2: ', end=' ')
    sum = args[0]                  # 初始化用第一个实参
    for next in args[1:]:          # 剩下不用递归，用循环遍历
        sum += next                # 用第二实参开始累加
    return sum

for func in (adder1, adder2):
    print(func(2, 3, 4))
    print(func('hack', 'code', 'well'))
    print(func(['a', 'b'], ['c', 'd'], ['e', 'f']))
```

```text
$ python3 adder2.py
adder1: 9
adder1: hack codewell
adder1: ['a', 'b', 'c', 'd', 'e', 'f']
adder2: 9
adder2: hack codewell
adder2: ['a', 'b', 'c', 'd', 'e', 'f']
```

### 深度理解

- **`*args` 收集**：`*args` 把**任意数量**的位置实参打包为一个元组。两种初始化的思路值得学习。
- **解法 2 更优的理由**：免去类型判断，靠四种类型各自的 `+` 语义（多态）自然得到正确结果——代码更短、更通用。
- **局限与延伸**：假定类型一致；想支持字典合并需改写（如 `for`/`update`/`**`/`|`）；`sum()` 内置只支持数值/可加；学习的重点在于"自己造轮子"。
- **运行文件的原因**：文件里没有自动回显，所以函数里加了 `print` 前缀才输出标记。

---

## 题 4. Keywords（关键字与默认值）

### 练习原文简译（含示例 B-7 / B-8）

- 定义 **`adder3.py`**：默认值三个参数 `red=1, green=2, blue=3`，返回三者之和，测试各种调用方式。
- 定义 **`adder4.py`**：四种版本求和（`*args` 位置收集版、`**args` 关键字收集版 ×3，分别用 `.keys()` 然后逐个访问、用 `.values()` 转换、或直接复用 `adder1(*args.values())`），验证结果一致。

### 代码（示例 B-7 / B-8）

```python
# adder3.py —— 默认值参数
def adder(red=1, green=2, blue=3):
    return red + green + blue

print(adder())               # 全默认：1+2+3 = 6
print(adder(5))              # red=5：5+2+3 = 10
print(adder(5, 6))           # 5+6+3 = 14
print(adder(5, 6, 7))        # 5+6+7 = 18
print(adder(blue=7, red=6, green=5))   # 关键字乱序：6+5+7 = 18
print(adder(blue=1, red=2))  # 部分关键字：2+2+1 = 5
```
```
$ python3 adder3.py
6
10
14
18
18
5
```

```python
# adder4.py —— *args 与 **args 求和
def adder1(*args):            # 任意位置参数
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

def adder2(**args):           # 任意关键字参数
    argskeys = list(args.keys())   # list()：字典键视图不可下标！
    tot = args[argskeys[0]]
    for key in argskeys[1:]:
        tot += args[key]
    return tot

def adder3(**args):           # 相同，但转成值列表
    args = list(args.values())     # list() 才能索引
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

def adder4(**args):           # 直接复用在位置版本上
    return adder1(*args.values())

print(adder1(1,2,3), adder1('aa','bb','cc'))
print(adder2(a=1,b=2,c=3), adder2(a='aa',b='bb',c='cc'))
print(adder3(a=1,b=2,c=3), adder3(a='aa',b='bb',c='cc'))
print(adder4(a=1,b=2,c=3), adder4(a='aa',b='bb',c='cc'))
```
```
$ python3 adder4.py
6 aabbcc
6 aabbcc
6 aabbcc
6 aabbcc
```

### 深度理解

- **默认值**：函数定义时的缺省实参值；调用时按位/按名覆盖。注意默认值在**定义时**求值一次（后面可变默认值是陷阱）。
- **关键字乱序**：关键字参数按名字匹配，顺序无关；可以用 `.keys()/.values()` 遍历 `**args` 字典。
- **list() 的必要性**：`args.keys()` 返回视图对象，没有下标能力，必须 `list()` 后才能 `[0]`、`[1:]`。
- **`**结合 `*`**：`adder1(*args.values())` 展示了 `**` 字典的键值解包再传给 `*` 参数收集——两套"打包/解包"机制互相衔接。
- **常见误区**：默认参数要用不可变值；`**args` 键是字符串名，即函数的形参名。

---

## 题 5 与题 6. Dictionary tools（字典工具）

### 练习重点

- 实现自己的 `copyDict(d)`（复制字典）与 `addDict(d1,d2)`（合并字典）。
- 比较"手写循环"与现代工具：`D.copy()`、`D1.update(D2)`、`{**D1, **D2}`、`D1 | D2`（合并字典的四种方式）。
- 记住：`e = d` **不是复制**，而是让 `e` 成为与 `d` 共享同一个字典对象的引用——改 `d` 会改 `e`。

### 代码（dicttools.py 示例 B-9）

```python
def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]       # 逐键复制——浅拷贝
    return new

def addDict(d1, d2):
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
    for key in d2.keys():
        new[key] = d2[key]       # 若键重复，d2 覆盖 d1
    return new
```

演示（REPL）：
```
>>> from dicttools import *
>>> d = {1: 1, 2: 2}
>>> e = copyDict(d)      # 复制一个新字典
>>> d[2] = '?'           # 改 d
>>> d                    # {1: 1, 2: '?'}
>>> e                    # {1: 1, 2: 2} —— e 不受影响，证明是复制
>>> x = {1: 1}; y = {2: 2}
>>> z = addDict(x, y)    # {1: 1, 2: 2}
```

### 深度理解

- **核心概念**：字典"拷贝"是**浅拷贝**——复制了键和里层引用，里层可变对象仍共享；`e = d` 则是别名（alias）而非拷贝。
- **四种合并**（Python 3.9+ 开始 `|` 运算符成了官方合并语法）：
  1. 手写 `for + ` 循环；
  2. `D1.update(D2)`（就地修改 D1，返回 None）；
  3. `{**D1, **D2}` 字典解包产生**新**字典；
  4. `D1 | D2` 运算符合并，产生新字典。
- **常见误区**：把"引用两用"当拷贝用导致 JSON 编辑一改全改；`D.copy()` 是浅拷贝，深层 json/deepcopy 才处理嵌套。

---

## 题 7. More argument-matching（更多参数匹配）

### 目标文件

```python
# testfuncs.py —— 各类形参形态
def f1(a, b):  print(a, b)          # 长度固定的两个形参
def f2(a, *b): print(a, b)          # 位置收集：多出来的位置存成元组 b
def f3(a, **b): print(a, b)         # 关键字收集：多出的关键字存成字典 b
def f4(a, *b, **c): print(a, b, c)  # 同时收集两类
def f5(a, b=2, c=3): print(a, b, c) # 默认值
def f6(a, b=2, *c): print(a, b, c)  # 默认值 + 收集器
```

REPL 交互（含解释注释）：
```
>>> from testfuncs import *
>>> f1(1, 2)              # 按位置匹配（顺序重要）           → 1 2
>>> f1(b=2, a=1)          # 按名匹配（顺序无所谓）           → 1 2
>>> f2(1, 2, 3)           # 位置收集器：接收 1，两(2,3)装进 b → 1 (2, 3)
>>> f3(1, x=2, y=3)       # 关键字收集器 → 1 {'x': 2, 'y': 3}
>>> f4(1, 2, 3, **dict(x=2, y=3))  # 星号解包调用 → 1 (2, 3) {'x': 2, 'y': 3}
>>> f5(1)                 # 两个默认都用到 → 1 2 3
>>> f5(1, 4)              # 只覆盖一个 → 1 4 3
>>> f5(1, c=4)            # 只覆盖 c → 1 2 4
>>> f6(1)                 # 一个实参 → 1 2 ()
>>> f6(1, *[3, 4])        # 星号解包调用 → 1 3 (4,)
```

### 深度理解（参数匹配规则汇总）

- **实参 → 形参的传递顺序**：先位置匹配的非默认形参，再用关键字参数按名匹配，多余的位置进 `*name`（元组）、多余的关键字进 `**name`（字典），剩下默认值兜底。
- **调用端的解包**：`func(*iterable)` 把可迭代拆成位置实参；`func(**mapping)` 把字典拆成关键字实参——`f6(1, *[3,4])` 等价 `f6(1, 3, 4)`。
- **设计思想**：参数传递的"灵活的"让一个函数既能接收标准调用也能适配第三方"任意签名"的通用可复用接口。
- **常见误区**：`*` 在前 `**` 在后是语法强制；默认参数不能放在无默认参数之前（`def f(a=1, b)` 是语法错误）；函数定义与调用端的 `*`/`**` 语义容易混淆。

---

## 题 8. Primes revisited（素数回归）

### 英文原文

> Sample answer (file `primes.py`), with key notes: use `//` (floor division) to avoid fractional factors; wrapped the logic in a function + module so we can run it repeatedly；加 `y <= 1` 处理边界。这是完整的交互与测试输出（略）。

### 中文翻译

> 这里练习的是"判断一个数是否是素数"（`y > 1` 且只能被 1 和自身整除）。关键点：
> - **用 `//`（整除法）**：`5 / 2` 会得到小数 `2.5`（但 2.5 不是上平=面上的"约数"），而 `5 // 2` 是 `2`，确保我们在整数范围检测。
> - 范围判定到 `y//2` 就够（更大约数一定更小），`while x > 1` 递减，凡整除即合数。
> - **`break` 跳出循环后 `else` 不会执行**：所以 `while … else` 在没找到约数时打印 is prime。

### 完整代码（示例 B-11 primes.py）

```python
def prime(y):
    if y <= 1:                  # 边界：1 和负数不是质数
        print(y, 'is nonprime')
    else:
        x = y // 2              # 从一半开始向下找约数（用 // 而不是 /）
        while x > 1:
            if y % x == 0:      # 有余数就是约数？
                print(y, 'has factor', x)
                break           # 找到即停
            x -= 1
        else:                   # 循环正常结束（无 break）→ 无约数 → 质数
            print(y, 'is prime')

tests = (27, 24, 13, 13.0, 15, 15.0, 3, 2, 1, -3)
for test in tests:
    prime(test)
```

```text
$ python3 primes.py
27 has factor 9
24 has factor 12
13 is prime
13.0 is prime
15 has factor 5
15.0 has factor 5.0
3 is prime
2 is prime
1 is nonprime
-3 is nonprime
```

### 深度理解

- **算法本质**：试除法（trial division），从 `y//2` 往下试除；有因子即合数，无因子即质数。
- **为什么用 // 与 %**：`//` 是地板除、`%` 是取余。`5.0 // 2` → `2.0`，`13.0 // 2` → `6.0`；连续 `13.0` 也判为质数（余数非零）。
- **`else` 与 `break` 的搭配**：循环 `else` 只在没有 `break` 时执行——这是本题最该学到关键结构。
- **脆弱点/改进方向**：函数打印而非 return（可复用性差）；`13.0` 这种浮点会被当正式质数测（数学上应该非整数不考虑）；效率 O(n) 不理想（可 `range(2, int(n**0.5)+1)` 或 Miller-Rabin）。

---

## 题 9. Iterations and comprehensions（迭代与推导式）

### 原文（就是下四种写法）

> ```
> >>> values = [2, 4, 9, 16, 25]
> >>> import math
> >>> res = []
> >>> for x in values: res.append(math.sqrt(x))   # 手动循环
> >>> res
> [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
> >>> list(map(math.sqrt, values))               # map 内置函数
> [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
> >>> [math.sqrt(x) for x in values]             # 列表推导式
> [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
> >>> list(math.sqrt(x) for x in values)         # 生成器表达式（+list()）
> [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
> ```

### 中文要点

同任务四种写法结果一致，无"正确"之分。它们演示了过程式、函数式（map）、声明式（推导式）、惰性（生成器）四种编程风格；涉及算法选择。

### 深度理解

- `map` 参数顺序是"函数在前、可迭代在后"；2.x 返回列表（3.x 返回惰性迭代器，需要 `list()`）。
- 列表推导式更 Pythonic 且略快（专门的 `LIST_APPEND` 字节码）。
- 生成器表达式惰性求值，避免中间大列表——大数据集内存友好。

---

## 题 10. Timing tools（计时工具）

### （前置文件与思路）

- **示例 B-12**：`../../Chapter21/timer2.py`（Example 21-7）的定义已列在示例包，多用于时间戳、基准测试，代码本附录不重打；下方答案用 `timer2.bestoftotal(test,...)` 统计。
- **关键实现**（示例 B-13 timesqrt.py）答点如下：

```python
import sys
sys.path.append('../../Chapter21')   # 把 timer2.py 所在目录加进模块搜索路径
import timer2                        # 作弊式引用第 21 章的工具（Part V 会解释）

reps = 10_000
repslist = list(range(reps))         # 显式生成，避免循环里反复构造 range
from math import sqrt                 # 直接导入 sqrt，避免 math.sqrt 的属性查找

def mathMod():
    for i in repslist:
        res = sqrt(i)                 # 使用 mapsqrt
    return res

def powCall():
    for i in repslist:
        res = pow(i, .5)              # 内置 pow
    return res

def powExpr():
    for i in repslist:
        res = i ** .5                 # 幂运算符
    return res

print(sys.version)
for test in (mathMod, powCall, powExpr):
    elapsed, result = timer2.bestoftotal(test, _reps1=5, _reps=1000)
    print(f'{test.__name__}: {elapsed:.5f} => {result}')
```

结果（CPython 3.12，macOS）：
```
$ python3 timesqrt.py
3.12.2 [Clang 13.0.0 ...]
mathMod: 0.40860 => 99.99499987499375
powCall: 0.68245 => 99.99499987499375
powExpr: 0.57762 => 99.99499987499375
```

**简评**：函数 `sqrt`（C 库封装）最快：`**` 运算符次之；`pow` 内置函数最慢。`pow` 需要做"指数参数多义性"处理，速度略逊。（PyPy 版本 8 倍 2 倍更快，因其 JIT 编译循环 + C 二级浮点。）

> 另：交互式比较字典推导式与 **for** 循环（同任务）的计时亦有说明（`dictcomp` 略快于一倍的 for 循环）。bench 结论因平台/版本而变——请按你的机器重测。

---

## 题 11. Recursive functions（递归函数）

```python
def countdown(N):
    if N == 0:
        print('stop')            # 递归出口
    else:
        print(N, end=' ')        # 先打印当前值（不换行）
        countdown(N - 1)         # 递 N-1

# countdown(5)  →  5 4 3 2 1 stop
# countdown(20) →  20 19 ... 2 1 stop
```

非递归一行同仁（range）：
```python
list(range(5, 0, -1))            # [5, 4, 3, 2, 1]
```

生成器递归版：
```python
def countdown2(N):               # 递归生成器
    if N == 0:
        yield 'stop'
    else:
        yield N
        for x in countdown2(N - 1):
            yield x              # yield from countdown2(N-1) 更简洁

list(countdown2(5))              # [5, 4, 3, 2, 1, 'stop']
```

### 深度理解

- 递归基 case（N==0）终止，否则每次调用处理 N、再调用 N-1 的副本——每次递归都有独立栈帧，局部 N 互不干扰。
- **生成器的坑**：在生成器生成器里直接 `yield countdown2(N-1)` 只是返回一个生成器对象，不产出它的元素；必须 `for ... : yield` 或 `yield from` 代理。
- 计数递减用递归"过度"了：range 更简单直接——这是个"何时该用递归（树型分解）、何时不该（顺序计数）"的绝佳案例。

---

## 题 12. Computing factorials（计算阶乘）

```python
from functools import reduce
from timeit import repeat
import math

def fact0(N):                   # 递归
    if N == 1:
        return N
    else:
        return N * fact0(N - 1)

def fact1(N):                   # 递归单行
    return N if N == 1 else N * fact1(N - 1)

def fact2(N):                   # 函数式 reduce
    return reduce(lambda x, y: x * y, range(1, N + 1))

def fact3(N):                   # 迭代
    res = 1
    for i in range(1, N + 1):
        res *= i
    return res

def fact4(N):                   # 标准库
    return math.factorial(N)

print(fact0(6), fact1(6), fact2(6), fact3(6), fact4(6))    # 6*5*4*3*2*1
print(fact0(500) == fact1(500) == fact2(500) == fact3(500) == fact4(500))  # True

for test in (fact0, fact1, fact2, fact3, fact4):
    print(test.__name__, min(repeat(stmt=lambda: test(500), number=1000, repeat=5)))
```

结果（CP Python 3.12 / macOS）：
```
$ python3 factorials.py
720 720 720 720 720
True
fact0 0.08720566902775317
fact1 0.08635473699541762
fact2 0.06704489700496197
fact3 0.05152307112302461
fact4 0.00873392098583281
```

### 深度理解

- **结论**：递归 = 慢；迭代 = 中；**标准库 `math.factorial` C 实现一骑绝尘**。
- 递归最慢的原因：每次函数调用建立新栈帧、逐层返回乘法；且 N 到约 1000 触发 `RecursionError`。
- `reduce(lambda x, y: x*y, range(1, N+1))` 中间的 lambda 每次调用都有开销。
- 教材意义：**能"标准库 + 内置原语"就不要手写复杂逻辑**——`math.factorial` 是答案作者推荐的"batteries"（电池）。
- 微基准（microbenchmark）结果随解释器/平台变化，别把单个数字当神谕。

# Part V：Modules and Packages（模块与包）

### 英文原文

> Part V, Modules and Packages
> See "Test Your Knowledge: Part V Exercises" in Chapter 25 for the exercises.

### 中文翻译

> 第五部分：模块与包。练习见第 25 章的 "Test Your Knowledge: Part V Exercises"。

### 深度理解

- **核心概念**：Part V 练习围绕模块文件的组织——导入（import/from）、自测（`__main__`）、嵌套导入、包（package）、重载（reload）、循环导入（circular imports）。
- **练习主线**：以一个统计文件行数/字符数的小模块 `mymod.py` 为实验对象，反复改造它，逐步掌握模块系统的全部机制。

---

## 题 1. Import basics（导入基础）

### 英文原文

> **1. Import basics**: When you're done, your file and REPL interaction with it should look similar to Example B-16. Remember that Python can read a whole file into a list of line strings, and the `len` built-in returns the lengths of strings and lists: **Example B-16.** `Part5/mymod.py` (initial code, mymod_start.py)

> ```python
> def countLines(name):
>     file = open(name)
>     return len(file.readlines())
> def countChars(name):
>     return len(open(name).read())
> def test(name):                    # Or pass file object
>     return countLines(name), countChars(name)    # Or return a dictionary
> ```
> ```
> $ python3
> >> import mymod >> mymod.test('mymod.py') (10, 281)

> ```
> Your counts may vary for comments, an extra line at the end, and so on, and you don't need to set `PYTHONPATH` if the module is in the automatically searched current working directory. Note that these functions load the entire file in memory all at once, so they won't work for pathologically large files that are too big for your device's memory.

> To be more robust, you could read line by line with iterators instead and count as you go (see `Part5/mymod_lines.py` in the examples package):

> ```python
> def countLines(name):
>     tot = 0
>     for line in open(name): tot += 1
>     return tot
> def countChars(name):
>     tot = 0
>     for line in open(name): tot += len(line)
>     return tot
> ```
> A generator expression can have the same effect (though the excessive magic may cost you some points):

> ```python
> def countLines(name): return sum(+1 for line in open(name))
> def countChars(name): return sum(len(line) for line in open(name))
> ```
> On Unix, you can verify your output with a `wc` command; on Windows, right-click on your file to view its properties. Note that your script may report fewer characters than Windows does—for portability, Python converts Windows `\r\n` line-end markers to `\n`, thereby dropping one byte (character) per line.

> To match byte counts with Windows exactly, you must open in binary mode (`'rb'`) or add the number of bytes corresponding to the number of lines. See Chapters 9 and 37 for more on end-of-line translations in text files.

> The "ambitious" part of this exercise (passing in a file object so you only open the file once) will require you to use the `seek` method of the built-in file object. It works like C's `fseek` call (and may call it behind the scenes): `seek` resets the current position in the file to a passed-in offset. After a `seek`, future input/output operations are relative to the new position.

> To rewind to the start of a file without closing and reopening it, call `file.seek(0)`; the file `read` methods all pick up at the current position in the file, so you need to rewind to reread.

> **Example B-17.** `Part5/mymod2.py`

> ```python
> def countLines(file):
> file.seek(0) # Rewind to start of file

>     return len(file.readlines())
> def countChars(file):
> file.seek(0) # Ditto (rewind if needed)

>     return len(file.read())
> def test(name):
>     file = open(name)               # Pass file object
>     return countLines(file), countChars(file)   # Open file only once
> ```
> ```
> $ python3
> >> import mymod2 >> mymod2.test('mymod2.py') (12, 414)

> ```

### 中文翻译

> **1. 导入基础**：完成之后，你的文件和与之交互的 REPL 会话应该类似于示例 B-16。记住：Python 可以把整个文件读入一个"行字符串列表"，而内置函数 `len` 返回字符串和列表的长度：
>
> ```python
> def countLines(name):
>     file = open(name)
>     return len(file.readlines())      # 行数 = 行列表的长度
>
> def countChars(name):
>     return len(open(name).read())     # 字符数 = 整个文件字符串的长度
>
> def test(name):                       # 或者传入文件对象
>     return countLines(name), countChars(name)   # 或者返回一个字典
> ```
>
> ```
> >>> import mymod
> >>> mymod.test('mymod.py')
> (10, 281)
> ```
>
> 由于注释、末尾多一个空行等原因，你的计数可能有所不同；如果模块位于自动搜索的当前工作目录中，你不需要设置 `PYTHONPATH`。注意这些函数一次把整个文件读入内存，因此对"大到超出设备内存"的病态大文件无法工作。更健壮的做法是用迭代器逐行读取、边读边计数（见示例包的 `Part5/mymod_lines.py`）：
>
> ```python
> def countLines(name):
>     tot = 0
>     for line in open(name): tot += 1      # 逐行迭代，边读边计
>     return tot
>
> def countChars(name):
>     tot = 0
>     for line in open(name): tot += len(line)
>     return tot
> ```
>
> 生成器表达式也能达到同样效果（不过过于"魔法"可能扣点分）：
> ```python
> def countLines(name): return sum(+1 for line in open(name))
> def countChars(name): return sum(len(line) for line in open(name))
> ```
>
> 在 Unix 上，你可以用 `wc` 命令验证输出；在 Windows 上，右键文件查看属性即可。注意：你的脚本报出的字符数可能比 Windows 少——为了可移植性，Python 会把 Windows 的行结束符 `\r\n` 转换为 `\n`，因此每行会少一个字节（字符）。要与 Windows 的字节数完全一致，你必须用二进制模式（`'rb'`）打开，或加上与行数对应的字节数。关于文本文件的行尾转换，参见第 9 章和第 37 章。
>
> 本练习的"进阶"部分（传入文件对象、只打开一次文件）需要使用内置文件对象的 `seek` 方法。它像 C 的 `fseek` 调用一样工作（并可能在幕后调用它）：`seek` 把文件中的当前位置重置为传入的偏移量。`seek` 之后，后续输入/输出操作都相对新位置进行。要回到文件开头而不关闭重开，调用 `file.seek(0)`；文件 `read` 方法都从当前位置继续，所以要重读必须回卷。
>
> ```python
> def countLines(file):
>     file.seek(0)                    # 回卷到文件开头
>     return len(file.readlines())
>
> def countChars(file):
>     file.seek(0)                    # 同样（需要时回卷）
>     return len(file.read())
>
> def test(name):
>     file = open(name)               # 传入文件对象
>     return countLines(file), countChars(file)   # 只打开一次文件
> ```
>
> ```
> >>> import mymod2
> >>> mymod2.test('mymod2.py')
> (12, 414)
> ```

### 代码分析（逐行解读）

```python
def countLines(name):
    file = open(name)              # 打开文件（默认 'r' 文本模式）
    return len(file.readlines())   # readlines() 把全部行读成一个列表，len 即行数

def countChars(name):
    return len(open(name).read())  # read() 读整个文件成一个字符串，len 即字符数

# 进阶版：传文件对象、只打开一次
def countLines(file):
    file.seek(0)                   # 关键：回卷指针到开头，否则 readlines 会从当前位置继续
    return len(file.readlines())

def countChars(file):
    file.seek(0)                   # 同理：第二次读取前必须回卷
    return len(file.read())

def test(name):
    file = open(name)              # 只打开一次文件对象
    return countLines(file), countChars(file)   # 传给两个计数函数轮流读
```

### 深度理解

- **核心概念**：文件对象是**带位置指针**的流——`read`/`readline`/`readlines` 都从"当前位置"开始。要多次读取同一文件，必须 `seek(0)` 回卷。
- **底层机制**：`seek` 对应 C 的 `fseek`；文件指针（file position indicator）是操作系统层面的概念。`read()` 读全量、`readlines()` 读成行列表、`readline()` 读一行。
- **健壮性**：一次读入内存的方式不适合超大文件；逐行迭代（文件对象本身可迭代）内存友好；`sum(+1 for line in open(name))` 一行等价但可读性差。
- **Windows 换行差异**：Python 文本模式默认做通用换行（universal newlines）翻译：`\r\n` → `\n`，所以字节数会比 Windows 资源管理器显示的少；要精确字节数需 `'rb'` 二进制模式。
- **常见误区**：忘了 seek 导致第二次计数为 0；用 `open(name)` 一次只读；把行数与字符数搞混（`readlines` 带 `\n` 也算一个字符）。

---

## 题 2. from / from *（导入特定名）

### 英文原文

> **2. from/from\***: Here's the `from *` part; replace `*` with `countChars` to do the rest:
>
> ```
> $ python3
> >>> from mymod import *
> >>> countChars('mymod.py')
> 281
> ```

### 中文翻译

> **2. from / from\***：下面是 `from *` 的部分；把 `*` 换成 `countChars` 就能完成其余部分：
>
> ```
> >>> from mymod import *
> >>> countChars('mymod.py')    # * 导入后无需模块名前缀，直接调用
> 281
> ```

### 代码分析

```python
from mymod import *            # 把 mymod 中所有不以 _ 开头的名字复制进当前命名空间
countChars('mymod.py')         # 直接使用，等价 mymod.countChars(...)
# 281
```

### 深度理解

- **核心概念**：`from module import *` 把模块的公共名字（不含下划线开头的）批量复制到当前作用域——少打字，但也**污染命名空间**。
- **与 `import module` 的区别**：`import` 引入的是模块对象本身（`mymod.countChars`）；`from` 引入的是模块里的名字（`countChars`）。两者都让名字指向同一函数对象。
- **最佳实践**：模块可定义 `__all__ = ['名字', ...]` 白名单控制 `*` 导出；Python 官方更推荐显式 `from module import 名字` 而非 `*`。
- **常见误区**：`from ... import *` 不会把下划线名字带进来；两个模块同名时 `*` 会静默覆盖。

---

## 题 3. __main__（主模块自测）

### 英文原文

> **3. \_\_main\_\_**: If you code it properly, this file works in either mode—program run or module import, as Example B-18 and the REPL session following it demo: **Example B-18.** `Part5/mymod.py` (edited)

> ```python
> def countLines(name):
>     file = open(name)
>     return len(file.readlines())
> def countChars(name):
>     return len(open(name).read())
> def test(name):                     # Or pass file object
>     return countLines(name), countChars(name)   # Or return a dictionary
> if __name__ == '__main__':          # Added: self-test code
>     print(test('mymod.py'))         # When run, not when imported
> ```
> ```
> $ python3 mymod.py
> (13, 434)

> ```
> This is where you would probably begin to consider using command-line arguments or user input to provide the filename to be counted instead of hardcoding it in the script. Examples B-19 and B-20 show the required mods (see Chapters 21 and 25 for more on `sys.argv`, and Chapter 10 for more on `input`): **Example B-19.** `Part5/mymod_argv.py` (changed parts)

> ```python
> if __name__ == '__main__':
>     import sys                     # Command-line argument
>     print(test(sys.argv[1]))
> ```
> ```
> $ python3 mymod_argv.py mymod.py
> (13, 434)

> ```
> **Example B-20.** `Part5/mymod_input.py` (changed parts)

> ```python
> if __name__ == '__main__':
>     print(test(input('Enter file name: ')))   # Console/user input
> ```
> ```
> $ python3 mymod_input.py
> Enter file name: mymod.py (13, 434)

> ```

### 中文翻译

> **3. \_\_main\_\_**：只要编码得当，这个文件在两种模式下都能工作——作为程序运行或作为模块导入，如示例 B-18 及其后的 REPL 会话所示：
>
> ```python
> if __name__ == '__main__':          # 新增：自测代码
>     print(test('mymod.py'))         # 只在"被运行"时执行，导入时不执行
> ```
>
> ```
> $ python3 mymod.py
> (13, 434)
> ```
>
> 到了这一步，你可能开始考虑用命令行参数或用户输入来提供要计数的文件名，而不是在脚本里写死。示例 B-19 和 B-20 展示了所需的改动（`sys.argv` 更多见第 21、25 章；`input` 更多见第 10 章）：
>
> ```python
> # mymod_argv.py 改动部分
> if __name__ == '__main__':
>     import sys                     # 命令行参数
>     print(test(sys.argv[1]))
> ```
> ```
> $ python3 mymod_argv.py mymod.py
> (13, 434)
> ```
>
> ```python
> # mymod_input.py 改动部分
> if __name__ == '__main__':
>     print(test(input('Enter file name: ')))   # 控制台/用户输入
> ```
> ```
> $ python3 mymod_input.py
> Enter file name: mymod.py
> (13, 434)
> ```

### 代码分析（逐行解读）

```python
if __name__ == '__main__':      # __name__ 是每个模块的内置全局名：
                                # 直接运行时为 '__main__'，被 import 时为模块名（如 'mymod'）
    print(test('mymod.py'))     # 只有直接运行才执行——导入时这整块被跳过

# argv 版本：从命令行取文件名
    import sys                  # sys.argv[0] 是脚本名，sys.argv[1] 是第一个参数
    print(test(sys.argv[1]))    # python3 mymod_argv.py mymod.py

# input 版本：从控制台问用户
    print(test(input('Enter file name: ')))   # input() 读取一行作为文件名
```

### 深度理解

- **核心概念**：`if __name__ == '__main__':` 是 Python 的**自测（self-test）惯例**——同一文件既可当程序跑（执行自测代码），又可当库导入（安静）。这是 Python 模块设计的精华之一。
- **底层机制**：解释器执行脚本时把该模块命名为 `__main__`；`import` 时命名空间字典里的 `__name__` 是模块的导入名。因此判断 `__name__` 就能区分两种运行场景。
- **三个输入来源**：写死（简单）、`sys.argv`（命令行，`sys.argv[0]` 是脚本路径，参数从 1 开始）、`input()`（交互式询问，返回字符串）。
- **常见误区**：忘了判断直接打印测试输出——导入时也会执行，造成"副作用"；`sys.argv[1]` 在没有参数时越界报 IndexError（应加判断或 try）。

---

## 题 4. Nested imports（嵌套导入）

### 英文原文

> **4. Nested imports**: It's not much, but Example B-21 gives one solution and its results (the point here is to experiment with importing one module from another in a variety of ways): **Example B-21.** `Part5/myclient.py`

> ```python
> from mymod import countLines, countChars
> print(countLines('mymod.py'), countChars('mymod.py'))
> ```
> ```
> $ python3 myclient.py
> 13 434

> ```
> As for the rest of this question, `mymod`'s functions are accessible (that is, importable) from the top level of `myclient`, since `from` simply assigns to names in the importer (it works as if `mymod`'s `def`s appeared in `myclient`). For example, another file can say:

> ```python
> import myclient
> myclient.countLines(...)

> from myclient import countChars
> countChars(...)

> ```
> If `myclient` used `import` instead of `from`, you'd need to use a path to get to the functions in `mymod` through `myclient`:

> ```python
> import myclient
> myclient.mymod.countLines(...)

> from myclient import mymod
> mymod.countChars(...)

> ```
> In general, you can define **collector** modules that import all the names from other modules so they're available in a single convenience module. The following hypothetical code, for example, creates three different copies of the name `somename`—`mod1.somename`, `collector.somename`, and `__main__.somename`; all three share the same integer object initially, and only the name `somename` exists at the interactive prompt as is:

> ```python
> # File mod1.py (hypothetical)
> somename = 99
> # File collector.py (hypothetical)
> from mod1 import *     # Collect lots of names here
> from mod2 import *     # "from" assigns to my names
> from mod3 import *
> >> from collector import somename

> ```

### 中文翻译

> **4. 嵌套导入**：内容不多，示例 B-21 给出一个方案和它的结果（这里的重点是以多种方式实验"从一个模块导入另一个模块"）：
>
> ```python
> # myclient.py
> from mymod import countLines, countChars    # 导入特定名字
> print(countLines('mymod.py'), countChars('mymod.py'))
> ```
> ```
> $ python3 myclient.py
> 13 434
> ```
>
> 至于本问题其余部分：`mymod` 的函数可以从 `myclient` 的顶层访问（即可导入），因为 `from` 只是向导入方命名空间中的名字赋值（就像 `mymod` 的 `def` 语句出现在 `myclient` 里一样）。例如，另一个文件可以这样写：
> ```python
> import myclient
> myclient.countLines(...)        # 通过 myclient 访问
> from myclient import countChars
> countChars(...)                 # 或者把名字再导入进来
> ```
> 如果 `myclient` 用的是 `import` 而不是 `from`，你就需要通过 `myclient` 用路径访问 `mymod` 里的函数：
> ```python
> import myclient
> myclient.mymod.countLines(...)  # 路径式访问：myclient 模块里还有 mymod 这个属性
> from myclient import mymod
> mymod.countChars(...)
> ```
>
> 一般来说，你可以定义**收集器（collector）**模块，把其他模块的所有名字导入进来，使它们集中出现在一个便利模块中。例如下面这段假设代码会创建 `somename` 这个名字的三个不同副本——`mod1.somename`、`collector.somename` 和 `__main__.somename`；三者起初共享同一个整数对象，交互提示符下直接存在的只有 `somename` 这个名字：
>
> ```python
> # 文件 mod1.py（假设）
> somename = 99
>
> # 文件 collector.py（假设）
> from mod1 import *     # 在这里收集大量名字
> from mod2 import *     # "from" 把名字赋给我
> from mod3 import *
> >>> from collector import somename
> ```

### 代码分析（逐行解读）

```python
from mymod import countLines, countChars   # from：把 mymod 的这两个名字复制进 myclient 命名空间
print(countLines('mymod.py'), countChars('mymod.py'))   # 直接调用

# 另一文件用法
import myclient
myclient.countLines(...)        # myclient 命名空间里有 countLines（from 的效果）
from myclient import countChars # 还能进一步再导入

# 若 myclient 用 import mymod：
import myclient
myclient.mymod.countLines(...)  # 属性链：myclient 模块对象 → mymod 模块对象 → 函数
```

### 深度理解

- **核心概念**：`import` 引入"模块对象"作为属性；`from` 把"模块内名字"复制进当前命名空间。这决定了嵌套导入后访问路径的差异。
- **命名空间的本质**：模块就是名字到对象的字典；`from ... import ...` 就是"复制字典条目"。因此 `mymod` 的函数会"像长在 myclient 里"一样可用。
- **收集器模式**：聚合模块（collector）把多个模块的公共接口集中到一处，方便统一导入——大型库常这么做（如 `tkinter`、`matplotlib.pyplot` 的便利导出）。
- **同一对象多名字**：`mod1.somename`、`collector.somename`、`__main__.somename` 是三个名字，但指向同一个整数对象——"名字 ≠ 对象"的心智模型再次体现。
- **常见误区**：误以为 `from` 会复制对象（复制的是引用/名字）；在导入方修改 `from` 来的名字不会改原模块（名字重绑定）。

---

## 题 5. Package imports（包导入）

### 英文原文

> **5. Package imports**: For this, copy the `mymod.py` solution file listed for exercise 3 (Example B-18) into a directory package. The following commands run in a Unix console set up the directory and an optional `__init__.py` file; you'll need to interpolate for other platforms and tools (e.g., use `copy` and `notepad` on Windows instead of `cp` and `vi`). This works in any directory, and you can do some of this from a file-explorer GUI, too.

> When finished, you'll have a `mypkg` subdirectory that contains the files `__init__.py` and `mymod.py`. Technically, `mypkg` is located in the "home" directory component of the module search path. Notice how a `print` statement coded in the directory's initialization file fires only the first time it is imported, not the second. Raw strings (`r'...'`) can also avoid `\` escape issues in the file paths if you're working on Windows, but `/` works there too:

> ```
> $ mkdir mypkg                  # Windows: same
> $ cp mymod.py mypkg/mymod.py   # Windows: copy mymod.py mypkg\mymod.py
> $ vi mypkg/__init__.py         # Windows: notepad mypkg\__init__.py
> …code a print statement…

> $ python3                      # Windows: py -3 (probably)
> >> import mypkg.mymod initializing mypkg >> mypkg.mymod.countLines('mypkg/mymod.py') # Windows: same 13 >> from mypkg.mymod import countChars >> countChars('mypkg/mymod.py') # Windows: same 434

> ```
> If you copy the module to `__main__.py`, the copy will run if you run the directory as a whole (though there may be no reason to do so in practice, as the original module can be run directly too):

> ```
> $ cp mypkg/mymod.py mypkg/__main__.py    # Windows: copy
> $ python3 mypkg
> (13, 434)

> $ python3 mypkg/mymod.py
> (13, 434)

> ```

### 中文翻译

> **5. 包导入**：这个练习需要把练习 3 的 `mymod.py` 方案文件（示例 B-18）复制到一个目录包里。下面的命令在 Unix 控制台中运行，用来建立目录和一个可选的 `__init__.py` 文件；其他平台和工具需要自行替换（例如 Windows 上用 `copy` 和 `notepad` 代替 `cp` 和 `vi`）。这在任何目录里都成立，你也可以在文件资源管理器 GUI 里完成其中一部分。
>
> 完成后，你会有一个包含 `__init__.py` 和 `mymod.py` 的 `mypkg` 子目录。从技术上讲，`mypkg` 位于模块搜索路径的"home"目录部分。注意：在目录初始化文件中编写的 `print` 语句只在**第一次**导入时触发，第二次不会。在 Windows 上工作的话，原始字符串（`r'...'`）也可以避免文件路径中的 `\` 转义问题，不过那里用 `/` 也可以：
>
> ```
> $ mkdir mypkg                        # Windows: 相同
> $ cp mymod.py mypkg/mymod.py         # Windows: copy mymod.py mypkg\mymod.py
> $ vi mypkg/__init__.py               # Windows: notepad mypkg\__init__.py
> …在文件中编写一条 print 语句…
> $ python3                            # Windows: 用 py -3（通常）
> >>> import mypkg.mymod
> initializing mypkg                   # 第一次导入：__init__.py 被执行
> >>> mypkg.mymod.countLines('mypkg/mymod.py')   # Windows: 相同
> 13
> >>> from mypkg.mymod import countChars
> >>> countChars('mypkg/mymod.py')     # Windows: 相同
> 434                                  # 第二次导入：没有再次打印 initializing
> ```
>
> 如果把模块复制成 `__main__.py`，那么以目录整体运行时会执行这份副本（虽然实践中可能没理由这样做，因为原模块也可以直接运行）：
>
> ```
> $ cp mypkg/mymod.py mypkg/__main__.py    # Windows: copy
> $ python3 mypkg                          # 运行整个目录 → 执行 __main__.py
> (13, 434)
> $ python3 mypkg/mymod.py                 # 或直接运行模块文件
> (13, 434)
> ```

### 代码分析（逐行解读）

```text
mkdir mypkg                    # 创建包目录
cp mymod.py mypkg/mymod.py     # 把模块复制进去
vi mypkg/__init__.py           # 创建（可选）初始化文件，内容如 print('initializing mypkg')
python3
>>> import mypkg.mymod         # 导入链：先 import 包 mypkg → 执行 __init__.py → 打印一次
                               # 再 import 子模块 mypkg.mymod → 执行 mymod.py
>>> mypkg.mymod.countLines('mypkg/mymod.py')   # 属性路径访问：包.模块.函数
>>> from mypkg.mymod import countChars         # 从深层模块导入名字
```

### 深度理解

- **核心概念**：包（package）= 含 `__init__.py` 的目录。`import mypkg.mymod` 会**先**执行 `__init__.py`（初始化包），**再**执行 `mymod.py`。
- **为什么 initializing 只打印一次**：模块与包都缓存进 `sys.modules`，第二次 `from mypkg.mymod import ...` 直接取缓存，`__init__.py` 不再执行——这与 Part I 练习 3 的模块缓存是同一个机制。
- **`__init__.py` 的职责**：包级初始化、`__all__` 导出控制、把子模块名字上提（`from .mymod import countLines` 等）。
- **`__main__.py`**：目录作为整体被 `python3 mypkg` 运行时执行的入口文件。
- **Windows 路径**：`\` 在普通字符串里是转义符，用 `r'C:\...'` 或 `/`（Windows 也接受正斜杠）。
- **常见误区**：忘记创建 `__init__.py`（3.3+ 的命名空间包除外）；以为 `import mypkg.mymod` 后可以直接写 `countLines`（还需 `from` 或属性路径）；以为每次 import 都重跑包初始化。

---

## 题 6. Reload（重载）

### 英文原文

> **6. Reloads**: This exercise just asks you to experiment with changing the `changer.py` example in the book's Example 23-10, so there's nothing to show here.

### 中文翻译

> **6. 重载**：这个练习只是让你实验性地修改书中示例 23-10 的 `changer.py` 例子，所以这里没有需要展示的内容。

### 深度理解

- **核心概念**：`importlib.reload(module)`（旧版是内置 `reload`）重新执行模块代码——开发期"改完代码立即在 REPL 里生效"的利器。
- **要点**：`reload` 重跑的是模块体，已有引用旧对象的名字不会自动更新；`from ... import 名字` 与 `reload` 混用是经典的"改了个寂寞"陷阱。
- **最佳实践**：改动模块后，要么 `reload` 该模块，要么重启解释器；使用 `from` 导入的名字需重新执行 `from`。

---

## 题 7. Circular imports（循环导入）

### 英文原文

> **7. Circular imports**: The short story is that importing `recur2` first works because the recursive import then happens at the `import` in `recur1`, not at a `from` in `recur2`.
>
> The long story goes like this: importing `recur2` first works because the recursive import from `recur1` to `recur2` fetches `recur2` as a whole instead of getting specific names. `recur2` is incomplete when it's imported from `recur1`, but because it uses `import` instead of `from`, you're safe: Python finds and returns the already created `recur2` module object and continues to run the rest of `recur1` without a glitch.
>
> When the `recur2` import resumes, the second `from` finds the name `Y` in `recur1` (it's been run completely), so no error is reported.
>
> Running a file as a **script** is not the same as importing it as a module; these cases are the same as running the first `import` or `from` in the script interactively. For instance, running `recur1` as a script works because it is the same as importing `recur2` interactively, as `recur2` is the first module imported in `recur1`. Running `recur2` as a script fails for the same reason—it's the same as running its first import interactively.

### 中文翻译

> **7. 循环导入**：简短版：先导入 `recur2` 能成功，是因为递归导入发生在 `recur1` 里的 `import` 处，而不是 `recur2` 里的 `from` 处。
>
> 详细版是这样的：先导入 `recur2` 能成功，是因为从 `recur1` 到 `recur2` 的递归导入是**整体获取** `recur2` 模块对象，而不是获取特定名字。`recur2` 在被 `recur1` 导入时是不完整的，但因为它用的是 `import` 而不是 `from`，所以你是安全的：Python 找到并返回已创建的 `recur2` 模块对象，继续毫无障碍地运行 `recur1` 的其余部分。当 `recur2` 的导入恢复执行时，第二个 `from` 能在 `recur1` 中找到名字 `Y`（它已完整运行），因此不会报错。
>
> 把文件作为**脚本**运行与把它作为模块导入不是一回事；这些情况等同于在交互模式下运行脚本中的第一条 `import` 或 `from`。例如，把 `recur1` 当脚本运行可以成功，因为它等同于交互式导入 `recur2`——因为 `recur2` 是 `recur1` 中第一个被导入的模块。把 `recur2` 当脚本运行失败也是同样的原因——它等同于交互式执行它的第一条导入语句。

### 深度理解

- **核心概念**：循环导入（A 导 B、B 导 A）的成败取决于**导入时刻的模块完成度**与**导入方式**。
- **底层机制**：`import` 的第一步是"找到模块 → 创建模块对象 → 放入 sys.modules → 执行模块体"。递归发生时，Python 会在 `sys.modules` 里发现"半成品"模块对象并直接返回它（不再重复执行）——所以 `import` 整体导入安全；而 `from recur1 import Y` 在 B 的顶层立刻取值，若此时 `recur1` 还没执行到定义 `Y` 的那行，就会 `ImportError`/`AttributeError`。
- **为什么脚本运行与导入不同**：脚本运行 = 模块以 `__main__` 身份从头执行；谁先导入谁决定了顺序与成败。
- **实战经验**：设计模块时避免循环依赖；实在需要时——把 `from` 挪进函数体（延迟到调用时）、或用 `import module` + `module.attr` 形式访问。
- **常见误区**：以为"循环导入总是错误"——它只在"时机不巧 + 用 from"时才会爆雷；同理，REPL 里手动按序导入往往掩盖了问题。

---

# Part VI：Classes and OOP（类与面向对象）

### 英文原文

> Part VI, Classes and OOP
> See "Test Your Knowledge: Part VI Exercises" in Chapter 32 for the exercises.

### 中文翻译

> 第六部分：类与面向对象。练习见第 32 章的 "Test Your Knowledge: Part VI Exercises"。

### 深度理解

- **核心概念**：Part VI 练习覆盖继承、运算符重载、子类化、属性拦截方法、包装/代理类（wrapper）、类树（class tree）、组合（composition）与多态分派。
- **练习主线**：亲手实现"加法家族"（Adder）、"列表包装器"（MyList）、"集合包装器"（Set/MultiSet）、"消息路由"（Lunch）、"动物分类树"（zoo）——每一个都是真实设计模式的迷你版。

---

## 题 1. Inheritance（继承）

### 英文原文

> **1. Inheritance**: Example B-22 lists a solution for this exercise, along with some interactive tests. The `__add__` overload has to appear only once, in the superclass, as it invokes type-specific `add` methods in subclasses: **Example B-22.** `Part6/adder.py`

> ```python
> class Adder:
>     def add(self, x, y):
>         print('not implemented!')
>     def __init__(self, start=[]):
>         self.data = start
>     def __add__(self, other):           # Or in subclasses?
>         return self.add(self.data, other)   # Or return type?
> class ListAdder(Adder):
>     def add(self, x, y):
>         return x + y
> class DictAdder(Adder):
>     def add(self, x, y):
>         new = {}
>         for k in x.keys(): new[k] = x[k]
>         for k in y.keys(): new[k] = y[k]
>         return new
> ```
> ```
> $ python3
> >> from adder import * >> x = Adder() >> x.add(1, 2) not implemented!

> >> x = ListAdder() >> x.add([1], [2]) [1, 2] >> x = DictAdder() >> x.add({1: 1}, {2: 2}) {1: 1, 2: 2} >> x = Adder([1]) >> x + [2] not implemented!

> >> >> x = ListAdder([1]) >> x + [2] [1, 2] >> [2] + x TypeError: can only concatenate list (not "ListAdder") to list

> ```
> Notice in the last test that you get an error for expressions where a class instance appears on the right of a `+`; if you want to fix this, use `__radd__` methods, as described in Chapter 30.

> If you are saving a value in the instance anyhow, you might as well rewrite the `add` method to take just one argument, in the spirit of other examples in this part of the book. Example B-23 sketches this mutation: **Example B-23.** `Part6/adder2.py`

> ```python
> class Adder:
>     def __init__(self, start=[]):
>         self.data = start
>     def __add__(self, other):           # Pass a single argument
>         return self.add(other)          # The left side is in self
>     def add(self, y):
>         print('not implemented!')
> class ListAdder(Adder):
>     def add(self, y):
>         return self.data + y
> class DictAdder(Adder):
>     def add(self, y):
>         d = self.data.copy()            # Change to use self.data instead of x
> d.update(y) # Or "cheat" by using quicker built-ins

>         return d
> x = ListAdder([1, 2, 3])
> y = x + [4, 5, 6]
> print(y)                                # Prints [1, 2, 3, 4, 5, 6]
> z = DictAdder(dict(name='x')) + {'a': 1}
> print(z)                                # Prints {'name': 'x', 'a': 1}
> ```
> Because values are attached to objects rather than passed around, this version is arguably more object-oriented. And, once you've gotten to this point, you'll probably find that you can get rid of `add` altogether and simply define type-specific `__add__` methods in the two subclasses.

### 中文翻译

> **1. 继承**：示例 B-22 给出了本练习的一个方案，并附上一些交互式测试。`__add__` 重载只需要在超类中出现一次，因为它调用的是子类中**类型特有**的 `add` 方法：
>
> ```python
> class Adder:                        # 超类：定义"骨架"
>     def add(self, x, y):
>         print('not implemented!')   # 占位实现——子类必须覆写
>     def __init__(self, start=[]):
>         self.data = start
>     def __add__(self, other):       # 或者在子类中定义？
>         return self.add(self.data, other)   # 或者返回类型？
>
> class ListAdder(Adder):
>     def add(self, x, y):
>         return x + y                # 列表拼接
>
> class DictAdder(Adder):
>     def add(self, x, y):
>         new = {}
>         for k in x.keys(): new[k] = x[k]    # 逐键复制 x
>         for k in y.keys(): new[k] = y[k]    # 再复制 y（键重复则 y 覆盖）
>         return new
> ```
>
> ```
> >>> x = Adder()
> >>> x.add(1, 2)          → not implemented!（基类占位实现）
> >>> x = ListAdder()
> >>> x.add([1], [2])      → [1, 2]（子类覆写后生效）
> >>> x = DictAdder()
> >>> x.add({1: 1}, {2: 2}) → {1: 1, 2: 2}
> >>> x = Adder([1])
> >>> x + [2]              → not implemented!（基类 add 未覆写）
> >>> x = ListAdder([1])
> >>> x + [2]              → [1, 2]（__add__ 调 self.add → 子类实现）
> >>> [2] + x              → TypeError（实例在 + 右侧，list 不认识它）
> ```
>
> 注意最后一个测试：当类实例出现在 `+` 的右侧时你会得到错误；想修复它，就按第 30 章的说明使用 `__radd__` 方法。
>
> 反正你都要在实例中保存值，那不如把 `add` 方法改写成只接收一个参数，与本书该部分的其他示例风格一致。示例 B-23 勾勒了这个改造：
>
> ```python
> class Adder:
>     def __init__(self, start=[]):
>         self.data = start
>     def __add__(self, other):       # 只传一个参数
>         return self.add(other)      # 左侧对象在 self 里
>     def add(self, y):
>         print('not implemented!')
>
> class ListAdder(Adder):
>     def add(self, y):
>         return self.data + y        # 状态存于 self.data
>
> class DictAdder(Adder):
>     def add(self, y):
>         d = self.data.copy()        # 复制自身数据（浅拷贝）
>         d.update(y)                 # 或"作弊"用更快的内置
>         return d
>
> x = ListAdder([1, 2, 3])
> y = x + [4, 5, 6]                  # 打印 [1, 2, 3, 4, 5, 6]
> z = DictAdder(dict(name='x')) + {'a': 1}    # 打印 {'name': 'x', 'a': 1}
> ```
>
> 因为值被附着在对象上而不是传来传去，这个版本可以说更符合面向对象精神。而且，一旦到了这一步，你可能会发现 `add` 方法可以整个删掉，直接在两个子类里定义类型特异的 `__add__` 方法。

### 代码分析（逐行解读）

```python
class Adder:                          # 基类 = 模板方法（template method）模式
    def add(self, x, y):
        print('not implemented!')     # "钩子"：子类覆写后真正执行
    def __init__(self, start=[]):     # 注意：可变默认值 [] 是共享陷阱（见下）
        self.data = start
    def __add__(self, other):         # 运算符重载只写一次，在超类
        return self.add(self.data, other)   # 动态分派：self.add 会找到子类的实现

class ListAdder(Adder):
    def add(self, x, y):
        return x + y                  # 列表：拼接

class DictAdder(Adder):
    def add(self, x, y):
        new = {}
        for k in x.keys(): new[k] = x[k]    # 复制 x 的所有条目
        for k in y.keys(): new[k] = y[k]    # 追加 y 的条目（同键覆盖）
        return new
```

- `x + [2]` 的求值链：`x.__add__([2])` →（继承自 Adder）→ `self.add(self.data, [2])` → 沿 MRO 找到 `ListAdder.add` → `[1] + [2]`。
- `[2] + x`：`list.__add__(x)` 不认识 ListAdder → 抛 TypeError。补救：定义 `__radd__`。

### 深度理解

- **核心概念**：继承 + 方法覆写 + 动态分派（dynamic dispatch）组成"模板方法"设计模式——骨架在超类定一次，细节在子类各自实现。
- **底层机制**：`self.add(...)` 是属性查找：沿 `self.__class__` 的 MRO（方法解析顺序）从子类向父类找 `add`。这就是"多态"在类层面的实现——同一行代码、不同对象、不同行为。
- **运算符重载的放置**：`__add__` 只需在超类定义一次，因为 `self.add` 是虚调用（virtual call），子类覆写 `add` 即可让 `+` 自动分派——少写代码、统一契约。
- **为什么 `[2] + x` 失败**：`+` 左侧优先使用左侧类型的 `__add__`；左侧是 list，它的 `__add__` 只接受 list。右侧补救用 `__radd__`（reflected addition，反射加法），它只在左侧类型拒绝时才被调用。
- **可变默认值陷阱**：`def __init__(self, start=[])` 中 `[]` 在定义时求值一次、被所有实例共享——这里只读（被重新赋值）问题不大，但若原地修改会"串味"。官方建议用 `start=None` 再在函数体内赋新列表。
- **版本演进**：adder2.py 把状态收进 `self.data`、`add` 只收一个参数——"左操作数即 self"，更 OOP；作者甚至提示可以完全去掉 `add`，直接在各子类定义 `__add__`。
- **常见误区**：忘了在子类覆写 `add` 导致静默输出 "not implemented!"；把运算符重载写在子类造成重复代码；忽略 `__radd__` 导致右侧运算崩。

---

## 题 2. Operator overloading（运算符重载：包装列表）

### 英文原文

> **2. Operator overloading**: The solution code and its REPL results in Example B-24 demo a handful of operator-overloading methods we explored in Chapter 30. Copying the initial value in the constructor is important because it may be mutable; you don't want to change or have a reference to an object that's possibly shared somewhere outside the class. The `__getattr__` method routes calls to the wrapped list.
>
> For tips on a possibly easier way to code this, see "Extending Types by Subclassing" in Chapter 32: **Example B-24.** `Part6/mylist.py`

> ```python
> class MyList:
>     def __init__(self, start):
>         #self.wrapped = start[:]      # Copy start: no side effects
>         self.wrapped = list(start)    # Make sure it's a list here
>     def __add__(self, other):
>         return MyList(self.wrapped + other)
>     def __mul__(self, time):
>         return MyList(self.wrapped * time)
>     def __getitem__(self, offset):    # Also passed a slice on [:]
>         return self.wrapped[offset]   # For iteration if no __iter__
>     def __len__(self):
>         return len(self.wrapped)      # Also fallback for truth tests
>     def append(self, node):
>         self.wrapped.append(node)
>     def __getattr__(self, name):      # Other methods: sort/reverse/etc.
>         return getattr(self.wrapped, name)
>     def __repr__(self):               # Catchall display method
>         return repr(self.wrapped)
> if __name__ == '__main__':
>     x = MyList('hack')
>     print(x)                          # ['h', 'a', 'c', 'k']
>     print(x[2])                       # c
>     print(x[1:])                      # ['a', 'c', 'k']
>     print(x + ['code'])               # ['h', 'a', 'c', 'k', 'code']
>     print(x * 3)                      # ['h','a','c','k'] * 3
> x.append('1'); x.extend(['z']) # extend 走 __getattr__ x.sort() # sort 走 __getattr__

>     print(' '.join(c for c in x))     # 迭代：1 a c h k z
> ```
> ```
> $ python3 mylist.py
> ['h', 'a', 'c', 'k'] c ['a', 'c', 'k'] ['h', 'a', 'c', 'k', 'code'] ['h', 'a', 'c', 'k', 'h', 'a', 'c', 'k', 'h', 'a', 'c', 'k'] 1 a c h k z

> ```
> Note that it's also important to copy the start value by calling `list` instead of slicing here, because otherwise the result may not be a true `list`, and so will not respond to expected list methods, such as `append` (e.g., slicing a string returns another string, not a list).
>
> You would be able to copy a `MyList` start value by slicing because its class overloads the slicing operation and provides the expected list interface; however, you need to avoid slice-based copying for objects such as strings.

### 中文翻译

> **2. 运算符重载**：示例 B-24 中的解决方案代码及其 REPL 结果演示了我们在第 30 章探讨过的一批运算符重载方法。在构造函数里**复制**初始值很重要，因为它可能是可变的——你不希望改动或引用一个可能在类外部某处被共享的对象。`__getattr__` 方法把调用路由到被包装的列表。关于更简单的实现提示，参见第 32 章的 "Extending Types by Subclassing"（通过子类化扩展类型）：
>
> ```python
> class MyList:                        # 包装器（wrapper）：包裹一个真正 list
>     def __init__(self, start):
>         #self.wrapped = start[:]     # 用切片复制 start：无副作用
>         self.wrapped = list(start)   # 确保这里是个 list
>     def __add__(self, other):
>         return MyList(self.wrapped + other)    # 返回 MyList 保持链式
>     def __mul__(self, time):
>         return MyList(self.wrapped * time)
>     def __getitem__(self, offset):   # 切片 [:] 也会传 slice 对象进来
>         return self.wrapped[offset]  # 无 __iter__ 时 for 循环也靠它
>     def __len__(self):
>         return len(self.wrapped)     # 真值测试的兜底
>     def append(self, node):
>         self.wrapped.append(node)    # 显式代理
>     def __getattr__(self, name):     # 其余方法：sort/reverse 等都转发
>         return getattr(self.wrapped, name)
>     def __repr__(self):              # 显示兜底方法
>         return repr(self.wrapped)
>
> if __name__ == '__main__':           # 自测代码
>     x = MyList('hack')
>     print(x)           # ['h', 'a', 'c', 'k']
>     print(x[2])        # c
>     print(x[1:])       # ['a', 'c', 'k']
>     print(x + ['code'])  # ['h', 'a', 'c', 'k', 'code']
>     print(x * 3)       # ['h','a','c','k'] 重复 3 次
>     x.append('1'); x.extend(['z'])   # extend 通过 __getattr__ 转发
>     x.sort()           # sort 通过 __getattr__ 转发
>     print(' '.join(c for c in x))    # 迭代 x → 1 a c h k z（sort 后顺序）
> ```
>
> ```
> $ python3 mylist.py
> ['h', 'a', 'c', 'k']
> c
> ['a', 'c', 'k']
> ['h', 'a', 'c', 'k', 'code']
> ['h', 'a', 'c', 'k', 'h', 'a', 'c', 'k', 'h', 'a', 'c', 'k']
> 1 a c h k z
> ```
>
> 注意：这里用 `list` 而不是切片来复制 start 值也很重要，否则结果可能不是真正的 `list`，因此无法响应预期的列表方法（比如 `append`）（例如，切片一个字符串得到的是另一个字符串，而不是列表）。对 `MyList` 的 start 值你倒是可以放心用切片复制，因为它的类重载了切片操作、提供了预期的列表接口；但对字符串这类对象，你需要避免基于切片的复制。

### 代码分析（逐行解读）

```python
class MyList:                          # "包装器/代理"类：实例内部藏一个真 list
    def __init__(self, start):
        self.wrapped = list(start)     # list() 强制转换：start 是字符串→字符列表；
                                       # start 是 MyList→走其迭代协议；start 是列表→浅复制
    def __add__(self, other):
        return MyList(self.wrapped + other)   # + 返回新 MyList，可继续链式运算
    def __mul__(self, time):
        return MyList(self.wrapped * time)    # * 重复拼接
    def __getitem__(self, offset):
        return self.wrapped[offset]   # 索引与切片都走这里（切片时 offset 是 slice 对象）
    def __len__(self):
        return len(self.wrapped)      # len() 与真值测试（bool 兜底）
    def append(self, node):
        self.wrapped.append(node)     # 少数显式提供的方法
    def __getattr__(self, name):      # 属性找不到时才调用！
        return getattr(self.wrapped, name)   # 把一切未知方法/属性转发给内部列表
    def __repr__(self):
        return repr(self.wrapped)     # 交互/打印时显示内部列表

# 测试链：
x = MyList('hack')      # list('hack') → ['h','a','c','k']
x[1:]                   # __getitem__(slice(1,None)) → ['a','c','k']
x + ['code']            # __add__ → MyList(['h','a','c','k','code'])
x * 3                   # __mul__ → MyList(列表重复 3 次)
x.extend(['z'])         # MyList 没定义 extend → __getattr__ → 转发给 list.extend
x.sort()                # 同样转发；sort 后 ['1','a','c','h','k','z']
' '.join(c for c in x)  # for 循环没有 __iter__，退而求其次用 __getitem__(0,1,2,...)
```

### 深度理解

- **核心概念**：**包装（wrapper）/ 代理（proxy）模式**——类持有一个内部对象，对外重定义核心操作，其余操作通过 `__getattr__` 全自动转发。这是 Python 实现"安全子类化之外的扩展"的经典手段。
- **`__getattr__` 只兜"找不到"的属性**：MyList 自己定义了 `append`、`__add__` 等，这些不会走 `__getattr__`；只有 `extend`、`sort`、`reverse` 等未定义的才转发。注意 `__getattr__` 对**内建隐式操作**（如 `+`、`len()` 不走它）——它们直接查类型槽，这也是本部分练习 4 的主题。
- **为什么 `list(start)` 而不是 `start[:]`**：切片返回"同类型"——`'hack'[:]` 是字符串，没有 `append`；`list()` 保证结果一定是 list（字符串→字符列表、元组→列表、列表→浅拷贝）。
- **为什么构造函数要复制**：`start` 可能是调用方仍在用的可变对象；不复制的话内部与外部共享同一对象，外部改动会"泄漏"进来。
- **迭代的兜底机制**：类没有 `__iter__` 时，`for x in obj` 会退化为"反复 `__getitem__(0)、[1]、[2]...` 直到 IndexError"——这是 Python 的"迭代协议退路"。
- **常见误区**：在 `__getattr__` 里访问自身不存在的属性造成无限递归；忘了 `__repr__` 导致打印 `<MyList object at ...>`；用切片复制字符串导致内部不是 list。

---

## 题 3. Subclassing（子类化：带统计的 MyListSub）

### 英文原文

> **3. Subclassing**: One solution appears in Example B-25; your solution will be similar. You can also use `super` here instead of explicit superclass names for methods and attributes, as partly noted in the code's comments: **Example B-25.** `Part6/mysub.py`

> ```python
> from mylist import MyList
> class MyListSub(MyList):
>     calls = 0                       # Shared by instances
>     def __init__(self, start):
>         self.adds = 0               # Varies in each instance
> MyList.__init__(self, start) # Or: super().__init__(start)

>     def __add__(self, other):
>         print('add: ' + str(other))
> MyListSub.calls += 1 # Class-wide counter

>         self.adds += 1              # Per-instance counts
>         return MyList.__add__(self, other)   # Or: super().__add__(other)
>     def stats(self):
>         return self.calls, self.adds    # All adds, my adds
> if __name__ == '__main__':
>     x = MyListSub('read')
>     y = MyListSub('code')
>     print(x[2])                     # e
>     print(x[1:])                    # ['e', 'a', 'd']
>     print(x + ['lp6e'])             # add: ['lp6e']  ['r','e','a','d','lp6e']
>     print(x + ['book'])             # add: ['book']  ...
>     print(y + ['py312'])            # add: ['py312'] ...
>     print(x.stats())                # (3, 2)
> ```
> ```
> $ python3 mysub.py
> e ['e', 'a', 'd'] add: ['lp6e'] ['r', 'e', 'a', 'd', 'lp6e'] add: ['book'] ['r', 'e', 'a', 'd', 'book'] add: ['py312'] ['c', 'o', 'd', 'e', 'py312'] (3, 2)

> ```

### 中文翻译

> **3. 子类化**：一种方案见示例 B-25；你的方案会与之类似。这里你也可以用 `super` 代替显式写出超类名来访问方法和属性，代码注释中部分提及：
>
> ```python
> class MyListSub(MyList):            # 继承 MyList 的包装功能
>     calls = 0                       # 类变量：所有实例共享
>     def __init__(self, start):
>         self.adds = 0               # 实例变量：每个实例独立
>         MyList.__init__(self, start)     # 或 super().__init__(start)：先初始化父类部分
>     def __add__(self, other):
>         print('add: ' + str(other))
>         MyListSub.calls += 1        # 类级计数器（所有实例共用一个）
>         self.adds += 1              # 实例级计数器
>         return MyList.__add__(self, other)   # 或 super().__add__(other)：复用父类逻辑
>     def stats(self):
>         return self.calls, self.adds    # (总加法次数, 本实例加法次数)
> ```
>
> ```
> >>> x = MyListSub('read')
> >>> x[2]          → e（继承自 MyList 的 __getitem__）
> >>> x[1:]         → ['e', 'a', 'd']
> >>> x + ['lp6e']  → add: ['lp6e'] 然后 ['r', 'e', 'a', 'd', 'lp6e']
> >>> x.stats()     → (3, 2)（全局 3 次 +，x 自己 2 次）
> ```

### 代码分析（逐行解读）

```python
class MyListSub(MyList):          # 子类继承 MyList 的全部接口
    calls = 0                     # 类属性：定义在类体里，实例共享一个对象
    def __init__(self, start):
        self.adds = 0             # 实例属性：self 上各自独立
        MyList.__init__(self, start)   # 显式调用父类构造器（或 super().__init__(start)）
    def __add__(self, other):
        print('add: ' + str(other))    # 覆写 +：先打印再委托父类
        MyListSub.calls += 1      # 类级计数：每任何实例的 + 都 +1
        self.adds += 1            # 实例级计数：只记本实例
        return MyList.__add__(self, other)   # 委托：父类 __add__ 执行真正的加法
    def stats(self):
        return self.calls, self.adds   # 注意 self.calls：实例找不到才沿类找 → 类变量
```

### 深度理解

- **核心概念**：**类变量 vs 实例变量**——`calls` 定义在类体（被所有实例共享，`MyListSub.calls` 与 `x.calls` 起初指向同一整数对象）；`adds` 在 `__init__` 里用 `self.adds` 创建（每实例一份）。属性查找顺序：实例字典 → 类 → 基类。
- **`+=` 与共享的微妙处**：`MyListSub.calls += 1` 是"读类变量 → 加一 → 写回类"；`self.adds += 1` 是"读实例属性 → 写回实例属性"——因为 `self.adds` 在实例字典里已有，不会污染类。若对类变量用 `self.calls += 1` 则会在实例上创建新属性、遮蔽类变量（经典陷阱）。
- **委托父类**：覆写 `__add__` 后显式 `MyList.__add__(self, other)`（或 `super().__add__(other)`）复用父类逻辑——"覆写 + 委托"是子类化的标准姿势。
- **为什么要调父类 `__init__`**：父类构造器负责设置 `self.wrapped`；子类不调用它，包装列表就不存在。
- **输出分析**：三次 `+`（x 两次、y 一次）→ `calls=3`；x 自身 `adds=2` → `stats()` 返回 `(3, 2)`。
- **常见误区**：忘记调用父类 `__init__`；用 `self.calls += 1` 意外创建实例属性；以为类变量"每个实例一份"。

---

## 题 4. Attribute methods（属性拦截方法）

### 英文原文

> **4. Attribute methods**: The following works through this exercise. As noted in Chapter 28 and elsewhere, `__getattr__` is *not* called for built-in operations in Python 3.X, so the expressions aren't intercepted at all here; a class like this must somehow redefine `__X__` operator-overloading methods explicitly.

> You can find more on this limitation in Chapters 28, 31, 32, and 38, as well as workarounds for it in Chapter 39 and its inheritance special case in Chapter 40. Its impacts are potentially broad but can be addressed with code:

> ```
> $ python3
> >> class Attrs:

> ...     def __getattr__(self, name):
> ...         print('get:', name)
> ...     def __setattr__(self, name, value):
> ...         print('set:', name, value)
> >> x = Attrs() >> x.append get append >> x.lang = 'py312'set: lang py312 >> x + 2 TypeError: unsupported operand type(s) for +: 'Attrs' and 'int'>> x[1] TypeError: 'Attrs' object is not subscriptable >> x[1:5] TypeError: 'Attrs' object is not subscriptable

> ```

### 中文翻译

> **4. 属性方法**：下面是对这个练习的完整演练。如第 28 章等处所述，在 Python 3.X 中，`__getattr__` **不会**为内置运算（built-in operations）调用，所以这里的表达式完全不会被拦截；像这样的类必须显式重定义 `__X__` 形式的运算符重载方法。关于这个局限的更多内容见第 28、31、32、38 章，它的变通方案见第 39 章，以及它在第 40 章中的继承特例。其影响可能很广，但都可以用代码应对：
>
> ```
> >>> class Attrs:
> ...     def __getattr__(self, name):
> ...         print('get:', name)         # 拦截"读不存在的属性"
> ...     def __setattr__(self, name, value):
> ...         print('set:', name, value)  # 拦截"所有属性赋值"
> >>> x = Attrs()
> >>> x.append
> get append                              # 属性查找失败 → __getattr__ 被调用
> >>> x.lang = 'py312'
> set: lang py312                         # 所有赋值都经过 __setattr__
> >>> x + 2
> TypeError: unsupported operand type(s) for +: 'Attrs' and 'int'   # 没定义 __add__，也没走 __getattr__
> >>> x[1]
> TypeError: 'Attrs' object is not subscriptable                    # 没定义 __getitem__
> >>> x[1:5]
> TypeError: 'Attrs' object is not subscriptable                    # 同样
> ```

### 代码分析（逐行解读）

```python
class Attrs:
    def __getattr__(self, name):        # 仅当普通查找（实例→类→基类）全部失败时调用
        print('get:', name)
    def __setattr__(self, name, value): # 任何 self.name = value 赋值都调用
        print('set:', name, value)

x = Attrs()
x.append          # 'append' 在实例/类/基类都不存在 → __getattr__ → 打印 get: append
x.lang = 'py312'  # 赋值 → __setattr__ → 打印 set: lang py312
x + 2             # + 是内建运算：直接查类型槽 __add__；Attrs 没定义 →
                  # TypeError（__getattr__ 完全不参与！）
x[1]              # 索引也是内建运算：查 __getitem__ → 没定义 → TypeError
x[1:5]            # 切片同样
```

### 深度理解

- **核心概念**：Python 3.X 中属性拦截有两套独立机制——**属性访问**（`x.name`）走 `__getattr__`/`__setattr__`；**内建运算符**（`+`、`[]`、`len()` 等）走**类型槽**（slot，即 `__add__`、`__getitem__` 等）。两者互不相通。
- **为什么这样设计**：性能考量——内建操作走 C 级快速路径（类型槽直接在类型对象上），不经过 Python 级的方法查找；若都走 `__getattr__` 会拖慢所有内建操作。
- **影响**：像 `__getattr__` 那样的"万能代理类"无法靠它拦截 `+` 与索引——必须在类里显式定义 `__add__`、`__getitem__` 等。这是实现"全功能代理"（如 RPyC、mock 库）时绕不开的工作量，第 39 章给出一些变通。
- **`__setattr__` 的递归陷阱**：在 `__setattr__` 里写 `self.name = value` 会无限递归——必须用 `object.__setattr__(self, name, value)` 或 `self.__dict__[name] = value`。
- **常见误区**：以为 `__getattr__` 能拦截一切；以为定义了 `__getattr__` 后 `+` 也会被打印。

---

## 题 5. Set objects（集合对象）

### 英文原文

> **5. Set objects**: Here's the sort of interaction you should get. To make the import of `Chapter32/setwrapper.py` work, either run this in the folder where this file resides, copy this file to your working directory, or add this file's folder to your import search path per Part V. Comments explain which methods are called. Also, bear in mind that sets are a built-in type in Python, so this is mostly just a coding exercise (see Chapter 5 for more on sets):

> ```
> $ python3
> >> from setwrapper import Set >> x = Set([1, 2, 3, 4]) # Runs __init__ >> y = Set([3, 4, 5]) >> x & y # __and__, intersect, then __repr__ Set:[3, 4] >> x | y # __or__, union, then __repr__ Set:[1, 2, 3, 4, 5] >> z = Set('hello') # __init__ removes duplicates >> z[0], z[-1], z[2:] # __getitem__ ('h', 'o', ['l', 'o']) >> for c in z: print(c, end=' ') # __iter__ (else __getitem__) h e l o >> ''.join(c.upper() for c in z) # __iter__ (else __getitem__)'HELO'>> len(z), z # __len__, __repr__ (4, Set:['h', 'e', 'l', 'o']) >> z & 'mello', z | 'mello'(Set:['e', 'l', 'o'], Set:['h', 'e', 'l', 'o', 'm'])

> ```
> A solution to the multiple-operand extension subclass looks like the class in Example B-26. It needs to replace only two methods in the original set. The class's documentation string explains how it works: **Example B-26.** `Part6/multiset.py`

> ```python
> from setwrapper import Set
> class MultiSet(Set):
> """Inherits all Set names, but extends intersect and union to support multiple operands. Note that "self" is still the first argument (stored in the *args argument now). Also note that the inherited & and | operators call the new methods here with 2 arguments, but processing more than 2 requires a method call, not an expression. intersect doesn't remove duplicates here: the Set constructor does.

> """

>     def intersect(self, *others):
>         res = []
>         for x in self:              # Scan first sequence
>             for other in others:    # For all other args
>                 if x not in other: break   # Item in each one?
>             else:                   # No: break out of loop
> res.append(x) # Yes: add item to end

>         return Set(res)
>     def union(*args):               # self is args[0]
>         res = []
>         for seq in args:            # For all args
>             for x in seq:           # For all nodes
>                 if not x in res:
> res.append(x) # Add new items to result

>         return Set(res)
> ```
> Your interaction with this extension will look something like the following. Note that you can intersect by using `&` or calling `intersect`, but you must call `intersect` for three or more operands; `&` is a binary (two-sided) operator. Also, note that we could have called `MultiSet` simply `Set` to make this change more transparent if we used `setwrapper.Set` to refer to the original within `multiset` (the `as` clause in an import could rename the class too if desired):

> ```
> >> from multiset import * >> x = MultiSet([1, 2, 3, 4]) >> y = MultiSet([3, 4, 5]) >> z = MultiSet([0, 1, 2]) >> x & y, x | y # Two operands (Set:[3, 4], Set:[1, 2, 3, 4, 5]) >> x.intersect(y, z) # Three operands Set:[] >> x.union(y, z) Set:[1, 2, 3, 4, 5, 0] >> x.intersect([1,2,3], [2,3,4], [1,2,3]) # Four operands Set:[2, 3] >> x.union(range(10)) # Non-MultiSets work, too Set:[1, 2, 3, 4, 0, 5, 6, 7, 8, 9] >> w = MultiSet('soap') # String sets >> w Set(['s', 'o', 'a', 'p']) >> ''.join(w | 'super')'soapuer'>> (w | 'super') & MultiSet('slots') Set(['s', 'o'])

> ```

### 中文翻译

> **5. 集合对象**：下面是你会得到的交互结果。要让 `Chapter32/setwrapper.py` 的导入生效，要么在它所在的文件夹里运行，要么把它复制到你的工作目录，要么按第五部分的方法把它的文件夹加进导入搜索路径。注释解释了调用了哪些方法。同时记住：集合是 Python 的内置类型，所以这基本只是个编码练习（集合更多见第 5 章）：
>
> ```
> >>> from setwrapper import Set
> >>> x = Set([1, 2, 3, 4])        # 调用 __init__（构造时去重）
> >>> y = Set([3, 4, 5])
> >>> x & y                        # 调 __and__ → intersect → 打印时调 __repr__
> Set:[3, 4]
> >>> x | y                        # 调 __or__ → union → __repr__
> Set:[1, 2, 3, 4, 5]
> >>> z = Set('hello')             # __init__ 去重 → {h,e,l,o}
> >>> z[0], z[-1], z[2:]           # 调 __getitem__
> ('h', 'o', ['l', 'o'])
> >>> for c in z: print(c, end=' ')   # 调 __iter__（否则退回 __getitem__ 协议）
> h e l o
> >>> ''.join(c.upper() for c in z)   # 同样走 __iter__
> 'HELO'
> >>> len(z), z                    # __len__、__repr__
> (4, Set:['h', 'e', 'l', 'o'])
> >>> z & 'mello', z | 'mello'     # 字符串也能参与运算
> (Set:['e', 'l', 'o'], Set:['h', 'e', 'l', 'o', 'm'])
> ```
>
> 多操作数扩展子类的一种方案看起来像示例 B-26 中的类。它只需要替换原集合中的两个方法。类的文档字符串说明了它的工作原理：
>
> ```python
> from setwrapper import Set
>
> class MultiSet(Set):
>     """
>     继承 Set 的所有名字，但把 intersect 和 union 扩展为支持多个操作数。
>     注意 "self" 仍是第一个参数（现在被装进 *args 参数里）。还要注意，
>     继承的 & 和 | 运算符会用 2 个参数调用这里的新方法，但处理 2 个以上
>     操作数需要方法调用，而不是表达式。intersect 在这里不去重：由
>     Set 构造器负责去重。
>     """
>     def intersect(self, *others):
>         res = []
>         for x in self:              # 扫描第一个序列
>             for other in others:    # 对所有其他参数
>                 if x not in other: break   # x 是否在每一个里？
>             else:                   # 不在：跳出循环
>                 res.append(x)       # 在：把元素加入结果
>         return Set(res)
>
>     def union(*args):               # self 就是 args[0]
>         res = []
>         for seq in args:            # 遍历所有参数
>             for x in seq:           # 遍历所有元素
>                 if not x in res:
>                     res.append(x)   # 新元素才加入结果
>         return Set(res)
> ```
>
> 与这个扩展的交互大致如下。注意：你可以用 `&` 或调用 `intersect` 做交集，但三个及以上操作数必须调用 `intersect`；`&` 是二元（两侧）运算符。另外，如果把原类以 `setwrapper.Set` 的方式引用（import 的 `as` 子句也可以按需给类改名），我们本来可以把 `MultiSet` 直接叫做 `Set`，让这个改动更透明：
>
> ```
> >>> x & y, x | y                  # 两个操作数
> (Set:[3, 4], Set:[1, 2, 3, 4, 5])
> >>> x.intersect(y, z)             # 三个操作数
> Set:[]
> >>> x.union(y, z)
> Set:[1, 2, 3, 4, 5, 0]
> >>> x.intersect([1,2,3], [2,3,4], [1,2,3])   # 四个操作数
> Set:[2, 3]
> >>> x.union(range(10))            # 非 MultiSet 也适用
> Set:[1, 2, 3, 4, 0, 5, 6, 7, 8, 9]
> >>> ''.join(w | 'super')          # 字符串集合
> 'soapuer'
> >>> (w | 'super') & MultiSet('slots')
> Set(['s', 'o'])
> ```

### 代码分析（逐行解读）

```python
class MultiSet(Set):                # 只改两个方法，其余全部继承
    def intersect(self, *others):   # *others 收集第二到第 N 个操作数
        res = []
        for x in self:              # 外层：遍历第一个集合（self 可迭代）
            for other in others:    # 中层：遍历其余每个操作数
                if x not in other: break   # 有一个不含 x → 直接放弃
            else:                   # 全部含 x（没有 break）→ 收进结果
                res.append(x)
        return Set(res)             # 由 Set 构造器去重

    def union(*args):               # 故意不写 self：self 就是 args[0]
        res = []
        for seq in args:            # 每个操作数（含 self）
            for x in seq:           # 每个元素
                if not x in res:    # 结果里没有才添加
                    res.append(x)
        return Set(res)
```

- `x & y` 的求值链：`x.__and__(y)` →（继承 Set 的 `__and__`）→ `self.intersect(y)` → MultiSet.intersect 接收 `(self, y)`。
- 三个操作数 `x.intersect(y, z)`：`&` 是二元运算符，语法上无法写 `x & y & z` 之外多参数，所以多操作数必须方法调用。

### 深度理解

- **核心概念**：继承 + 方法覆写让"集合"支持任意多个操作数的交集/并集；`for...else`（无 break 走 else）是实现"全通过"语义的精妙结构。
- **`self` 也是 `*args` 的一员**：`union(*args)` 里 `self` 就是 `args[0]`——方法调用 `x.union(y,z)` 等价 `union(x, y, z)`。
- **`&`/`|` 是二元运算符**：最多两个操作数；多操作数必须调用方法——这是运算符重载的天然边界。
- **通用性**：`union(range(10))`、`'mello'`、`'super'` 都能参与——因为实现只要求操作数是**可迭代对象**（`x not in other` 做的是迭代式成员测试）。
- **为何构造时去重**：`Set(res)` 构造器内部会去掉重复元素，所以 intersect/union 只管"收集"。
- **常见误区**：把 `x in y` 写成 `y in x`；忘记 `for...else` 的语义（有 break 就不走 else）；以为 `&` 能带 3 个操作数。

---

## 题 6. Class tree links（类树链接）

### 英文原文

> **6. Class tree links**: Example B-27 lists one way to change the lister class in Example 31-10, along with a rerun of the associated tester to show its augmented format. For full credit, do the same for the `dir`-based version, and also do this when formatting class objects in the tree-climber variant.

> To import `testmixin.py` as a test, either copy it over from the Chapter 31 examples folder or add that folder to `sys.path` as we did earlier in Part IV's solutions. It was copied here for variety: **Example B-27.** `Part6/listinstance-mod.py`

> ```python
> class ListInstance:
>     def __attrnames(self):
> …unchanged…

>     def __str__(self):
>         return (f'<Instance of {self.__class__.__name__}'    # My class's name
> f'({self.__supers()}), ' # My class's supers f'address {id(self):#x}:' # My address (hex) f'{self.__attrnames()}>') # name=value list

>     def __supers(self):
>         names = []
>         for super in self.__class__.__bases__:      # One level up from class
> names.append(super.__name__) # name, not str(super)

>         return ', '.join(names)
>         # Or: ', '.join(super.__name__ for super in self.__class__.__bases__)
> if __name__ == '__main__':
>     import testmixin                  # Assume testmixin.py copied to "."
> testmixin.tester(ListInstance) # Test class in this module

> ```
> ```
> $ python3 listinstance-mod.py
> <Instance of Sub(Super, ListInstance), address 0x10edc66c0:

>   data1='code'
>   data2='Python'
>   data3=3.12
> >

> ```

### 中文翻译

> **6. 类树链接**：示例 B-27 列出了修改示例 31-10 中 lister 类的一种方式，并重跑关联的测试器以展示增强后的格式。要得满分，请对基于 `dir` 的版本做同样处理，并且在对类对象格式化时也要在树形攀登（tree-climber）变体中这样做。
>
> 要导入 `testmixin.py` 作为测试，要么从第 31 章的示例文件夹复制它，要么像我们之前在第四部分解答里那样把那个文件夹加进 `sys.path`。这里为多样化起见把它复制了过来：
>
> ```python
> class ListInstance:                   # 混入类（mixin）：给任何类附加打印能力
>     def __attrnames(self):
>         …保持不变…
>     def __str__(self):
>         return (f'<Instance of {self.__class__.__name__}'  # 我的类名
>                 f'({self.__supers()}), '                   # 我的父类们
>                 f'address {id(self):#x}:'                  # 我的地址（十六进制）
>                 f'{self.__attrnames()}>')                  # 属性名=值 列表
>     def __supers(self):
>         names = []
>         for super in self.__class__.__bases__:    # 从类往上走一级
>             names.append(super.__name__)         # 用名字，而不是 str(super)
>         return ', '.join(names)
>         # 或：', '.join(super.__name__ for super in self.__class__.__bases__)
>
> if __name__ == '__main__':
>     import testmixin                  # 假设 testmixin.py 已复制到 "."
>     testmixin.tester(ListInstance)    # 测试本模块里的类
> ```
>
> ```
> $ python3 listinstance-mod.py
> <Instance of Sub(Super, ListInstance), address 0x10edc66c0:
>   data1='code'
>   data2='Python'
>   data3=3.12
> >
> ```

### 代码分析（逐行解读）

```python
class ListInstance:                      # 一个 mixin：被别的类多继承后提供 __str__
    def __str__(self):                   # print(实例) 时触发
        return (f'<Instance of {self.__class__.__name__}'   # self.__class__ 是实例的类型
                f'({self.__supers()}), '                    # 括号里列出父类名
                f'address {id(self):#x}:'                   # id(self) 内存地址，#x 十六进制带 0x
                f'{self.__attrnames()}>')                   # 追加属性清单
    def __supers(self):
        names = []
        for super in self.__class__.__bases__:   # __bases__：直接的父类元组（只一层）
            names.append(super.__name__)         # 取类名
        return ', '.join(names)                  # 逗号连接
```

- `self.__class__` 指向实例所属的类对象；`__bases__` 是该类直接父类的元组（"类树"的一级链接）。
- `id(self)` 返回对象的内存地址（CPython 中），`:#x` 格式化成 `0x10edc66c0` 样式。
- 输出 `<Instance of Sub(Super, ListInstance), address 0x10edc66c0: ...>`：显示了类名、父类名（类树链接）和属性。

### 深度理解

- **核心概念**：**类树（class tree）**是 Python OOP 的组织结构——类通过 `__bases__` 链接到父类，实例通过 `__class__` 链接到类。属性查找就是沿这条树向上搜索（MRO）。
- **为什么这样实现**：`__str__` 混入类（mixin）让任何多继承它的类自动获得友好的打印输出——这是"用组合代替复制"的横切关注点（cross-cutting concern）模式。
- **`__bases__` 只给直接父类**：向上多级需要循环或递归遍历 `super.__bases__`——树形攀登（tree-climber）变体就是在做这件事。
- **常见误区**：把 `super`（内置函数）当变量名用会遮蔽内置；`str(super)` 是 `<class ...>` 表示，想要名字必须用 `super.__name__`；`__str__` 返回字符串而非打印。

---

## 题 7. Composition（组合：午餐模拟）

### 英文原文

> **7. Composition**: A full-points solution is coded in Example B-28, with comments from the description mixed in with the code. This is one case where it's probably easier to express a problem in code than it is in narrative: **Example B-28.** `Part6/lunch.py`

> ```python
> class Lunch:
>     def __init__(self):                     # Make/embed Customer, Employee
>         self.cust = Customer()
>         self.empl = Employee()
>     def order(self, foodName):              # Start Customer order simulation
>         self.cust.placeOrder(foodName, self.empl)
>     def result(self):                       # Ask the Customer about its Food
>         self.cust.printFood()
> class Customer:
>     def __init__(self):                     # Initialize my food to None
>         self.food = None
>     def placeOrder(self, foodName, employee):   # Place order with Employee
>         self.food = employee.takeOrder(foodName)
>     def printFood(self):                    # Print the name of my food
>         print(self.food.name)
> class Employee:
>     def takeOrder(self, foodName):          # Return Food, with desired name
>         return Food(foodName)
> class Food:
>     def __init__(self, name):               # Store food name
>         self.name = name
> if __name__ == '__main__':
>     x = Lunch()                             # Self-test code
> x.order('burritos') # If run, not imported x.result() x.order('pizza') x.result()

> ```
> When run, customers place orders and get food from employees. This could be much more involved, but it suffices to demo the routing of messages between objects that's typical in OOP code:

> ```
> $ python3 lunch.py
> burritos pizza

> ```

### 中文翻译

> **7. 组合**：一个满分解法编码在示例 B-28 中，题目描述中的注释与代码混排在一起。这大概是一个"用代码表达问题比用文字叙述更容易"的例子：
>
> ```python
> class Lunch:                              # 组合器：把 Customer 和 Employee 装配起来
>     def __init__(self):                   # 创建/嵌入 Customer、Employee
>         self.cust = Customer()
>         self.empl = Employee()
>     def order(self, foodName):            # 启动 Customer 的订餐模拟
>         self.cust.placeOrder(foodName, self.empl)
>     def result(self):                     # 询问 Customer 关于它的 Food
>         self.cust.printFood()
>
> class Customer:                           # 顾客
>     def __init__(self):                   # 初始化我的食物为 None
>         self.food = None
>     def placeOrder(self, foodName, employee):   # 向 Employee 下订单
>         self.food = employee.takeOrder(foodName)   # 拿到 Food 对象存入自己
>     def printFood(self):                  # 打印我的食物名字
>         print(self.food.name)
>
> class Employee:                           # 员工
>     def takeOrder(self, foodName):        # 返回带所需名字的 Food
>         return Food(foodName)
>
> class Food:                               # 食物
>     def __init__(self, name):             # 存食物名
>         self.name = name
>
> if __name__ == '__main__':                # 自测代码
>     x = Lunch()                           # 运行而不是导入时才执行
>     x.order('burritos')
>     x.result()
>     x.order('pizza')
>     x.result()
> ```
>
> ```
> $ python3 lunch.py
> burritos
> pizza
> ```

### 代码分析（逐行解读）

```python
class Lunch:                    # "组合"：Lunch 拥有（has-a）Customer 和 Employee
    def __init__(self):
        self.cust = Customer()  # 创建并嵌入两个部件对象
        self.empl = Employee()
    def order(self, foodName):
        self.cust.placeOrder(foodName, self.empl)   # Lunch 是"调度员"：把员工对象传给顾客
    def result(self):
        self.cust.printFood()

class Customer:
    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)   # 顾客向员工要食物，员工返回 Food
    def printFood(self):
        print(self.food.name)   # 顾客打印自己拿到的食物名
```

消息路由链：`x.order('burritos')` → `Customer.placeOrder` → `Employee.takeOrder` → 创建 `Food('burritos')` → 存进 `customer.food` → `x.result()` → `printFood` → 打印 `burritos`。

### 深度理解

- **核心概念**：**组合（composition）**——一个对象"拥有"其他对象（has-a 关系），通过**消息传递（message passing）**协作：Lunch 调度、Customer 下单、Employee 制作、Food 描述。这是 OOP 代码中典型的"对象间路由"。
- **与继承的区别**：组合强调"部分-整体"装配（Lunch 有 Customer），继承强调"是"关系（Cat 是 Mammal）。优先组合、必要时继承是公认的设计原则。
- **职责划分**：每个类只做一件事——Customer 存食物、Employee 造食物、Food 存名字；类间通过公开方法协作，内部细节不外泄（封装）。
- **运行入口**：`if __name__ == '__main__':` 保证作为模块导入时静默，作为脚本运行时执行演示。
- **常见误区**：把组合写成"深层链式调用"（如 `x.cust.food.name`）破坏封装——通过方法暴露才是正道；忘了给类设计"协作接口"导致对象无法互相调用。

---

## 题 8. Zoo animal hierarchy（动物园动物层次）

### 英文原文

> **8. Zoo animal hierarchy**: Example B-29 shows one way to code the taxonomy in Python; it's artificial, but the general coding pattern applies to many real structures, from GUIs to employee databases to spacecraft. Notice that the `self.speak` call in `Animal` triggers an independent inheritance search, which generally finds `speak` in a subclass. Test this interactively by calling the `reply` method for instances per the exercise description.
>
> Try extending this hierarchy with new classes and making instances of various classes in the tree:
>
> **Example B-29.** `Part6/zoo.py`
> ```python
> class Animal:
>     def reply(self): self.speak()        # Back to subclass
>     def speak(self): print('blah')       # Custom message
>
> class Mammal(Animal):
>     def speak(self): print('huh?')
>
> class Cat(Mammal):
>     def speak(self): print('meow')
>
> class Dog(Mammal):
>     def speak(self): print('bark')
>
> class Primate(Mammal):
>     def speak(self): print('Hello world!')
>
> class Hacker(Primate): pass              # Inherit from Primate
> ```

### 中文翻译

> **8. 动物园动物层次**：示例 B-29 展示了在 Python 中编写这个分类体系的一种方式；它是人为构造的，但这种通用编码模式适用于许多真实结构——从 GUI 到员工数据库再到航天器。注意：`Animal` 里的 `self.speak` 调用会触发一次独立的继承搜索，通常会在子类里找到 `speak`。按练习描述，通过为实例调用 `reply` 方法来交互式测试它。试着用新类扩展这个层次结构，并创建树中各种类的实例：
>
> ```python
> class Animal:                     # 根类：定义通用协议
>     def reply(self): self.speak() # 转发给 self.speak —— 动态分派
>     def speak(self): print('blah')# 默认实现（"自定义消息"）
>
> class Mammal(Animal):             # 一级子类
>     def speak(self): print('huh?')
>
> class Cat(Mammal):
>     def speak(self): print('meow')
>
> class Dog(Mammal):
>     def speak(self): print('bark')
>
> class Primate(Mammal):
>     def speak(self): print('Hello world!')
>
> class Hacker(Primate): pass       # 空类体：全部继承自 Primate
> ```

### 代码分析（逐行解读）

```python
class Animal:
    def reply(self): self.speak()   # 调用 self.speak——不写死版本，运行时才决定
    def speak(self): print('blah')  # 兜底实现

class Mammal(Animal):
    def speak(self): print('huh?')

class Cat(Mammal):
    def speak(self): print('meow')

class Hacker(Primate): pass         # pass：类体为空，speak 继承自 Primate
```

交互测试（预期行为）：
```text
>>> cat = Cat(); dog = Dog(); hacker = Hacker()
>>> cat.reply()    # → meow：reply 里 self.speak() 沿 Cat→Mammal→Animal 找 speak，找到 Cat 版
>>> dog.reply()    # → bark
>>> hacker.reply() # → Hello world!：Hacker 无 speak，向上到 Primate
```

### 深度理解

- **核心概念**：**多态分派（dynamic dispatch）**——`Animal.reply` 中的 `self.speak()` 不是"调用 Animal.speak"，而是"以实例的类型为起点、沿继承树向上查找 speak"。因此同一句 `reply()` 在不同实例上发出不同的叫声。
- **底层机制**：`self.speak` 是属性查找：实例 → 实例的类 → 父类 → ……（MRO）。每新建一层 `speak` 覆写，分派结果就改变——这就是"覆写（override）"的威力。
- **空类的意义**：`class Hacker(Primate): pass` 表示"不做任何改动、完全继承"——用于给分类体系占位或将来添加特殊行为。
- **设计模式对应**：这本质是"模板方法"的又一例（骨架 `reply` 固定，可变点 `speak` 由子类决定），也常被称为"策略的继承实现"。
- **常见误区**：在 `reply` 里写 `Animal.speak(self)` 会**绕过**多态（永远用基类实现）；忘记覆写导致所有动物都喊 "blah"。

# Part VII：Exceptions（异常）

### 英文原文

> Part VII, Exceptions
> See "Test Your Knowledge: Part VII Exercises" in Chapter 36 for the exercises.

### 中文翻译

> 第七部分：异常。练习见第 36 章的 "Test Your Knowledge: Part VII Exercises"。

### 深度理解

- **核心概念**：Part VII 练习覆盖 `try/except/else` 结构、自定义异常类、异常的"冒泡（percolation）"、`sys.exc_info`、`traceback` 打印、装饰器包装异常，以及 10 个自学演示程序（Self-Study Demos）。
- **练习主线**：从一个会抛异常的 `oops` 函数出发，逐步把它改造成"能捕获、能识别类型、能记录 traceback"的健壮异常处理工具。

---

## 题 1. try / except

### 英文原文

> **1. try/except**: One possible coding of the `oops` function is listed in Example B-30. As for the noncoding questions, changing `oops` to raise a `KeyError` instead of an `IndexError` means that the `try` handler won't catch the exception—it "percolates" to the top level and triggers Python's default error message. The names `KeyError` and `IndexError` come from the outermost built-in names scope (the `B` in "LEGB").
>
> Import `builtins` and pass it as an argument to the `dir` function to see this for yourself, per Chapter 17:
>
> **Example B-30.** `Part7/oops.py`
> ```python
> def oops():
>     raise IndexError()
>
> def doomed():
>     try:
>         oops()
>     except IndexError:
>         print('caught an index error!')
>     else:
>         print('no error caught...')
>
> if __name__ == '__main__': doomed()
> ```
>
> ```
> $ python3 oops.py
> caught an index error!
> ```

### 中文翻译

> **1. try/except**：`oops` 函数的一种可行写法列在示例 B-30 中。至于非编码问题：把 `oops` 改为抛出 `KeyError` 而不是 `IndexError`，意味着 `try` 处理器不会捕获该异常——它会"冒泡（percolates）"到顶层，触发 Python 的默认错误消息。`KeyError` 和 `IndexError` 这两个名字来自最外层的内置名字作用域（LEGB 中的 `B`）。按第 17 章的方法，导入 `builtins` 并把它作为参数传给 `dir` 函数，你自己就能看到这一点：
>
> ```python
> def oops():
>     raise IndexError()          # 抛出一个 IndexError 实例
>
> def doomed():
>     try:
>         oops()                  # 调用可能抛异常的函数
>     except IndexError:          # 只捕获 IndexError 类型
>         print('caught an index error!')
>     else:                       # 没有异常时才执行
>         print('no error caught...')
>
> if __name__ == '__main__': doomed()
> ```
>
> ```
> $ python3 oops.py
> caught an index error!
> ```

### 代码分析（逐行解读）

```python
def oops():
    raise IndexError()          # raise 语句：抛出异常类的实例，立即中断函数

def doomed():
    try:                        # try 块：可能出错的代码
        oops()
    except IndexError:          # 捕获子句：异常类型匹配（含子类）才执行
        print('caught an index error!')
    else:                       # 无异常时执行（跳过 except）
        print('no error caught...')

if __name__ == '__main__': doomed()
```

### 深度理解

- **核心概念**：`try/except/else` 是异常处理的骨架——`try` 监控、`except` 捕获指定类型、`else` 在"无异常"时执行（区别于 `finally` 的无条件执行）。
- **异常匹配**：`except IndexError` 用**类**匹配，不只精确类型——`IndexError` 的子类也会被捕获。改成 `KeyError` 后，`except IndexError` 不再匹配，异常沿调用栈一路冒泡到顶层，由默认处理器打印 Traceback。
- **名字来源（LEGB）**：`KeyError`、`IndexError` 是内建命名空间（builtins，即 LEGB 的 B）里的名字——`import builtins; dir(builtins)` 就能看到它们。异常类型本身就是"继承自 Exception 的类对象"。
- **设计思想**：异常让"错误处理"与"业务逻辑"分离——调用方决定如何应对，而不是每个函数都自己打印错误。
- **常见误区**：捕获"裸 except"（捕获一切，包括 KeyboardInterrupt）是不良实践；`else` 与 `finally` 语义混淆。

---

## 题 2. Exception objects and lists（异常对象与异常列表）

### 英文原文

> **2. Exception objects and lists**: Example B-31 is one way to extend this module for an exception of its own: **Example B-31.** `Part7/oops2.py`

> ```python
> class MyError(Exception): pass
> def oops():
>     raise MyError('Hack!')
> def doomed():
>     try:
> oops()

>     except IndexError:
>         print('caught an index error!')
>     except MyError as exc:
>         print('caught error:', MyError, exc)
>     else:
>         print('no error caught...')
> if __name__ == '__main__':
> doomed()

> ```
> ```
> $ python3 oops2.py
> caught error: <class '__main__.MyError'> Hack!

> ```
> Like all class exceptions, the raised instance is accessible via the `as` variable data; the error message shows both the class's (`<...>`) and its instance's (`Hack!`) displays. The instance must be inheriting both an `__init__` and a `__repr__` or `__str__` from Python's `Exception` class, or it would print much as the class does. See Chapter 35 for details on how these defaults work in built-in exception classes.

### 中文翻译

> **2. 异常对象与异常列表**：示例 B-31 是把该模块扩展出自定义异常的一种方式：
>
> ```python
> class MyError(Exception): pass      # 自定义异常：继承内置的 Exception 基类
>
> def oops():
>     raise MyError('Hack!')          # 抛出自定义异常，带一条消息参数
>
> def doomed():
>     try:
>         oops()
>     except IndexError:              # 第一个 except：只匹配 IndexError
>         print('caught an index error!')
>     except MyError as exc:          # 第二个 except：匹配 MyError，用 as 绑定异常实例
>         print('caught error:', MyError, exc)
>     else:
>         print('no error caught...')
>
> if __name__ == '__main__':
>     doomed()
> ```
>
> ```
> $ python3 oops2.py
> caught error: <class '__main__.MyError'> Hack!
> ```
>
> 与所有类异常一样，被抛出的实例可以通过 `as` 变量访问；错误消息同时显示类的表示（`<...>`）和实例的表示（`Hack!`）。该实例必须从 Python 的 `Exception` 类同时继承 `__init__` 和 `__repr__` 或 `__str__`，否则它打印起来会跟类本身差不多。关于这些默认值在内置异常类中如何工作，详见第 35 章。

### 代码分析（逐行解读）

```python
class MyError(Exception): pass     # 自定义异常 = 继承 Exception 的空类
                                   # 自动获得：__init__(args)、__str__/__repr__（打印 args）

def oops():
    raise MyError('Hack!')         # MyError('Hack!') 是构造实例；'Hack!' 存进实例的 args

def doomed():
    try:
        oops()
    except IndexError:             # 顺序匹配：先试 IndexError
        print('caught an index error!')
    except MyError as exc:         # 再试 MyError；exc 绑定被抛出的异常实例
        print('caught error:', MyError, exc)
                                   # MyError 打印为 <class '__main__.MyError'>（类对象）
                                   # exc 打印为 'Hack!'（实例的 __str__ 输出消息）
    else:
        print('no error caught...')
```

### 深度理解

- **核心概念**：异常是**类**，`raise` 抛的是**实例**。`except SomeError as e:` 里的 `e` 就是那个实例，可以读取、检查、重新抛出。
- **自定义异常的最小写法**：`class MyError(Exception): pass` 就够了——`Exception` 基类提供了默认的 `__init__`（把参数存进 `args`）和 `__str__`/`__repr__`（打印 args）。`MyError('Hack!')` 的 `'Hack!'` 就是一条"错误消息"。
- **`as` 绑定的作用域**：Python 3 中 `as` 变量在 except 块结束后即被清除（防止悬垂引用）。
- **多个 except 的顺序**：从上到下逐一匹配，命中第一个即停——所以**子类必须写在父类之前**（先 `except MyError` 再 `except Exception`，反过来就永远轮不到 MyError）。
- **常见误区**：`except MyError as exc` 里打印 `MyError` 得到的是类对象而不是消息；忘了自定义异常继承 `Exception`（继承普通类也行，但 Exception 保证兼容性）。

---

## 题 3. Error handling（错误处理工具）

### 英文原文

> **3. Error handling**: Example B-32 is one way to solve this exercise. It codes tests in a file rather than interactively, but the results are similar enough for full credit. Notice that the empty `except` and `sys.exc_info` approach used here will catch exit-related exceptions that listing `Exception` with an `as` variable won't; that's probably not ideal in most applications code but might be useful in a tool like this designed to work as a sort of exceptions firewall.

> **Example B-32.** `Part7/exctools.py`

> ```python
> import sys, traceback
> def safe(callee, *pargs, **kargs):
>     try:
> callee(*pargs, **kargs) # Catch everything else

>     except:                             # Or "except Exception as E:"
> traceback.print_exc()

>         print(f'Got {sys.exc_info()[0]} {sys.exc_info()[1]}')
> if __name__ == '__main__':
>     import oops2
> safe(oops2.oops)

> ```
> ```
> $ python3 exctools.py
> Traceback (most recent call last): File "/…/LP6E/AppendixB/Part7/exctools.py", line 5, in safe callee(*pargs, **kargs) # Catch everything else File "/…/LP6E/AppendixB/Part7/oops2.py", line 4, in oops

>     raise MyError('Hack!')
> oops2.MyError: Hack! Got <class 'oops2.MyError'> Hack!

> ```
> Bonus points: the sort of code in Example B-33 could turn this into a function decorator that could wrap and catch exceptions raised by any function, using techniques introduced briefly in Chapter 32, but covered more fully in Chapter 39—it augments a function, rather than expecting it to be passed in explicitly, and produces similar output when run (there's an extra call level, and filenames differ): **Example B-33.** `Part7/exctools_deco.py`

> ```python
> import sys, traceback
> def safe(callee):
>     def callproxy(*pargs, **kargs):
>         try:
>             return callee(*pargs, **kargs)
>         except Exception as E:
> traceback.print_exc()

>             print(f'Got {E.__class__} {E}')
>     return callproxy
> if __name__ == '__main__':
>     import oops2
>     @safe
>     def test():                     # test = safe(test)
> oops2.oops() test()

> ```

### 中文翻译

> **3. 错误处理**：示例 B-32 是解决这个练习的一种方式。它把测试写在文件里而不是交互式地运行，但结果足够相似、可得满分。注意：这里使用的**空 `except`** 和 `sys.exc_info` 方案会捕获与退出（exit）相关的异常，而 `Exception` 加 `as` 变量的写法捕获不到；这在大多数应用代码中可能并不理想，但对这种设计成"异常防火墙"的工具可能有用：
>
> ```python
> import sys, traceback
>
> def safe(callee, *pargs, **kargs):    # 通用安全调用器
>     try:
>         callee(*pargs, **kargs)        # 调用任意函数（位置+关键字参数）
>     except:                            # 空 except：捕获一切（包括 SystemExit 等）
>         traceback.print_exc()          # 打印完整回溯
>         print(f'Got {sys.exc_info()[0]} {sys.exc_info()[1]}')
>                                        # sys.exc_info() 返回 (类型, 实例, 回溯对象)
> if __name__ == '__main__':
>     import oops2
>     safe(oops2.oops)
> ```
>
> ```
> $ python3 exctools.py
> Traceback (most recent call last):
>   File ".../exctools.py", line 5, in safe
>     callee(*pargs, **kargs)      # 抛出点
>   File ".../oops2.py", line 4, in oops
>     raise MyError('Hack!')
> oops2.MyError: Hack!
> Got <class 'oops2.MyError'> Hack!
> ```
>
> 加分项：示例 B-33 中的代码可以把这变成一个**函数装饰器**，包装并捕获任何函数抛出的异常——使用第 32 章简要介绍、第 39 章更全面讲解的技术；它增强（augments）一个函数，而不是期待函数被显式传入，运行输出也类似（多一层调用，文件名不同）：
>
> ```python
> import sys, traceback
>
> def safe(callee):                     # 装饰器工厂：接收函数
>     def callproxy(*pargs, **kargs):   # 代理函数：原函数的"替身"
>         try:
>             return callee(*pargs, **kargs)
>         except Exception as E:        # 捕获 Exception 及其子类
>             traceback.print_exc()
>             print(f'Got {E.__class__} {E}')
>     return callproxy                  # 返回代理，替换原函数名
>
> if __name__ == '__main__':
>     import oops2
>
>     @safe                             # 语法糖：test = safe(test)
>     def test():
>         oops2.oops()
>
>     test()
> ```

### 代码分析（逐行解读）

```python
def safe(callee, *pargs, **kargs):     # 接收"任意签名"的函数：*pargs 位置、**kargs 关键字
    try:
        callee(*pargs, **kargs)        # 原样转发调用
    except:                            # 空 except = 捕获所有异常
        traceback.print_exc()          # 打印回溯（print_exc 等价于 traceback.format_exc 再打印）
        print(f'Got {sys.exc_info()[0]} {sys.exc_info()[1]}')
                                       # sys.exc_info() → (异常类, 异常实例, traceback 对象)
```

装饰器版关键点：
```python
def safe(callee):
    def callproxy(*pargs, **kargs):    # 闭包：记住被包装的 callee
        try:
            return callee(*pargs, **kargs)   # 正常时返回原结果
        except Exception as E:         # 注意：捕获 Exception 子类（不含 SystemExit/KeyboardInterrupt）
            traceback.print_exc()
            print(f'Got {E.__class__} {E}')
    return callproxy                   # 把"代理"交给调用方

@safe
def test(): ...    # 等价于 test = safe(test)——装饰器在定义时把函数替换为代理
```

### 深度理解

- **核心概念**：异常"防火墙"模式——把任意函数包在 try 里，异常发生时既打印回溯又不让程序崩溃。两种包装方式：**显式传函数**（safe(f)）与**装饰器**（@safe）。
- **空 except vs except Exception**：空 `except:` 捕获包括 `SystemExit`、`KeyboardInterrupt` 在内的一切（exit-related）；`except Exception as E:` 只捕获普通异常子树。工具型"防火墙"用前者（宁可吞掉一切），应用代码用后者更安全。
- **`sys.exc_info()`**：返回当前异常的三元组 `(类型, 实例, traceback 对象)`——`[0]` 是类（`<class 'oops2.MyError'>`）、`[1]` 是实例（打印出 `Hack!`）。它在 3.x 中比 Python 2 的裸 `sys.exc_type`/`sys.exc_value` 更规范。
- **装饰器的机制**：`@safe` 在函数定义完成时执行 `safe(test)`，用 `callproxy` 替换名字 `test`；此后调用 `test()` 实际调用代理——闭包捕获原函数，"增强而非修改"。
- **闭包与 *args/**kwargs**：代理用 `*pargs, **kargs` 原样转发任意签名，保证接口透明——这是所有装饰器/包装器的标配。
- **常见误区**：裸 except 吞掉 Ctrl+C（KeyboardInterrupt）；装饰器忘了 `return`（函数变 None）；`sys.exc_info` 在 except 块外调用返回 `(None, None, None)`。

---

## 题 4. Self-study examples（自学演示程序）

### 英文原文

> **4. Self-study examples**: In closing, Examples B-34 through B-43 are 10 examples for you to study on your own. Their code and supporting files are in the `Self-Study-Demos` subfolder of the examples package's `AppendixB/Part7` folder. These require no extra installs as they use standard-library tools, though `tkinter` is sketchy on phones (see Appendix A). For more examples, see follow-up books and resources for the application domains you'll be exploring next:

### 中文翻译

> **4. 自学演示程序**：最后，示例 B-34 到 B-43 是 10 个供你自行研究的例子。它们的代码和支持文件在示例包 `AppendixB/Part7` 文件夹的 `Self-Study-Demos` 子文件夹中。它们只使用标准库工具，无需额外安装，不过 `tkinter` 在手机上不太靠谱（见附录 A）。想要更多例子，请看后续书籍和相关应用领域的资源：

### 示例 B-34 到 B-36：找出最大的 Python 源文件（三个版本）

```python
# Example B-34. Part7/Self-Study-Demos/largest-dir.py
# 找出单个目录里最大的 Python 源文件
import os, glob
dirname = '/Users/me/Downloads'          # 改成你自己的目录（或用 input() 或 sys.argv）
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')   # glob 匹配目录下所有 .py 文件
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))      # 元组 (大小, 路径) 入列表

allsizes.sort()                          # 按大小升序排序（先比第一个元素）
print(allsizes[:2])                      # 最小的两个
print(allsizes[-2:])                     # 最大的两个
```

```python
# Example B-35. Part7/Self-Study-Demos/largest-tree.py
# 找出一整棵目录树里最大的 Python 源文件
import sys, os, pprint
if sys.platform[:3] == 'win':
    dirname = r'C:\Users\me\Downloads'   # Windows 用 raw 字符串避免 \ 转义
else:
    dirname = '/Users/me/Downloads'
allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):   # os.walk：递归遍历目录树
    for filename in filesHere:
        if filename.endswith('.py'):
            fullname = os.path.join(thisDir, filename)    # 拼出完整路径
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))
allsizes.sort()
pprint.pprint(allsizes[:2])              # pprint：漂亮的递归打印
pprint.pprint(allsizes[-2:])
```

```python
# Example B-36. Part7/Self-Study-Demos/largest-import.py
# 在模块导入搜索路径上找出最大的 Python 源文件
import sys, os, pprint
visited = {}                             # 记录已访问的目录（避免重复统计）
allsizes = []
for srcdir in sys.path:                  # 遍历搜索路径中的每个目录
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        thisDir = os.path.normpath(thisDir)      # 规范化路径（消除 .、.. 等）
        if thisDir.upper() in visited:           # 大小写不敏感去重（Windows）
            continue
        else:
            visited[thisDir.upper()] = True
        for filename in filesHere:
            if filename.endswith('.py'):
                pypath = os.path.join(thisDir, filename)
                try:
                    pysize = os.path.getsize(pypath)
                except:                          # 权限等错误时跳过
                    print('skipping', pypath)
                allsizes.append((pysize, pypath))
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])
```

**深度理解**：
- 三个版本分别演示 `glob`（单目录通配）、`os.walk`（递归树遍历）、`sys.path` 遍历（import 搜索路径）+ `visited` 去重——同一任务的三种"范围"。
- `(size, name)` 元组 + `sort()`：利用元组比较"先比第一个元素"的特性，天然按大小排序；`pprint.pprint` 适合打印大结构。
- 路径处理：`os.sep`（平台分隔符）、`os.path.join`（安全拼路径）、`os.path.normpath`（规范化）、raw 字符串防 `\` 转义。

### 示例 B-37 与 B-38：按列求和（summer）

```python
# Example B-37. Part7/Self-Study-Demos/summer1.py
# 求一个逗号分隔文本文件每列的和
filename = 'data.txt'                    # 改成你的文件名
sums = {}                                # 列号 → 累加和
for line in open(filename):              # 逐行读取（文件对象可迭代）
    cols = line.split(',')               # 按逗号拆成字符串列表
    nums = [int(col) for col in cols]    # 列表推导式：全部转整数
    for (ix, num) in enumerate(nums):    # enumerate：同时拿到下标和值
        sums[ix] = sums.get(ix, 0) + num # dict.get(key, 默认0)：列不存在时从 0 开始
for key in sorted(sums):                 # 按键排序输出
    print(key, '=', sums[key])
```

```python
# Example B-38. Part7/Self-Study-Demos/summer2.py
# 与 summer1 类似，但用列表而不是字典存和
import sys
filename = sys.argv[1]                   # "python3 summer2.py data.txt 3"
numcols = int(sys.argv[2])               # 列数来自命令行

totals = [0] * numcols                   # 初始化全 0 列表
for line in open(filename):
    cols = line.split(',')
    nums = [int(x) for x in cols]
    totals = [(x + y) for (x, y) in zip(totals, nums)]   # zip 成对相加 → 新列表
print(totals)
```

**深度理解**：
- `summer1`：字典版——`get(key, 0)` 处理"列首次出现"；`enumerate` 提供列号。列数未知也能跑。
- `summer2`：列表版——列数必须预先知道（命令行传入）；`zip(totals, nums)` 逐对相加再生成新列表。
- 对比两种数据结构：字典灵活（键任意）、列表高效（下标直取）——"选型即设计"。

### 示例 B-39：回归测试（regrtest）

```python
# Example B-39. Part7/Self-Study-Demos/regrtest.py
# 为一组脚本的输出做简单的回归测试
import os
testscripts = [dict(script='test1.py', args=''),   # 改成你自己的（或用 glob）
               dict(script='test2.py', args='-opt')]   # 需要时再加编码
for testcase in testscripts:
    commandline = '%(script)s %(args)s' % testcase     # 老式 % 格式化拼命令
    output = os.popen(commandline).read()              # 运行子进程并捕获其输出
    result = testcase['script'] + '.result'            # 结果文件名
    if not os.path.exists(result):
        open(result, 'w').write(output)                # 首次运行：保存基线
        print('Created:', result)
    else:
        priorresult = open(result).read()              # 后续运行：与基线对比
        if output != priorresult:
            print('FAILED:', testcase['script'])       # 输出变了 → 回归失败
            print(output)
        else:
            print('Passed:', testcase['script'])
```

**深度理解**：
- **回归测试（regression test）**思想：把程序首次输出存为"基线（baseline）"，以后每次运行对比——输出变了就报 FAILED。这是软件工程里自动化测试的雏形。
- `os.popen` 运行子命令并读取其输出（在 3.x 中可用 `subprocess` 更规范）；测试脚本列表用字典列表描述"脚本名 + 参数"。

### 示例 B-40 与 B-41：tkinter GUI（两个版本）

```python
# Example B-40. Part7/Self-Study-Demos/gui1.py
"""
用 tkinter 构建一个 GUI：按钮能改变颜色并让标签长大。
注意：这个 GUI 可能会一直长大，直到你手动关闭它的窗口！
"""
from tkinter import *
import random
fontsize = 25
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']

def reply(text):
    print(text)
    popup = Toplevel()                       # 弹出新窗口
    color = random.choice(colors)            # 随机选色
    Label(popup, text='Popup', bg='black', fg=color).pack()
    L.config(fg=color)                       # 改主标签文字颜色

def cycle():
    L.config(fg=random.choice(colors))
    win.after(250, cycle)                    # 250ms 后再执行 cycle（定时循环）

def grow():
    global fontsize                          # 修改模块级全局变量需要 global
    fontsize += 5
    L.config(font=('arial', fontsize, 'italic'))
    win.after(100, grow)                     # 100ms 后再执行

win = Tk()                                   # 主窗口
L = Label(win, text='Hack',
          font=('arial', fontsize, 'italic'), fg='yellow', bg='navy',
          relief=RAISED)
L.pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text='popup', command=(lambda: reply('new'))).pack(side=BOTTOM, fill=X)
Button(win, text='cycle', command=cycle).pack(side=BOTTOM, fill=X)
Button(win, text='grow', command=grow).pack(side=BOTTOM, fill=X)
win.mainloop()                               # 事件循环：GUI 从这里开始运行
```

```python
# Example B-41. Part7/Self-Study-Demos/gui2.py
"""
与 gui1 类似，但用类，让每个窗口拥有自己的状态信息。
注意：这个 GUI 可能会一直长大，直到你按 Stop 或关掉窗口！
"""
from tkinter import *
import random

class MyGui:
    """
    一个 GUI：按钮改变颜色、让标签长大
    """
    colors = ['blue', 'green', 'orange', 'red', 'brown', 'yellow']
    def __init__(self, parent, title='popup'):
        parent.title(title)
        self.growing = False                 # 实例状态：是否在生长
        self.fontsize = 10
        self.lab = Label(parent, text='Hack2', fg='white', bg='navy')
        self.lab.pack(expand=YES, fill=BOTH)
        Button(parent, text='Hack', command=self.reply).pack(side=LEFT)
        Button(parent, text='Grow', command=self.grow).pack(side=LEFT)
        Button(parent, text='Stop', command=self.stop).pack(side=LEFT)
    def reply(self):
        "按 Hack 按钮时随机改变标签颜色"
        self.fontsize += 5
        color = random.choice(self.colors)
        self.lab.config(bg=color,
                        font=('courier', self.fontsize, 'bold italic'))
    def grow(self):
        "按 Grow 按钮时开始让标签长大"
        self.growing = True
        self.grower()
    def grower(self):
        "多次按键会调度多个生长器"
        if self.growing:                     # 状态门控：Stop 后停止
            self.fontsize += 5
            self.lab.config(font=('courier', self.fontsize, 'bold'))
            self.lab.after(500, self.grower) # 500ms 后再来一次
    def stop(self):
        "按 Stop 按钮时停止所有生长循环"
        self.growing = False

class MySubGui(MyGui):
    colors = ['black', 'purple']             # 子类覆写颜色选项

MyGui(Tk(), 'main')                          # 创建多个窗口
MyGui(Toplevel())
MySubGui(Toplevel())
mainloop()
```

**深度理解**：
- **tkinter 事件驱动模型**：`mainloop()` 进入事件循环；`after(毫秒, 函数)` 是"定时器回调"——GUI 的动画/周期任务都靠它，而不是死循环（会卡死界面）。
- **gui1（过程式）vs gui2（类）**：gui2 把状态（字体大小、生长开关）收进实例属性，多个窗口互不干扰，还支持子类覆写（MySubGui 换颜色）——**类把 GUI 组件和状态打包成可复用单元**，这就是 Part VI 学的 OOP 在真实 GUI 里的应用。
- `global fontsize`：函数内修改模块级变量必须先声明 global，否则会创建局部变量。
- `command=...` 绑定回调；lambda 用于给回调传参。

### 示例 B-42：POP 邮件检查工具（popmail）

```python
# Example B-42. Part7/Self-Study-Demos/popmail.py
"""
POP 邮件收件箱扫描与删除工具。
扫描 pop 邮箱，只取邮件头，允许在不下整封信的情况下删除。
"""
import poplib, getpass, sys
mailserver = 'your pop email server name here'   # 改成你的 pop.server.net
mailuser = 'your pop email user name here'       # 改成你的 userid
mailpasswd = getpass.getpass(f'Password for {mailserver}? ')   # 安全输入密码

print('Connecting...')
server = poplib.POP3(mailserver)                 # 连接 POP3 服务器
server.user(mailuser)                            # 用户名
server.pass_(mailpasswd)                         # 密码
try:
    print(server.getwelcome())                   # 服务器欢迎信息
    msgCount, mboxSize = server.stat()           # 邮件数与邮箱总大小
    print('There are', msgCount, 'mail messages, size ', mboxSize)
    msginfo = server.list()                      # 列出所有邮件
    print(msginfo)
    for i in range(msgCount):
        msgnum = i+1
        msgsize = msginfo[1][i].split()[1]       # 解析每封大小
        resp, hdrlines, octets = server.top(msgnum, 0)   # 只取邮件头（不下正文）
        print('-'*80)
        print('[%d: octets=%d, size=%s]' % (msgnum, octets, msgsize))
        for line in hdrlines: print(line)
        if input('Print?') in ['y', 'Y']:
            for line in server.retr(msgnum)[1]: print(line)   # 下载全文
        if input('Delete?') in ['y', 'Y']:
            print('deleting')
            server.dele(msgnum)                  # 标记删除（在服务器上）
        else:
            print('skipping')
finally:
    server.quit()                                # 确保释放邮箱锁
input('Bye.')                                    # Windows 下保持窗口不关
```

**深度理解**：
- 展示网络编程 + 协议库（`poplib`）的完整流程：连接、认证、stat、list、top（取头）、retr（取全文）、dele（删除）、quit。
- `getpass.getpass` 不在屏幕回显密码——安全输入的标准做法。
- `try/finally` 保证无论发生什么都能 `server.quit()`（释放服务器端邮箱锁）——异常部分的核心实践。

### 示例 B-43：SQLite 数据库脚本（sqldbase）

```python
# Example B-43. Part7/Self-Study-Demos/sqldbase.py
# 数据库脚本：填充并查询一个存储在 people.db 里的 SQLite 数据库
import sqlite3, time
conn = sqlite3.connect('people.db')          # 数据库文件名（没有则创建）
curs = conn.cursor()                         # 通过游标提交 SQL
# 若表还不存在则创建并填充
tbl = curs.execute('select name from sqlite_master where name = \'people\'')
if tbl.fetchone() is None:                   # 表不存在
    print('Making table anew')
    curs.execute('create table people (name, job, pay)')   # 建表
    recs = [('Pat', 'mgr', 40000), ('Sue', 'dev', 60000), ('Bob', 'dev', 50000)]
    for rec in recs:
        curs.execute('insert into people values (?, ?, ?)', rec)  # 参数化插入
    conn.commit()                            # 提交事务
# 显示所有行
print('Rows:')
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)
# 只显示 dev
print('Devs:')
curs.execute("select name, pay from people where job = 'dev'")
colnames = [desc[0] for desc in curs.description]      # 列名
while row := curs.fetchone():                # 海象运算符：赋值并测试
    print('-' * 30)
    for (name, value) in zip(colnames, row):
        print(f'{name:<4} => {value}')       # f-string 左对齐格式化
# 更新 dev 的工资：下次运行时可见
secs = int(time.time())                      # UTC 秒数
curs.execute('update people set pay = ? where job = ?', [secs, 'dev'])
conn.commit()
```

**深度理解**：
- **sqlite3**：Python 内置 SQLite 数据库驱动——无需服务器，一个文件就是数据库。连接（connect）→ 游标（cursor）→ execute（SQL）→ commit（提交）→ fetch（取结果）。
- **参数化查询**：`execute('insert ... values (?, ?, ?)', rec)` 用 `?` 占位符传参——**防止 SQL 注入**的最佳实践。
- `sqlite_master` 是 SQLite 的系统表，用来检查表是否已存在；`curs.description` 提供列名。
- `while row := curs.fetchone():` 是 Python 3.8+ 的海象运算符（walrus operator）——在条件里赋值。
- 综合了大全书的多项技术：异常（try/finally）、文件、字符串格式化（% 、format、f-string）、推导式、zip、时间戳。

---

# 附录总结

## 技术要点回顾（Key Takeaways）

- **七大 Part 的技术全景**：
  - **Part I（入门）**：REPL vs 脚本、模块导入缓存、字节码与 `.pyc`、shebang、Traceback 阅读、循环引用与垃圾回收。
  - **Part II（对象）**：索引与切片语义（越界报错 vs 自动缩放）、不可变性、字典键的可哈希性、文件读写与 seek 回卷。
  - **Part III（语句）**：循环的 `else` 子句、if/match/字典/列表四种选择写法、`list.sort()` 返回 None 的陷阱、`sorted()` 内置。
  - **Part IV（函数）**：多态、`*args`/`**kwargs`/默认值的匹配规则、推导式 vs map vs 循环、生成器的惰性、递归的栈深度限制、计时与基准测试（`timeit`、`timer2`）。
  - **Part V（模块）**：`import` vs `from` 的命名空间语义、`if __name__ == '__main__':` 自测惯例、包与 `__init__.py`、reload、循环导入的成因与规避。
  - **Part VI（类）**：继承与动态分派（模板方法）、运算符重载（`__add__`/`__radd__`）、`__getattr__` 代理与内建操作不拦截的局限、类变量 vs 实例变量、组合 vs 继承、mixin 与类树（`__bases__`）。
  - **Part VII（异常）**：try/except/else、异常类与实例、`as` 绑定、`sys.exc_info` 与 `traceback`、装饰器包装异常、参数化 SQL 与 GUI 事件循环等综合应用。
- **贯穿全书的主线**：**名字是引用**（赋值不复制）——它解释了循环结构、字典共享、类变量共享、import 命名空间等几乎所有"反直觉"现象。
- **性能认知**：标准库 C 实现（`math.factorial`、`math.sqrt`）通常碾压手写 Python 循环；递归最慢且有栈深上限；基准结果随平台/解释器变化，要自己实测。

## 学习建议（Learning Advice）

- **重要程度**：5/5 星——习题是检验理解的最快途径，本附录是"答案卷"，两者配合使用效果最佳。
- **应该掌握到什么程度**：
  - 能够**不看答案**独立完成每题，并解释每一步输出为什么如此；
  - 对每个"为什么"（为什么切片越界安全、为什么 sort 返回 None、为什么 `__getattr__` 拦不住 +）都能说出底层机制；
  - 能把答案中的代码**改造**成自己的版本（作者明说"任何合理方案都得满分"）——这才是真正的掌握。
- **后续学习路线**：
  - 巩固：重做各 Part 的 "Test Your Knowledge" 练习，对照本附录逐题订正；
  - 深入：阅读第 39 章（装饰器细节）、第 40 章（元类与特殊属性）、第 41 章（编码规范）——本附录的多处内容在那里有更系统的展开；
  - 实践：把 Self-Study Demos（largest-*.py、summer*.py、regrtest.py、gui*.py、popmail.py、sqldbase.py）跑起来并改造——它们是"标准库 + 真实任务"的最佳示范；
  - 拓展：学习 `unittest`/`pytest`（把 regrtest 的朴素想法升级为正式测试框架）、`subprocess`（替代 os.popen）、`pathlib`（替代 os.path 拼接）。
