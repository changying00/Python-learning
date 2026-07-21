#【递归】使用递归实现 2 + 4 + 6 + 8 + 10 + .... n个偶数的和
"""
    n 个 偶数的和 = 第n个 偶数 + 前 n -1 个偶数之和
    前n - 1 个偶数之和 = 第 n - 1个偶数 + 前 n -2 个 偶数之和
    .....
    .....
    前三个偶数之和  =  第三个偶数  +  前俩个偶数之和
    前二个偶数之和  =  第二个偶数  +  前一个偶数之和
    第一个偶数之和   =  第一个偶数

    第n    个偶数    =  第 n - 1 个偶数 + 2
    第n - 1 个偶数   =  第 n - 2 个偶数 + 2
    ......
    .....
    第 3 个偶数 = 第 2 个偶数  + 2
    第 2 个偶数 = 第 1 个 偶数 + 2
    第 1个 偶数 = 2
"""
#方法一先算 第n个偶数是多少，然后算n个偶数之和分俩个函数实现
def get_even(n):
    if n == 1:
        return 2
    return get_even(n-1) + 2

def get_even_count(n):
    if n == 1:
        return 2
    return get_even(n) + get_even_count(n-1)
print(get_even_count(8)) #2 + 4 + 6 + 8 +10 +12 +14 +16 = 72

#方法2  直接计算
def get_even_number(n, a = 2):
    if n == 1:
        return a
    return a + get_even_number(n - 1, a + 2)
print(get_even_number(8))