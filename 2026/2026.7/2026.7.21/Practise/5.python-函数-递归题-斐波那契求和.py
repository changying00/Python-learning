#【递归】使用递归算法 计算 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21+ 34 + 55 ... n 个数字的和

"""
   n个数字之和 = 第n个数字 + 前 n -1 之和
   前n -1 之和 = 第 n -1个数字 + 前 n -2 之和
   前n - 2 之和 = 第n -2个数字 + 前 n -3 之和
   ......
   ......
   前三项之和  = 第3项数字 + 前二项之和
   前二项之和  = 第 2 项数字 + 第一项数字之和
   前一项之和 =  第 1 项数字
"""
#先求斐波那契数列的第n个数字
def get_fac_num(n):
    if n in [1,2]:
        return 1
    return get_fac_num(n-1) + get_fac_num(n-2)
#在求斐波那契额前n项和
def get_count_num(n):
    if n == 1:
        return 1
    return get_fac_num(n) + get_count_num(n-1)
print(get_count_num(20))
