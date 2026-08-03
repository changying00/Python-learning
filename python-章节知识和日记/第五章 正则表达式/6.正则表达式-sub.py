"""
re.sub(pattern, repl, string, count=0, flags=0)  :  将 正则表达式 匹配的内容 进行 替换，替换成 repl 、并返回 替换后的 字符串
    pattern:  正则表达式
    repl :
        a)  普通字符串、代表 要 替换的内容
        b)  包含 \num 的字符串、会获取 正则指定组的内容 并进行替换
        c)  功能型函数、 消费一个 匹配的 match 对象、返回一个 要替换的 字符串

    string :  要处理的 字符串
    count :  要 替换的次数 、默认 替换所有 。
    flags :  设置 正则匹配的模式 、 I, M , S

re.subn(pattern, repl, string, count=0, flags=0) :  用法 参考 sub, 返回一个长度为 2的 元组 、第一个值代表替换后的字符串、第二个值代表替换的次数
"""

import re

# 定义一个字符串
string = "我的 QQ号是 47243466, 手机号是 15467514353。"
# 编写 一个正则表达式 、匹配 字符串的所有数字 、
regex = r"\d+"
# 将 字符串中 所有敏感的数字 全部替换成 *****
print(re.sub(regex, "******", string))
# 编写一个正则表达式 、匹配 手机号、且 将 前三位 和 后四位 进行分组
regex2 = r"(1[3-9]\d)\d{4}(\d{4})"
# 将 字符串中的 手机号 中间 四位 隐藏、并替换成 ****
print(re.sub(regex2, r"\1****\2", string))
# 编写一个正则表达式 、匹配 字符串中所有的数字
# 将 字符串中 所有 匹配的 数字 倒序输出
print(re.sub(regex, lambda d: d.group()[::-1], string))
