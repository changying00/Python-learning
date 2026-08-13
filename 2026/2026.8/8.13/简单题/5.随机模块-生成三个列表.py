"""
【随机模块】生成 三个列表、分别代表 1900 ~ 2100 之间的所有年份、 1 ~ 12 之间所有的月份、 1 ~ 31 之间所有的 天数 。 使用 随机模块 快速 获取一个 年、月、日数据 、并验证该数据 是否合法， 例如 小月 天数不能超过 30，
2月闰年不能超过29，平年不能超过28 获取该 年、月、日 对应的 星期 和 这个日期是 一年中的第几天
"""
"""
【随机模块】

生成三个列表：
1900 ~ 2100 年
1 ~ 12 月
1 ~ 31 日

随机获取一个年月日，
判断日期是否合法，
并获取星期和一年中的第几天。
"""

import random
from datetime import datetime
def random_date():
    # 生成年份列表
    years = list(range(1900, 2101))
    # 生成月份列表
    months = list(range(1, 13))
    # 生成日期列表
    days = list(range(1, 32))
    # 随机获取年月日
    year = random.choice(years)
    month = random.choice(months)
    day = random.choice(days)
    print(f"随机日期：{year}-{month}-{day}")
    # 判断是否为闰年
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap_year = True
    else:
        leap_year = False
    # 判断当前月份最多有多少天
    if month == 2:
        if leap_year:
            max_day = 29
        else:
            max_day = 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31
    # 判断日期是否合法
    if day > max_day:
        print("日期不合法！")
        return
    print("日期合法！")
    # 创建日期对象
    date = datetime(year, month, day)
    # 获取星期
    weeks = [
        "星期一",
        "星期二",
        "星期三",
        "星期四",
        "星期五",
        "星期六",
        "星期日"
    ]
    print("星期：", weeks[date.weekday()])
    # 获取一年中的第几天
    print("一年中的第", date.timetuple().tm_yday, "天")
if __name__ == '__main__':
    random_date()