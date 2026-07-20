"""
【函数】编写一个函数 get_week(year , month, day) 获取指定时间对应的星期， day 如果不传入，默认为 1 。 星期计算公式(蔡乐公式)：


W =((26M−2)/10+D+Y+Y/4+C/4−2C)%7
为了确定某一天是星期几、可以用下面的算法
M 表示月。 M 为 1 表示 3月， 2表示4月，以此类推。M为11表示1月、12表示2月，但是针对这两个月，在进行递推计算的时候要将年减1
D 表示日 （1 ~ 31）
C 表示年的头两位数（在 对 1、2月做了调整之后的年）
Y 表示年的后两位数 （在 对 1、2月做了调整之后的年）

W 表示星期、0代表周日，1代表周一、依次类推
如果 W 是负数、则需要加 7
"""
#定义一个函数
def get_week(year, month, day=1):
    """
    :param year:用户输入的年份
    :param month: 用户输入的月份
    :param day: 用户输入的日
    :return: 返回指定时间对应的星期，
    2008 2012
    """
    # 计算公式中的 M
    M = month - 2 if month > 2 else month + 10

    # 判断月份是否是 1, 2 月，如果是年份减去 1
    adjusted_year = year if month > 2 else year - 1

    # 获取公式中的 C 和 Y
    C, Y = adjusted_year // 100, adjusted_year % 100
    # 使用蔡乐公式计算 W
    W = ((26 * M - 2) // 10 + day + Y + Y // 4 + C // 4 - 2 * C) % 7
    if W < 0:
        W += 7
    # 输出星期
    weekdays = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]
    return weekdays[W]
print(get_week(2026, 7, 20))#周一