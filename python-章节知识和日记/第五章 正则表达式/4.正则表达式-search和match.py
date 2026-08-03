"""
re.search(pattern,string,flags= 0):从 字符串 提取 满足正则表达式匹配的第一个数据、并返回一个Match对象、如果找不到、返回None

re.match(pattern,string,flags=0): 提取 字符串以 指定 正则表达式匹配的内容开头 的第一个数据、并返回Match对象、如果找不到、返回None
    match 强调 匹配的内容在字符串中 作为开头

re.fullmatch(pattern,string,flags= 0)：正则表达式 如果 完全匹配字符串、则返回一个Match 对象、否则返回 None
    fullmatch 强调 匹配的 内容为整个 字符串

fullmatch 可以实现数据校验、match 和 fullmatch 配合M模式 没有意义(字符串为多行那种)，如果正则表达式加上 ^ 和 $ 后缀也能匹配

"""
import re


string = "123开始了和对方的话，hsfs232的考试g43dch57"

# 编写一个正则表达式，提取 字符串中 第一个匹配的 数字
regex = r"\d+"
# 尝试 提取 第一个满足条件的数据
# m = re.search(regex, string)
# m = re.match(regex, string)
m = re.fullmatch(regex, string)
if m is not None:
    # 获取匹配的内容
    print(m.group())
print(m)
strings = """
https://www.baidu.com/images/xx.jpg
https://www.baidu.com/images/xx.jpg2
https://www.baidu.com/images/xx.jpeg
https://www.baidu.com/images/xx.gif
https://www.baidu.com/images/xx.doc
https://www.baidu.com/images/xx.pdg
https://www.baidu.com/images/xx.txt
"""
# 编写一个正则表达式、提取 字符串中 每一行 表示 图片路径的 数据
regex = r"^.+\.(?:jpe?g|png|gif|bmp)$"
print(re.findall(regex, strings, re.M))
