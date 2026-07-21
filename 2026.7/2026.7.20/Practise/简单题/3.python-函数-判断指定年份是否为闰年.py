"""
【函数】编写一个函数 is_leap_year(year) 获取指定的年份是否是闰年
"""
#定义一个函数判断是否为闰年
def is_leap_year(year):
    #根据闰年的规则判断
    """
    下面写的有问题，最后一行可以
    """
    # if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    #     #如果是闰年返回，闰年
    #     return  "是闰年"
    # #如果不是返回不是
    # return "不是闰年"
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
input_year = is_leap_year(2009)
print (input_year)