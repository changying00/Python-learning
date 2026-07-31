# 正则表达式 Regular Expression

> 独立于 语言的一种 表达式 、大部分编程语言 都支持 正则表达式的处理 ~~~
> 
> 正则表达式 可以对字符串 进行 `检索`、 `提取`、`替换` 等 操作 。
> 
> 正则表达式 是一个 `模式匹配规则` 、本质 是由 一组 `特殊符号` 组成的 字符串 、这些 特殊符号 构成了 正则表达式的 匹配规则 ！！！
> 
> 正则表达式 通常可以简写为  regex  或者  regexp 、 在 python 语言中，操作正则表达式的 模块是 re 模块 

## 正则特点

- 性能高 
- 可读性差

## 常见匹配规则

- xyz  :   xyz 是一个泛指、 写什么就 匹配什么 ，  xyz 中 不能包含 特殊匹配规则 符号 
- [xyz] :   匹配 x,  y,  z  中的 任意 1个 字符 
  - [0-9] :  匹配 任意一个数字 :   `-`  代表 匹配 的字符是 连续的区间 
  - [A-Z] :  匹配任意一个大写字母 
  - [A-Za-z]：匹配任意一个字母 
  - [A-Za-z0-9]:  匹配任意一个字母或数字
  - [A-Za-z0-9_]： 匹配任意一个单词字母 (由  字母、数字、下划线组成)
- [^xyz]  :   匹配 除 x,  y,  z  中的 任意 1个 字符
- \d  :    匹配 任意一个 数字字符 、等价于  [0-9]
- \D  :    匹配 任意一个 非数字字符 、等价于  [^0-9]
- \w  :   匹配任意一个 单词字符 、 等价于 [A-Za-z0-9_]  ，  在 python3 中 还可以匹配 中文 
- \W :   匹配任意一个 非单词字符 、 等价于 [^A-Za-z0-9_]  ，  在 python3 中 还可以不能匹配 中文
- \s   :   匹配任意一个 空白符 (空格、  制表符 、 换行符 )
- \S  :    匹配任意一个 非空白字符 
- \b  :    匹配一个单词边界 、需要和其他规则配合使用
- `.`     :  匹配 除 换行符 之外的 其他任意 一个字符
- `\.`     :   匹配 一个 小数点 、 也可以 使用  [.]  来代替

**正则中有特殊含义的符号 要想在字符串中进行匹配 、都需要 使用 \ 进行转移处理 ***

## 多字符匹配规则

- X{m}  :    X 匹配规则 匹配 连续的 m 个字符 
- X{m,} :    X 匹配规则 匹配 至少连续的 m 个字符
- X{m,n} :   X 匹配规则 匹配 至少连续的 m 个字符 ,  最多 不超过 n 个字符

**X 是一个泛指、 代表正则匹配规则 **

## 贪婪式表达式

> 尽可能多的尝试匹配满足条件的数据~~~

- `X*`    ： X 匹配规则  至少 匹配 0个字符 
- `X+`   :   X 匹配规则  至少 匹配 1个字符
- `X?`   :   X 匹配规则  最多 匹配 1个字符

## 非贪婪式表达式

> 尽可能少的尝试匹配满足条件的数据~~~ 
> 
> 在 贪婪式 表达式的 后面 添加一个  `?` ,  形成非贪婪式 表达式

- X*?`    ： X 匹配规则  至少 匹配 0个字符 
- `X+?`    :   X 匹配规则  至少 匹配 1个字符
- `X??`    :   X 匹配规则  最多 匹配 1个字符

## 分组匹配 `()`

- 普通分组 :   在 编写正则表达式的时候，可以将 部分匹配规则  放到 小括号中， 作为一个 组 、整体 、 分组可以让 正则 关心 组匹配的内容， 对组中的内容 起到 检索、 提取 和 替换的 作用 ~~~
  ```
  (1[3-9]\d(\d{4}))\d{4}
  ```
- 命名捕获分组 :    可以给指定的 组添加一个名字 、后期 可以根据 组名 查找 或替换 组中的内容  ， 语法  `(?P<name>regex)`
  ```python
  (1[3-9]\d(?P<middle>\d{4}))\d{4}
  ```
  
  **在 python 中  命名捕获分组 需要使用  ?P<name> 开头 、某些语言 只需要使用  ?<name>  语法**
- 非捕获分组 :   如果 希望某一个 小括号 括起来的匹配规则  不产生 分组 效果 、只当作 整体使用 ， 那么 可以 使用 非捕获分组  
  
  语法 `(?:regex)`
  ```
  1[3-9]\d(?:\d{4}){2}
  ```
- 引用分组 :   引用 指定 组 匹配的内容  作为 该规则匹配的结果 、语法 `\num`   ,  num 代表 的是 组的 序号 、序号 从 1 开始  
  ```python
  \w(\w)\1
  ```

## 选择匹配  `|`

```
(?:(?:1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.){3}(?:1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)
```

## 限定符

> 限定符 通常用来进行数据校验 ~~~

- `^`  :    该符号如果出现在 整个正则表达式的 头部 、代表  以 .... 开头
- $   :    该符号如果出现在 整个正则表达式的 尾部 、代表  以 .... 结尾

## 断言

> 正则在前 、断言在 后、 为 正向 断言  、 反之  为 反向断言 ！！！ 

- 正向确定断言  regex(?=regex)
- 正向否定断言  regex(?!regex)
- 反向确定断言  (?<=regex)regex
- 反向否定断言  (?<!regex)regex

# 正则表达式 修饰符/模式

- i 模式  ：  忽略大小写
- s 模式  ：  也称 dotAll 模式  ,  在 该模式 下，  `.`  可以匹配 任意一个字符
- m 模式 :    该 模式 需要 和  限定符 (^ , $)  配合使用 ， 可以 匹配 多行

## re 模块常见的函数

- re.findall(pattern , string , flags)  ： 查找正则匹配的所有数据、返回一个列表
  > 1. 如果正则中 没有进行分组 、那么返回一个列表 ，列表中存储的是 正则匹配的 字符串
  > 2. 如果 正则中 有且只有 1个 分组 ， 那么返回一个列表 、列表中存储的 正则 第一组匹配的 字符串 
  > 3. 如果正则中有 超过 1个分组、那么 返回一个列表、列表中的每一个元素 是一个元组、且元组中的 每一个值 是对应组匹配的内容

```python
import re 

# 求 字符串中所有连续数字的和
strings = "abc123xys56gdh78"
# 编写一个正则表达式, 提取 字符换中的所有数字 
regex = r"\d+"

# 调用 findall 获取 正则 匹配的内容 
all_nums = re.findall(regex, strings)

print(sum(map(lambda x: int(x) , all_nums)))

# 定义一个字符串、字符串中可能会包含 多个手机号 、要求 提取 所有的手机号 
strings = "145647678958yts453654768741324352436576dgfhd2467687641134546767sdSSsdgfh45463475879ds1345667823567" 

regex = r"(1[3-9]\d(\d{4})\d{4})"
# 分组后、获取 2个组匹配的数据组成的元组
ret = re.findall(regex, strings)

print(ret)

# 提取字符串中所有的连续字母 
regex = r"[a-z]+"
# 使用 I 模式 忽略大小写
print(re.findall(regex, strings, re.I))

strings = """
abc
123
xYz
124xYXx
"""
# 编写一个正则表达式、提取每一行中的纯字母
regex = r"^[a-z]+$"
print(re.findall(regex, strings, re.M | re.I))

```

- finditer(pattern,  strings, flags=0) :  查找正则匹配的所有数据、返回一个迭代器、迭代器中的每一个数据是一个 Match 对象

```python
import re


strings = "145647678958yts453654768741324352436576dgfhd2467687641134546767sdSSsdgfh45463475879ds1345667823567" 
# 编写一个正则表达式、提取字符串中的手机号
regex = r"(?P<prefix>1[3-9]\d(?P<mid>\d{4}))\d{4}"

all_iter = re.finditer(regex, strings) 

# 存储所有的手机号 、前7位 、中4位、并组装为字典
ret = []
# 使用 for 遍历整个结果 
for m in all_iter:
    # print(m.group(1) ,  m.group("prefix"))
    ret.append({"tel": m.group(), **m.groupdict() })
    
print(ret)
```

- search(pattern,  strings,  flags=0) :  从字符串中查找  第一次 正则表达式 匹配的内容，并返回 Match 对象，找不到 返回 None

```python
import re 

strings = "sdf@er3457dfg578w" 

# 编写一个正则表达式、匹配 连续的数字 
regex = r"\d+"

match = re.search(regex, strings) 

# 结果 可能是 None ,也可能是 Match对象
if match is not None:
    # 获取正则匹配的内容
    print(match.group(), match.start(),  match.end())
```

- match(pattern , strings,  flags=0) :    尝试从字符串的头部开始进行匹配，如果匹配 返回 Match 对象， 否则 返回 None
- fullmatch(pattern,  strings,  flags=0)  :   校验正则表达式是否匹配整个字符串， 如果匹配 返回 Match对象， 否则 返回 None 
- split(pattern, string, maxsplit=0, flags=0) ：根据正则表达式 进行字符串的拆分、并获取拆分后的 列表对象
- sub(pattern,  repl,   strings,  count,  flags=0)  :  替换正则表达式的内容为 repl , 并返回 替换后的字符串
- subn(pattern,  repl,   strings,  count,  flags=0)  :  替换正则表达式的内容为 repl , 并返回 替换后的字符串 和替换次数 组成的元组

```python
import re 

# 定义一个字符串
strings = "abfdgd25436ygdbdu46565tgbfmh47685ujn v3ty5ujrn3557ikjm f"

# 将字符串中的所有数字 替换成 * 
regex = r"\d"
# 使用 sub 替换 数据 
ret = re.sub(regex, "*", strings) 
print(ret)

# 将 字符串中 多个连续的 数字 进行替换、替换为 原数字 的 逆序 
regex = r"\d+"

ret = re.sub(regex,  lambda m: m.group()[::-1] , strings)
print(ret)

# 使用正则 将 手机号 的 中间四位 替换成 **** 
strings = "145647678958yts453654768741324352436576dgfhd2467687641134546767sdSSsdgfh45463475879ds1345667823567"

regex = r"(1[3-9]\d)\d{4}(\d{4})"

ret = re.subn(regex, lambda m: m.group(1) + "****" + m.group(2) ,  strings) 

print(ret)
```

### re.Match 对象 常见的方法

- group(n=0)  : 获取正则表达式指定组匹配的内容
- start(n=0)  : 获取正则表达式 匹配的内容的 起始索引值 
- end(n=0)  :  获取正则表达式 匹配的内容的 结束索引值
- span(n=0) :  获取正则表达式 匹配的内容的 起始索引值 和 结束索引值组成的元组 
- groups():   获取正则表达式 每一组 匹配的内容 组成的元组
- groupdict() :  获取正则表达式中 命名捕获分组 匹配的内容组成的 字典

**n  代表的是 正则中的分组序号、 也可以是 组的名字、 默认0 代表 获取 整个正则匹配的数据 **

# pip 镜像源配置

window 操作系统:   在 当前用户根目录下 、新建一个 pip 文件夹、 在 pip 文件夹下、新建一个  pip.ini 文件，并添加如下内容

```python
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
```

# requests 库

- 安装 requests 库
  ```
  pip  install requests
  ```
- 读取指定 url 、并 获取结果
  ```python
  headers = {
      # "referer": "https://www.qu05.cc",   # 添加防盗链 反反扒措施
      # 添加用户身份代理信息
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
  }
  
  # 发起一个 请求 、获取 对应网址的资源、并返回一个 response 对象
  response = requests.get("https://www.qu05.cc/html/42900/", headers=headers)
  
  print(response.status_code)
  # 获取 返回的结果 ， 状态码 200 ~ 300之间 代表成功
  if 200 <= response.status_code < 300:
      # 获取网址对应的数据
      content = response.text
      # 编写一个正则表达式
      regex = r'<dd><a\s+href\s*=".*?">(.*?)</a></dd>'
  
      # 使用 findall 获取所有的章节
      data = re.findall(regex, content, re.I)
      print(data)
  
  else:
      print("网址解析失败、请检查代码、增加反反爬措置")
  ```
  
   **user-agent 和 referer 都可以在 浏览器 F12 调试工具 网络 请求头信息中找到 ！！！**

# 包 Package

package 包 是用来 管理模块的特殊文件夹、该文件夹下 存放了一个 `__init__.py`模块 、导入包会自动加载初始 `__init__.py` 中的代码

##  导入 

- import  :   导入模块

> 在 模块 上下文中 书写的代码， 会在 导入 模块的时候 自动执行
> 
> 一个 模块 可以被 导入 多次 、 但 模块 上下文中的 代码 只会在 第一次导入的时候 执行一次 ~~~

```python
import re 

# 导入 xyz.qikux 包下的 test 模块、并设置别名 test
import xyz.qikux.test as test
```

- from  ...  import

> 可以导入 包 , 模块 , 模块中的 函数、类、全局变量等、 还支持 使用 `*`  一次性导入模块中所有的数据 
> 
> 支持 相对导入 、相对导入只能导入 自己项目中 书写的模块、且 两个模块之间必须 有相同的 顶层包(祖宗包)， 使用相对导入的模块不能作为程序运行的入口。
> 
> 程序运行的入口 模块 被称为 顶层模块 、顶层模块的 名字 叫 `__main__`  
> 
> 在模块中书写的 测试代码 推荐 写到  `if  __name__   = "__main__"：` 中
