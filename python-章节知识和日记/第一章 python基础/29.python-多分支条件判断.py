"""
多分支条件判断 语法

if condition:
    pass
elif condition:
    pass 
...

else:
    pass

输入一个成绩、请输出对应的等级、  

练习题： 从键盘 输入一个月份 、请输出该月份所对应的季节 


多分支条件 在编写代码的时候，一定要注意逻辑是否正确 

"""

# 获取从键盘输入的成绩 
# score = float(input("请输入某学生的成绩"))

# if score >= 90:
#     print("优秀") 
# elif score >= 70:
#     print("中等")  
# elif score >= 80:
#     print("良好")
# elif score >= 60:
#     print("及格")
# else:
#    print("不及格")

# 从键盘输入一个月份
month = int(input("请输入一个月份"))

if month in [3, 4, 5]:
    print("春天")
elif month in [6, 7, 8]:
    print("夏天")
elif month in [9, 10, 11]:
    print("秋天")
elif month in [12, 1, 2]:
    print("冬天")
else:
    print("未知")





