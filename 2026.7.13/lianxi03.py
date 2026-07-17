"""
【循环】编写一段程序、计算 5! 提示: 5! = 5 * 4 * 3 * 2 * 1
"""
count = 1
for i in range(5,1,-1):
    count *= i
print(count)

#
# text = "5! = "
#
# for i in range(5, 0, -1):
#     text += str(i)
#
#     if i != 1:
#         text += " * "
#
# print(text)