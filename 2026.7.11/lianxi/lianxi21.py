"""
【循环结构】输入某年某月某日，判断这一天是这一年的第几天？

"""

#定义一个变量year,接收用户输入的年份

year = int(input("请你输入年份:"))

#定义一个变量 month,接收用户输入的月份

month = int(input("请你输入月份:"))

#定义一个变量 day ,接收用户输入的日

day = int(input("请你输入日:"))

#先把日子加进去

count = day
#定义一个变量x,控制循环
x =  1

while x < month :
# 1、3、5、7、8、10、12月 一个月为31天
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        count +=   31
# 4 、6、9、11 为30一天
    elif x == 4 or x == 6 or x == 9 or x ==11:
        count +=  30
# 判断二月,闰年29天，平年28天
    else:
        if (year % 4 == 0 and year % 100 != 0  )  or  year % 400 == 0:
            count += 29
        else:
            count += 28
    x += 1
print("这一天是这一年的第", count, "天")