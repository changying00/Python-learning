"""
获取 日期在一年内的天数 
"""
year = int(input("请输入一个年份，例如 2026\n"))

month = int(input("请输入一个月份, 范围 1 ~ 12\n"))

day = int(input("请输入一个天数, 范围 1 ~ 31\n"))

# 计算 从 1月 ~ (month - 1) 月 的所有天数
# 定义一个变量、用来存储最终的结果 
s = day 

# 定义一个变量、用来控制循环的次数 
m = 1 

while m < month:
    # 获取 m 月对应的 最大天数 
    if m in [1, 3, 5, 7, 8, 10, 12]:
        s += 31
    elif m in [4, 6, 9, 11]:
        s += 30
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        s += 29
    else:
        s += 28

    # m 增加 1
    m += 1

# 输出 最终的结果 
print(s)
