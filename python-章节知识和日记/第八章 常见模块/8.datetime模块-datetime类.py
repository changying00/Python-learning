from datetime import datetime 

"""
datetime : 表示 日期 和 时间 

"""

# 创建 日期和时间对象 
# 1. 使用 构造方法创建 、时分秒 可传 可不传
d = datetime(2026, 8, 13, 10, 10, 10)

# 2. 使用 静态方法 获取 当前系统时间 
d = datetime.now()
# 3. 使用 ISO8601 
d = datetime.fromisoformat("2000-10-10T12:22:33")
# 4. 使用 时间戳构建 
d = datetime.fromtimestamp(2 * 24 * 60 * 60)

# 获取 对应的 年月日 
print(d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond)

print(d.weekday())

print(d)

print(d.timetuple())

print(d.strftime("%Y-%m-%d %H:%M"))

string = "2000/10/10 12点22分"

print(datetime.strptime(string, "%Y/%m/%d %H点%M分"))


