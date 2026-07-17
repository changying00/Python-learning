"""

【循环】要求用户输入一个正整数，如果用户输入的数字小于等于0，则继续要求用户重新输入，直到输入一个正整数。满足条件后计算给定正整数的阶乘

"""

# 定一个变量num接收用户输入一个正整数：
num = int(input("请你输入一个正整数:"))
# 定义一个变量count、用于接收正整数的阶乘
count =  num
if num <= 0:
    print("请你重新输入一个正整数")
else:
    while  True :
        num = num -1
        count = count *  num
        if num == 1:
            break
    print(count)
    
 """   
num = int(input("请你输入一个正整数："))

while num <= 0:
    num = int(input("请重新输入一个正整数："))

count = 1

while num > 0:
    count *= num
    num -= 1

print(count)
"""