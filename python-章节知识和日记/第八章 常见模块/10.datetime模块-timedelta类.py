"""
时间间隔 timedelta : 

 timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

 weeks : 周
 days : 天
 hours : 小时
 minutes : 分钟
 seconds : 秒
 milliseconds : 毫秒
 microseconds : 微秒


 两个 日期 做 减法 返回一个 时间间隔对象 
 两个 日期和时间对象 做减法 返回一个 时间间隔对象

 日期 支持 和 时间间隔间隔 做 加法/减法运算 、返回 一个 新的 日期  

"""
from datetime import timedelta, date, datetime 

# 创建 一个 三天 多 2小时的 时间间隔 
duration = timedelta(days=3, hours=2)

# print(duration)
# 获取 间隔的天数 
print(duration.days)

# 获取 间隔的秒数 (不满足 1天的秒数)
print(duration.seconds)

# 获取 整个时间间隔 对应的秒数 
print(duration.total_seconds())

# 两个 日期 支持 做 减法运算 、返回 一个时间间隔对象 

d1 = date(2000, 10, 10)
d2 = date(2026, 8, 14)

# 获取 d1 和 d2 间隔的时长 、返回 一个时间间隔对象  
print(d2 - d1)

d3 = datetime(2000, 10, 10, 20, 10, 10)
d4 = datetime.now()

print(d4 - d3)


d5 = date.today()
# 求 5天后的日期 
print(d5 + timedelta(days=5))

# 获取 昨天的日期 
print(d5 - timedelta(days=1))


d6 = datetime.now()

# 获取 一小时后的时间 
print(d6 + timedelta(hours=1))

# 获取 2周前的时间 
print(d6 - timedelta(weeks=2))