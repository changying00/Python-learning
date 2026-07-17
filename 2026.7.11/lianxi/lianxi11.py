"""
从键盘输入一个数字例如2 则计算 2 + 22 +222 +2222+ 22222 前五项的和
当前项的数字 永远等于 前一项的数字 * 10 + n

"""
n = int(input("请输入一个数字:"))
sum  = temp  =  0
for _ in range(5):
    temp  =  temp * 10 + n
    sum  += temp
print(sum)