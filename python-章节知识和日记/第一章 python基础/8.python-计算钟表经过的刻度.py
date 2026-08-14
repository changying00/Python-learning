"""
计算钟表 针经过的度数
"""

# 定义三个变量、分别代表 小时、分钟和秒 
hour, minute, second = 19, 20, 21

# 计算 记录 0:0:0 经过的总秒数
total_seconds = hour * 3600 + minute * 60 + second 

# 每秒钟 秒针 走 6 度
# sec_deg = second * 6
sec_deg = total_seconds * 6 % 360

# 分针 1 分钟 走 6 度 、 1秒钟 分针走 0.1度
# min_deg = minute * 6 + second * 0.1
min_deg = total_seconds / 10 % 360

# 时针 1小时走 30度、 1分钟 时针走 0.5度   1秒钟 时针走 1/120 度
# hour_deg = (hour * 30 + minute * 0.5 + second / 120) % 360
hour_deg = total_seconds / 120 % 360

# 输出时间
print(hour, minute, second, sep=":", end="")
# 输出结果
print("时针走了", hour_deg, "°", sep="", end=",")
print("分针走了", min_deg, "°", sep="", end=",")
print("秒针走了", sec_deg, "°", sep="")


