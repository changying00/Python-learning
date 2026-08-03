# 字符串

>  字符串 是编程语言中用来表示 一段文本内容的数据类型、通常使用 单引号、双引号、三引号(三单引号、三双引号)标识
> 
> 字符串是 不可变的 数据类型 ，  字符串 是 可迭代 对象 。

## 字符串的定义方式

- 字面量定义方式
  ```python
  # 将 字符串 以多行代码的形式 表示
  #   1. 将 多行代码表示的字符串 添加 一个 小括号 括起来
  #   2. 将 多行代码表示的字符串 每一行的 尾部 添加一个 `\`
  string = 'abc盛大官方电话给发给开发商的共和党国会和' \
           '十三点和客户是德国函数的华盛顿和水果蛋糕深刻'
           
  
  string1 = ('abc盛大官方电话给发给开发商的共和党国会和'
             '十三点和客户是德国函数的华盛顿和水果蛋糕深刻')
             
  
  # 三个引号 会保留 换行符
  string2 = """
      abc盛大官方电话给发给开发商的共和党国会和
      十三点和客户是德国函数的华盛顿和水果蛋糕深刻
  """
  
  print(string is string1)
  
  print(string is not string2)
  
  
  # 使用 unicode 编码 定义的字符串
  string3 = u"hello \u2ec3"
  
  print(string3)
  ```
- str 函数 ：  该函数可以将任意数据转成字符串

## 特殊字符

- 字符串中 使用引号 
  ```python
  # 输出 一个 I'm Chinese
  # 如果 字符串中 出现 单引号 、此时 字符串 定义的时候， 可以使用 双引号 、三引号 来代替
  string = "I'm Chinese"
  print(string)
  
  # 输出一个 我"喜欢"你 ,
  # 如果 字符串中 出现 双引号 、此时 字符串 定义的时候， 可以使用 单引号 、三引号 来代替
  string2 = """我"喜欢"你"""
  
  print(string2)
  # 如果一个 文本内容 即包含 单引号 ，又 包含 双引号
  # 输出 一个 I'm Chinese, 我"喜欢"你 ,
  # 如果 字符串中 出现 单引号、双引号 、此时 字符串 定义的时候， 可以使用 三引号 来代替
  string3 = '''I'm Chinese, 我"喜欢"你'''
  print(string3)
  
  # 如果一个字符串 中 可能出现单引号、也可能出现双引号、还可能出现 三引号
  # 此时 在 字符串中出现的 特殊引号(和定义的引号冲突) 、可以使用 `\`  进行转义处理， `\` 可以让指定的符号保持原意
  string4 = "I'm Chinese, 我\"喜欢\"你"
  
  print(string4)
  ```
- 字符串中 使用 反斜杠
  ```python
  # 反斜杠 有特殊含义、代表转义符， 那么此时 会出现错误 反斜杠u 会代表特殊含义 unicode 编码，导致解释失败
  # strings = "我的个人头像地址在： C:\Users\admin\Desktop\avatar.jpg"
  # 解决方案1 :  对 反斜杠 进行转义处理
  strings = "我的个人头像地址在： C:\\Users\\admin\\Desktop\\avatar.jpg"
  print(strings)
  
  # 解决方案2 :  可以在 字符串的头部 添加一个 `r` 前缀
  strings = r"我的个人头像地址在： C:\Users\admin\Desktop\avatar.jpg"
  print(strings)
  ```

## 常见的运算符

- 算术运算符   `+`  ,   `*` 
  >  字符串 和  字符串 之间 支持 使用  加法运算、 进行 2个字符串 的拼接 
  > 
  > 字符串 和  整数 n  支持 乘法运算 、 将 字符串内容 重复 n 次
  ```python
  str1 = "hello"
  str2 = "world"
  
  print(str1 + str2)
  
  print(str1 * 3) 
  
  """
      2 + 22 + 222 + 2222 + 22222 的和
  """
  c = input("从键盘上输出一个0 ~ 9 数字")
  n = int(input("输入一个整数 n、代表 前 n 项的和"))
  # 定义一个变量、用来存储最终的计算结果 
  
  s = 0
  
  for x in range(n):
      s += int(c * (x + 1))
  
  print(s)
  
  ```
- 关系运算符 :   > ,  >= ,  <,   <= ,  == ,  !=
- 成员运算符 :   in   ,   not  in

## 字符串的遍历方式

> 字符串 是由 多个字符组成的文本内容， 支持 通过 `索引` 的方式 来 获取数据 、支持使用 len 内置函数 获取字符串的长度 、
> 
> 所以 字符串 常见的遍历方式有  基于索引的遍历方法、  基于 值得遍历方式 、  基于 索引和值的遍历方式

- 基于 索引的遍历方式

```python
string = "hello"

for i in range(len(string)):
    print(string[i])
```

- 基于 值 的遍历 方式 
  ```python
  string = "hello"
  
  for v in string:
      print(v)
  ```
- 基于 索引 和 值的遍历方式
  ```python
  string = "hello"
  
  for index, v in enumerate(string):
      print(index, v)
  ```

## 字符串的切片

>  语法 `[start:end:step]`
> 
> 字符串是不可变的、只支持使用切片技术 提取数据、不支持 修改和删除数据 、具体用法参考列表

## 字符串的格式化

> 字符串 拼接 可以使用 `+` 进行拼接 (仅支持2个字符串进行拼接)、在 进行 字符串数据展示的时候，可能部分数据 需要调整格式， 此时 就可以使用 字符串格式化技术 对要处理 的字符串 进行 格式化操作 ！！！

- % 占位符 进行格式化  (天生具备的能力、仿 C 语言设计的)
- format 方法 进行化  (Python2.6X 版本开始支持)
- f-string 格式化 (Python3.6X 版本开始支持)

###  % 占位符 

> 语法： ` %[(name)][对齐方式][填充宽度][.精度]类型`
> 
> (name) :  给占位符 设置一个关键字 、传参的时候 需要用到 设置的关键字 、 该参数 可有 可无 
> 
> 对齐方式 :   默认采用 右对齐 、左补空格 ~~~
> 
> ```
> `+`  ： 右对齐 、如果数字是正数、且 填充的内容 不够 、左边会多出一个 `+` 符号 
> 
> `-`  :   左对齐 
> 
> `0`   :    右对齐 、前面补  0 
> ```
> 
> 填充宽度 ：  设置 字符串占用的宽度 、当 实际字符串 宽度 不够的时候， 对其方式 和 填充字符 才会生效 ~~
> 
> `.`精度 ：   如果 数据是 字符串，代表 截取字符串的 长度 、 如果是 数字，代表 保留 几位小数 
> 
> 类型 ：  s (字符串) 、 d  (整数) 、  f (浮点数) 、  o (八进制) 、  x (十六进制)

```python
a = 7 
b = 9 

# 不带关键字的占位符 传值 使用 元组 传值
strings = "%02d * %-5.2f = %d" % (a, b, a * b) 
print(strings)

# 带有关键字的占位符 传值的时候 必须 使用 字典格式
strings = "%(a)02d * %(b)02d = %(c)02d" % {"a": a , "b": b, "c": a * b}
print(strings)

c = 234
print("%d的八进制是%o, 十六进制是 %x" % (c, c, c))

strings = "hello"
# 如果只有 一个占位符 ，则传值的时候 小括号 可以省略
print("%.2s 你好!" % strings)

```

**在 使用 % 进行格式化字符串的时候， 如果 字符串中 需要 表示 %,  则 需要 使用  %%  进行转义 **

```python
# 获取一个字符串、字符串的内容是 我叫小明，本次考试成绩为 95， 比上次增长 12% 
text = "我叫小明，本次考试成绩为 %d， 比上次增长 %d%%" % (score, rate)
print(text)
```

###  format 方法

- 基本使用方法  
  ```python
  a = 7
  b = 9
  # 输出 7 * 9 = 63
  strings = "{} * {} = {}".format(a, b, a * b)
  print(strings)
  
  strings = "{1} * {0} = {2}".format(a, b, a * b)
  print(strings)
  
  strings = "{x} * {y} = {z}".format(x=a, y=b, z=a * b)
  print(strings)
  
  strings = "{0} * {1} = {x}".format(a, b, x=a * b)
  print(strings)
  ```
  
    **使用 {} 进行占位，  {} 中 支持 传入 索引 和 关键字 、索引参数 通过 format的位置参数传入， 关键字通过 关键字参数传入 **
- 高级使用方法 
  > 语法 :     `{  [index|keyword] : [填充的单字符] [对齐方式] [填充的宽度] [数字分隔符 , ] [.精度] [类型]   }`
  > 
  > 填充的单字符  :   设置 对其后 填充的 字符、 此处设置的 必须是 单字符 、默认值 是 空格
  > 
  >  对齐方式 :  
  > 
  > ```
  > `<`  :   左对齐
  > 
  > `>`   :   右对齐
  > 
  > `^`  :   居中对齐 
  > ```
  > 
  > 填充的宽度 ：   设置 字符串占用的宽度 、当 实际字符串 宽度 不够的时候， 对其方式 和 填充字符 才会生效 ~~
  > 
  > 数字分隔符  :   在 对 数字 进行格式化的时候， 数字 会 每 三位 添加一个 逗号
  > 
  > `.精度`   :    如果 数据是 字符串，代表 截取字符串的 长度 、 如果是 数字，代表 保留 几位小数, 且 类型必须设置为 f 
  > 
  > 类型 ：  不常用， 一般 只用 `f` 
  ```python
  a = 7
  b = 93453635
  
  # 输出 7 * 9 = 63
  strings = "{:0^10.2f} * {:,} = {:,.5f}".format(a, b, a * b)
  print(strings)
  ```

 **在基本使用方法的基础上 添加 冒号 ， 后面写 高级 格式化 代码即可**

###  f-string 

> 语法 : `{ exp : [填充的单字符] [对齐方式] [填充的宽度] [数字分隔符 , ] [.精度] [类型]   }`
> 
> exp  表示的是 python 表达式 、 字符串的前缀 必须添加  `f` 

- 基本使用方法
  ```python
  def test(x):
      return x * 10
  
  
  a = 7
  b = 9
  
  string = f"{a} * {test(b)} = {a * b}"
  
  print(string)
  
  string = "hello"
  print(f"{string}的倒序内容是{string[::-1]}")
  
  ```
- 高级使用方式 ： 参考 format 的高级使用方式

## 字符串常见的方法

###  大小写转换方法

- upper()  :   将 字符串中的所有 字母 转成 大写 
- lower()   :   将  字符串中的所有 字母转成 小写
- capitalize()  :  将 字符串的 首字母转大写、  其他字母转小写
- title()   :    将 每一个单词的首字母 转 大写 、其他字母转小写 
- swapcase()  :   将 字符串中的 大小写 互换 ~~
  ```python
  strings = "hello world ! I'm Chinese" 
  
  # 将字符串转大写
  print(strings.upper()) 
  
  # 将字符串转小写
  print(strings.lower()) 
  
  # 将字符串 首字母 转大写
  print(strings.capitalize())
  
  # 将 字符串每一个单词的首字母 转大小 
  print(strings.title())
  
  # 将 字符串 中的大小写 互换 
  print(strings.swapcase())
  
  # 判断 一个字符串中的字母是否是全大写
  print(strings.upper() == strings) 
  ```

### 对齐和填充方法

- ljust(width,   fillchar=' ')  :   左对齐 、右填充 , 默认填充空格
- rjust(width,   fillchar=' ')  :   右对齐、左填充, 默认填充空格
- center(width,  fillchar=' ') :   居中对齐, 默认填充空格
  ```python
  strings = "hello"
  
  print(strings.ljust(10, "x"))
  print(strings.rjust(10))
  print(strings.center(10, "x"))
  ```

### 去除字符串前/后字符

- lstrip(chars=None)  :    去除 字符串 左边 指定的 字符前缀 、默认是 空格 
- rstrip(chars=None)  :    去除 字符串 右边 指定的 字符后缀 、默认是 空格
- strip(chars=None)  :      去除 字符串 前/后 指定的 字符 、默认是 空格
- removeprefix(substr)  :   去除字符串 指定的 前缀 
- removesuffix(substr)   :   去除字符串 指定的 后缀
  ```python
  string = "       hello     "
  
  # 去除左边空格
  print(string.lstrip(),  len(string.lstrip()))
  # 去除右边空格
  print(string.rstrip())
  # 去除前后两边空格
  print(string.strip(), len(string.strip()))
  
  
  string = "xyzhelloyzx" 
  
  # 去除 字符串左侧的 x, y, z 字符 
  print(string.lstrip("zyx"))
  # 去除 字符串右侧的 x, y, z 字符 
  print(string.rstrip("zyx"))
  # 去除 前后 x, y, z 
  print(string.strip("xyz"))
  
  # 移除 字符串 前缀 xyz
  print(string.removeprefix("xyz"))
  # 移除 指定的 后缀 yzx
  print(string.removesuffix("yzx"))
  
  ```

### 查找和替换

- index(sub,  start ? ,   end ?)  :   从指定区间 start ~ end 查找 第一次出现 sub子串的 索引位置、如果找不到，则报错 ！！！
- rindex(sub, start ？,  end ?)  :   从指定区间 start ~ end 查找 最后一次出现的 sub字串的索引位置，找不到 报错！！！
- find(sub,  start ?  , end ? ) :  从指定区间 start ~ end 查找 第一次出现 sub子串的 索引位置、找不到 返回  -1
- rfind(sub, start? , end ?) :   从指定区间 start ~ end 查找 最后一次出现的 sub字串的索引位置，找不到 返回  -1
- count(sub, start? , end ? )  :   从指定区间 start ~ end  获取 sub 子串 在区间内出现的次数 
- replace(old,  new ,  count=-1)  :   将 字符串中的 old 替换成 new,  默认替换全部， 如果指定 count , 可以设置替换次数
  ```python
  string = "hello qiku , hello everyone"
  
  # 查找 el 在 字符串中第一次出现的索引位置 
  # print(string.index("el", 3)) 
  # print(string.rindex("el", 3,  -15)) 
  
  print(string.find("el", 3)) 
  print(string.rfind("el", 3,  -15)) 
  
  print(string.count("el", 3 , -15))
  
  # 将 字符串中的 el 全部替换成 *** 
  print(string.replace("el", "***"))
  
  # 将 字符串中的 el 替换第一个 
  print(string.replace("el", "***",  1))
  
  ```

### 拆分和合并

- split(sep,   maxsplit=-1)  :  将 字符串 按照 指定的 分割符 sep (默认是 空白符)  进行拆分,  返回一个 列表对象
- rsplit(sep ,  maxsplit=-1)  :  将 字符串 按照 指定的 分割符 sep (默认是 空白符)  从 右向左 进行拆分
- splitlines(keepends=False) :  按照换行符 进行字符串拆分 、keepends 用来设置是否保留换行符 。
- join(iterable)  :  将一个可迭代对象中的数据(数据的类型必须是 字符串) 按照 指定的 字符 进行 合并 
  ```python
  # 定义一个字符串 
  strings = "1,2,3,4,5,6,7,8"
  
  # 按照 逗号 将字符串 进行拆分 、返回一个列表 
  print(strings.split(",")) 
  
  # 按照 逗号进行拆分、最多拆分 2次 
  print(strings.split(",", 2)) 
  
  # 按照 逗号进行拆分、从 右边拆分 最多2次
  print(strings.rsplit(",", 2))
  
  strings = """
      abc
      123
      xyz
  """
  # 按照 换行符  进行拆分、且 不保留 换行符 
  print(strings.splitlines(keepends=False))
  
  ls = ["1", "2", "3", "4"]
  
  # 将列表中的数据 使用 :: 进行合并 
  print("::".join(ls)) 
  
  # 将 列表 [1, 2, 3, 4] 转成  1:2:3:4 
  ls = [1, 2, 3, 4]
  # 需要先将 列表中的数据映射为 字符串，才能使用 join 合并
  print(":".join(map(lambda x: str(x) ,ls)))
  ```

### 编码和解码

- encode(encoding = 'utf-8') :   将 字符串 以 指定编码的方式 转成 二进制流 数据
  ```python
  strings = "hello中国"
  
  # 将字符串转成 二进制流 bytes 数据 （方便数据在网络间进行传输）
  #  二进制流 只支持 ascii 范围内的字符, 超出范围字符 必须使用 16进制表示
  # utf-8 编码 一个汉字 占用 3个字节
  str_bytes = strings.encode('utf-8')
  print(str_bytes)
  # 二进制流中 提供一个 decode 方法 ，可以将 二进制流转成 字符串 
  text = str_bytes.decode('utf-8') 
  print(text) 
  
  # gbk 编码 一个汉字 占用 2个字节
  str_bytes = strings.encode('gbk') 
  print(str_bytes) 
  text =  str_bytes.decode("gbk")
  print(text) 
  
  # 使用 unicode 编码 字符串 
  str_bytes = strings.encode("unicode_escape")
  print(str_bytes) 
  
  text = str_bytes.decode("unicode_escape")
  print(text)
  ```

**二进制流数据以  b 开头 、  unicde 编码的字符串 以  u 开头 **

### base64 编解码

> 字符串 是用来表示 文本内容， 二进制流 是用来 表示 流数据的，在 网络中 进行数据传输的时候 通常为了保证数据的安全性， 需要对数据 进行 base64编码 
> 
> base64 技术 最早应用于 邮件的 发送 上 、常见的使用场景有  邮件发送 、 签名认证 、 图片的存储 、下载软件路径的转码等 。

```python
import base64

strings = "hello + ?sdf" 

# 使用 base64 对 二进制流 进行编码 、并将 编码后的 结果(二进制流) 进行 解码 
ret = base64.b64encode(strings.encode()).decode()

# 输出 编码后的字符串 
print(ret) 

# 将编码后的内容 进行 base64解码 获取原数据 
text = base64.b64decode(ret.encode()).decode()

print(text) 
```

### 判断方法

- isupper()  :  判断字符串中的 字母是否全是大写
- islower()  :  判断 字符串中的 字母是否全部小写 
- istitle()  :   判断 字符串是否是 标题 (每个单词首字母大写、其他字母小写) 
- isalpha() :   判断 字符串是否是 纯 字母 组成 
- isdigit()  :   判断 字符串是否是 纯 数字 组成
- startswith(sub)  :  判断 字符串是否 以  指定 sub 开头 
- endswith(sub) :   判断 字符串是否 以  指定 sub 结尾