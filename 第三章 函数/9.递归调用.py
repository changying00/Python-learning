""""
    递归:在定义 函数的时候、函数体 中调用了自己 、这个现象被称为递归调用
    在python 中、递归 是由默认 深度的 、默认值为1000
    递归 性能 是非常差的、在实际工作中 、能用 循环解决的任务、不建议使用 递归实现

    如果 想要 掌握递归调用、需要掌握 递归的三要素

        a) 必须 完全 了就 递归函数 本身的意义

        b) 找到 递归的 解题思路

        c) 必须 找到 递归的收敛(停止递归调用)条件
"""
"""
 已知 1 ，1，2，3，5，8....
 求第20项的数字
 由上面的推导，
 第20项数字 = 第19项数字 + 第18项数字
 第19项数字 = 第18项数字 + 第17项数字
 第18项数字 = 第17项数字 + 第16项数字
 ...
 ...
 ...
 第三项数字 = 第二项数字 + 第一项数字
 第二项数字 = 1
 第一项数字 = 1

"""
def get_fac_num(n):
    if n in [1,2]:
        return 1
    return get_fac_num(n-1) + get_fac_num(n-2)
print(get_fac_num(10))

#练习题:使用 递归 将一个字符串 进行反转
"""
    比如传入一个字符串string = "dgx2541104422"，len(string) = 13
    反转        2244011452xgd
    反转完成 =      剩下         + d 
        if i == 0:
            return sting[0]
    return get_re_sting[i] + get_re_sting[i-1]
"""
def get_re_sting(string):
     if len(string) < 1:
         return string
     return get_re_sting(string[1:]) + string[0]
print(get_re_sting("dgx2541104422"))

