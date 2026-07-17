#【循环题】 编写一段程序 使用 for 循环 计算(1/1 - 1/3 + 1/5 - 1/7 + 1/9 - .... ) * 4 的
# 前 1000000项的结果
# num = 0
# x = 0
# while x < 1000000:
#     for i in range(1,1000000,2):
#         if x & 1 :
#             num += 1 / i
#         else:
#             num -= 1 / i
#     x += 1
# print(num)
num = 0
#循环控制1000000次
for i in range(1000000):
#计算分母
    x = 2 * i + 1
    # 如果结果为0，为False说明i是偶数，前面为正号
    # 如果结果为1，为True说明i是奇数，前面为减号
    if 1 & i:
        num -= 1 / x
    else:
        num += 1 / x
#打印结果
print(num * 4)