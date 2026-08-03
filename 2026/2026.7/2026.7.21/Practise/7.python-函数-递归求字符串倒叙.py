#【递归题】编写一个递归函数reverse_str(n) 将一个字符串 倒序输出。
# 思路:
# 一个数字的倒序 =  尾部字符 和 除尾部字符外的其它字符组成的字符串的倒叙拼接。
# 收敛条件:  空字符串 还是 空字符串。
def reverser_str(strings):
    if len(strings) < 1:
        return strings
    return reverser_str(strings[1:]) + strings[0]
"""strings ="dgx110" --》 011xgd
                     --》 gx110 + d
                     --》 x110 + g
"""
print(reverser_str("dgx110"))