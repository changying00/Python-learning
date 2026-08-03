"""
re.finditer(pattern, string, flags):  查找所有正则匹配的内容、并返回一个 迭代器 、且 迭代器中 每一个数据是一个 Match 对象

Match 对象 有哪些 常见的操作

    - group(n=0)  :  获取正则表达式 指定组匹配的内容， 默认 为 整个正则匹配的内容

        n 也支持传入 组名

    - groups() :  获取正则表达式 每一个组 匹配的内容 组成的 元组 对象

    - groupdict() : 获取正则表达式 中 所有 命名捕获分组 匹配的内容组成的 字典对象

    - start(n=0) :  获取正则表达式 匹配的内容的 起始索引位置

    - end(n=0) :    获取正则表达式 匹配的内容的 结束索引位置(不包含)、满足 end - start = length

    - span(n=0) :   获取正则表达式 匹配的内容的 起始索引和结束索引位置 组成的 元组对象

"""
import re

strings = "133037018532758973750319937063398"
#编写一个正则表达式、用来 提取字符串中所有的手机号、且对手机号 进行分组、第一组 表示手机号的前七位、第二组表示表示手机号的中间四位
regex = r"(?P<o1>1[3-9]\d(\d{4}))\d{4}"

iters = re.finditer(regex,strings)
#使用next 获取第一个匹配的元素
match = next(iters)
# ls = []
# for value in iters:
#     ls.append(value)
# print(ls)
#获取正则表达式 匹配的手机号
print(match.group(),match.group(1),match.group(2),match.group("o1"))
print(match.groups())
print(match.groupdict())
print(match.start(),match.start(1),match.start(2),match.start("o1"))
print(match.end(),match.end(1),match.end(2),match.end("o1"))
print(match.span(),match.span(1),match.span(2),match.span("o1"))