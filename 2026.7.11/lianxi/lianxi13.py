"""

分支】根据指定月份，打印该月份所属的季节。3,4,5 春季 6,7,8 夏季 9,10,11 秋季 12, 1, 2 冬季

"""
# 定义一个变量，用于接收用户输入的月份

month = int(input('请你输入一个月份:'))
#3,4,5 春季
if 5 >= month >= 3:
    print(month,"春季")

#6,7,8 夏季
elif 8 >= month >= 6:
    print(month,"夏季")
#9,10,11 秋季
elif 11 >= month >= 9:
    print(month,"秋季")
#除此之外
else:
    print(month,"冬季")