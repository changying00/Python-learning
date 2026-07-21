#【递归题】创建一个递归函数，将正整数整数转换为二进制字符串。
# 思路：
# 一个正整数整数的二进制  =  这个数 右移 1位 的 二进制 + 个位数 % 2
# 收敛条件:  数字 0 的二进制是 0
"""
        num =  num >> 1 + num  % 2
        num >>1 = num >> 2 +  num  % 2
        num >>2 = num >> 3 + num  % 2
        ...
"""
def get_bin(num):
        if num == 0:
            return ""
        return get_bin(num >> 1) + str(num % 2)
# get_bin(8)
# = get_bin(4) + "0"
# = get_bin(2) + "0" + "0"
# = get_bin(1) + "0" + "0" + "0"
# = "1" + "0" + "0" + "0"
# = "1000"
print(get_bin(25))

