# 异常

程序出现的错误 被称为 异常 。所有异常的父类 是 BaseException ,  BaseException 有一个非常重要的子类 Exception ,  通常 可以使用 Exception 类 来代替 BaseException 。 

## 常见的异常类 

IndexError  :  索引错误

TypeError   :   类型错误 

NameError :   名字错误

KeyError  :   键错误

ValueError :   值错误 

SyntaxError :   语法错误

ZeroDivisionError ：  除数不能为0的错误

ArithmeticError  ：  算术错误

## 异常的特点

程序一旦产生异常、 如果没有处理异常的代码， 那么 异常会抛给 上层调用者 、直到 抛给 python解析器，此时会显示错误的异常栈信息、并   会立即终止程序的调用 ， 在整个异常产生的过程中， 只要有任意一个地方 进行了 异常处理 、那么 异常就不再 向上抛， 也不会终止程序的运行 。

## 异常的处理

- try - except 结构 
  - try :    将 可能会产生异常的代码 放到 try 块中 ， 去捕获 可能存在的异常 
  - except :    捕获 并处理 指定的异常、 如果 没有指定要 捕获哪一种异常， 则 默认捕获 所有异常 ！

***except 结构可以出现多次， 多个 except 要保证 子类异常处理在 前 、父类异常处理 在 后**

```python
try:
    x = int(input("请输入一个整数"))
    y = int(input("请输入一个整数"))
    a = x / y
    print(a)
    dct = {"name": "张三", "age": 20}
    print(dct["birth"])

except KeyError as e:
    # 捕获 值错误异常, 可以使用 e.args[0] 获取异常的错误消息，
    # as e 可以省略， 如果省略，则无法获取异常错误对象
    print("输入的键有误", e.args[0])

except (ZeroDivisionError, ValueError) as e:
    # 捕获多种异常并处理异常, 可以使用 str函数将异常对象转成字符串，获取异常错误消息
    print("异常已被处理", str(e))

except:
    # 如果 except 没有明确设置捕获的异常，则默认处理剩余的所有异常
    # 此时 无法 获取 异常错误 对象
    print("未知错误！！！")


print("异常处理后执行的代码")
```

- try - except - else 结构 
  - else :   当 try 块中的代码 没有产生异常 才会 执行的代码
- try - except - finally 结构 
  - finally  :   当执行了 try 中的代码， finally  一定会被执行 ，通常用来释放资源 、关闭 链接、 通道 等信息
- try - finally  :   不是用来处理异常的， 只是用来 释放资源的

## 手动抛出异常

```python
try:
    a = 3 / 0
except:
    raise Exception("除数不能为0") 
```

## 断言

`assert condtion, message`   :  断言条件 不成立 、抛出  AssertionError 异常、 错误信息为 message 

```python
import re

month = input("请输入一个月份")

assert re.fullmatch(r"\d+", month), "月份必须是一个整数"

# 将其转成整数
month = int(month)

# 断言月份在 1 ~ 12 之间 
assert month in range(1, 13), "月份值的范围必须是 1 ~ 12"

# 求当月的最大天数
print("=========================")
```

## 自定义异常

编写一个类、继承 一个已知的 异常类 ，那么这个类 就成为了 异常类、  没有特殊要求的情况下， 建议 继承 Exception 类 

```python
class QikuException(Exception):
    pass
```

# 日志模块 logging

> 日志 对于一个系统而言 是非常重要的、 我们通常 在系统中 都需要 记录日志，可以通过 日志 进行 追踪和问题排查 ~~~ 
> 
> 可以 针对不同的 运行环境 显示 不同级别的日志 、例如 开发环境下 显示 较多的日志 ， 生产环境 只显示错误日志 。

## 日志级别 

- DEBUG  :   调式 、 级别最低、 输出最多的日志 、会输出 DEBUG 、INFO 、WARNING、ERROR 等级别 的错误 

- INFO ： 通知 、比 DEBUG 级别高 、通常 输出一些 业务流程日志 。

- WARNING :  警告 、比 INFO 级别高 

- ERROR :  错误 、比 WARNING  级别高 

**级别越高、输出的日志信息越少**

## 日志输出目的地

- 控制台  console
- 文件     file
- 邮件     email
- 数据库  db

## 日志输出格式

- %(levelname)s  :   显示日志级别 
- %(asctime)s   :    日志 产生的 时间 
- %(pathname)s  :  调用日志记录函数的源文件的完整路径名
- %(filename)s     调用日志记录函数的源文件名
- %(lineno)d    	 调用日志记录函数的源代码行号
- %(message)s    日志消息

## 编写日志配置文件

```ini
[loggers]
# 设置 logger 、默认需要提供一个 root 
keys=root,sampleLogger

[handlers]
# 设置处理器、可以设置多个
keys=console

[formatters]
# 设置格式化方式、可以配置多个
keys=simple

[logger_root]
# 配置 root logger 处理的日志级别为 ERROR, 且输出到 控制台目的地
level=ERROR
handlers=console

[logger_sampleLogger]
# 配置 sampleLogger logger 处理的日志级别为 INFO, 且输出到 控制台目的地
level=INFO
handlers=console
# 设置 logger 的名字、使用 getLogger 传入的名字、如果名字未找到，默认使用 root logger
qualname=sampleLogger 
# 该 logger 处理完日志消息后，不会将消息传递给它的父 logger, 如果为 1 或者 True, 会继续交给父Logger进行处理
propagate=0

[handler_console]
# 设置 控制台目的地 
class=StreamHandler
# 设置控制台的默认日志级别、会被 logger 中设置的级别 覆盖
level=DEBUG
# 设置日志采用的格式化方式
formatter=simple
# 设置 StreamHandler 需要用到的参数
args=(sys.stdout,)


[formatter_simple]
# 设置日志的格式化样式
format= 【%(levelname)s】%(asctime)s - %(pathname)s - %(filename)s - %(message)s
# 对 asctime 进行日期格式化处理
datefmt= %Y-%m-%d %H:%M:%S
```

## 程序读取配置文件、并输出日志信息

```python
import logging
import logging.config
import os 

path = os.path.join(os.path.dirname(__file__), "logging.conf")

# 读取 日志的 配置文件 
logging.config.fileConfig(path, encoding="utf-8")

# 获取 日志 logger 对象 
logger = logging.getLogger("sampleLogger")

# 打印日志信息
logger.debug("我是一个debug日志")
logger.info("我是一个info日志")
logger.warning("我是一个warning日志")
logger.error("我是一个error日志")
```
