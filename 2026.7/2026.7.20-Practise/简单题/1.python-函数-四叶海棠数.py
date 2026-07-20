""""

【函数】编写一个函数、获取 1000 ~ 9999 以内的 所有 四叶海棠数。
四叶海棠数: 一个数字 它的 每一位数字 四次方 和 仍旧等于 这个数
7710
"""
# #定义一个函数名为hai_num的函数
# def hai_num ():
#     for i in range(1000,10000):
#         #因为是1000~9999 有四位数把对应的四位数求出来
#         #个位数
#         num_first = i % 10
#         #十位数
#         num_second = (i //10) % 10
#         #百位数
#         num_third = (i // 100)  % 10
#         #千位数
#         num_fourth = i // 1000
#         # 判断四位数字的四次方之和是否等于原数字
#         if (num_first ** 4
#                 + num_second ** 4
#                 + num_third ** 4
#                 + num_fourth ** 4 == i):
#             print (i)
#
# # 调用函数
# hai_num()



def hai_num():
    result = []   # 创建一个空列表保存结果

    for i in range(1000, 10000):

        num_first = i % 10
        num_second = (i // 10) % 10
        num_third = (i // 100) % 10
        num_fourth = i // 1000

        if (num_first ** 4
            + num_second ** 4
            + num_third ** 4
            + num_fourth ** 4 == i):

            result.append(i)

    return result


# 接收函数返回值
nums = hai_num()

print(nums)