






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