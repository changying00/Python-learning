"""
num = int(input())

if num & 1:
    print("奇数")
if ont(num & 1):
    print("偶数")
  """
#优化前自己写
""" 
month = int(input("请输入一个月份:"))
if  5 >= month >= 3:
  print("该月份是春季")
elif 8 >= month > 5:
  print("该月份是夏季")
elif 11 >= month > 8:
  print("该月份是秋季")
else:
  print("该月份是冬季")
"""
#优化后

month = int(input("请输入一个月份:"))
if 3 <= month <= 5:
    print("该月份是春季")

elif 6 <= month <= 8:
    print("该月份是夏季")

elif 9 <= month <= 11:
    print("该月份是秋季")

elif 1 <= month <= 2 or month == 12:
    print("该月份是冬季")

else:
    print("输入月份错误")