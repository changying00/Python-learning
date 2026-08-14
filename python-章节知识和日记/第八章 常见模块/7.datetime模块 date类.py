"""

ISO 8601 日期规范 : 

    表示日期和时间的字符串格式 必须为  2000-10-10T11:22:33 


datetime 模块 :  用来表示 日期和时间的类 、是 编程中 非常重要的数据类型 。

    date : 日期类 、表示 年、月、日

    datetime : 日期和时间类  表示 年、月、日、 时、分、秒 

    time : 时间类 、表示 时、分、秒 

    timedelta : 时间间隔类 、表示 一段时间 。

"""
from datetime import date, datetime 


# 日期类 对象的创建方式 
# 1. 使用 构造方法 创建一个 指定日期的 日期对象 
d = date(2000, 2, 1)
# 2. 使用 静态方法 、获取 当前日期对象 
d = date.today()
# 3. 使用 静态方法、通过 时间戳 构建当前日期对象 
d = date.fromtimestamp(2 * 24 * 60 * 60)
# 4. 使用 静态方法， 通过 ISO-8601 规范 构建日期对象 
d = date.fromisoformat("2000-10-20")

print(d)

# 获取 日期对象中的 年、月 、 日 
print(d.year, d.month, d.day)

# 获取 星期 、 0 代表 周一 、 1 代表周二 ...
print(d.weekday())

# 将 日期 对象转成 时间元组 
print(d.timetuple())

# 将 日期 对象 转成 指定格式的 字符串 (日期的格式化)
print(d.strftime("%Y年%m月%d日"))

# 定义一个 表示 日期的 字符串 
string = "2000/10/30"

# 将上述 字符串 转成 日期对象 (日期的反格式化)
print(datetime.strptime(string, "%Y/%m/%d").date())



