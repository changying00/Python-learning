"""
【time模块】编写一个函数 show_calendar(year, month) 显示指定时间对应的日历信息
日   一   二   三   四   五   六
      1    2    3   4    5    6
 7    8    9   10   11   12   13
 14   15   16  17   18   19   20
 21   22   23  24   25   26   27
 28   29   30
"""
import time
def show_calendar(year, month):
    # 获取指定月份的第1天是星期几
    # %w：星期日=0，星期一=1，...，星期六=6
    first_day = time.strptime(f"{year}-{month}-01", "%Y-%m-%d")
    # 获取第1天对应的星期
    week = int(time.strftime("%w", first_day))
    # 获取这个月一共有多少天
    # 方法：找到下个月的第1天，然后减去1天
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    next_month_first = time.strptime(
        f"{next_year}-{next_month}-01",
        "%Y-%m-%d"
    )
    # 将下个月第1天转换成时间戳
    next_timestamp = time.mktime(next_month_first)
    # 减去一天，得到当前月份最后一天
    last_day = time.localtime(next_timestamp - 24 * 60 * 60)
    # 获取当前月份最后一天是几号
    days = int(time.strftime("%d", last_day))
    # 打印星期标题
    print("日  一  二  三  四  五  六")
    # 第1天之前空出来的位置
    print("    " * week, end="")
    # 依次打印1号到最后一天
    for day in range(1, days + 1):
        # 每个日期占4个字符
        print(f"{day:>3}", end=" ")
        # 星期六之后换行
        if (week + day) % 7 == 0:
            print()
if __name__ == '__main__':

    show_calendar(2026, 8)