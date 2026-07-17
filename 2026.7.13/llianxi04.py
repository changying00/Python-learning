"""
【循环】统计 1~1000 中，数字之和等于 10 的所有数 。
例：28 = 2 + 8 = 10，55 = 5 + 5 = 10
"""
# for i in range(1,1001):
#     a = i % 10
#     b = i // 10
#     c = i // 100
#     if i < 10:
#         continue
#     if 10 <= i <= 100 and a + b == 10:
#         print(i)
#     if 100 <= i <= 1000 and a + b + c == 10:
#         print(i)
#

for i in range(1,1001):
    a = i % 10  # 个位
    b = i // 10 % 10  # 十位
    c = i // 100  # 百位

    if a + b + c == 10:
        print(i)

"""
for number in range(10,1000):
   # 定义一个变量、用于存储当前数字number 它的每一位数字之和
   s = 0
   #定义一个变量、存储number 的初始值
   _number = number
   #使用while循环 、获取数字上的每一位数字
   while _number > 0:
       x = _number %10:
       #将每一个数字 累加求和
       s += x
       _number //= 10
   #循环结束，判断s 的和是否等于10
    if s ==10:
        print(number)
"""