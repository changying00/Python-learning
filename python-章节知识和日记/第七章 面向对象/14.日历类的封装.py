from typing import Tuple


class Calendar:
    """
    日历类
    """

    def __init__(self, year, month, day=1):
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    def is_leap(self) -> bool:
        """是否是闰年"""
        return self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0

    def __get_month_max_day(self, month):
        """获取 指定月份它的最大天数"""
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if month in [4, 6, 9, 11]:
            return 30
        if self.is_leap():
            return 29
        return 28

    def get_month_max_day(self) -> int:
        """
        获取 当前月的最大天数
        """
        return self.__get_month_max_day(self.month)

    def get_day_in_year(self) -> int:
        """获取当前日历是一年中的第一天"""
        total = self.day
        for m in range(1, self.month):
            # 获取 m 月的最大天数
            total += self.__get_month_max_day(m)
        return total

    def __get_week(self, day=1) -> Tuple[int, str]:
        """获取当前月 某一天是星期几"""
        # 定义一个变量、存储年份
        year = self.year
        # 获取公式中的 M
        M = self.month - 2
        # 如果 月份是 1 或者 2 月
        if self.month <= 2:
            M = self.month + 10
            # 年份要减少 1 年
            year -= 1

        # 计算 公式中的 C 和 Y
        C, Y = divmod(year, 100)
        # 套用 蔡乐公式 计算 W
        W = ((26 * M - 2) // 10 + day + Y + Y // 4 + C // 4 - 2 * C) % 7
        # 定义一个列表 、用来表示 周日 、周一 ...
        weeeks = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]

        return W, weeeks[W]

    def get_week(self) -> Tuple[int, str]:
        """获取当前日历是星期几"""
        return self.__get_week(self.day)

    def get_week_num(self) -> int:
        """获取 星期的 数字表示形式"""
        return self.get_week()[0]

    def get_week_str(self) -> str:
        """获取 星期的 数字表示形式"""
        return self.get_week()[1]

    def show_calendar(self):
        """输出当月日历"""
        # 输出 日历的标题
        print("一\t二\t三\t四\t五\t六\t日")

        # 空格数 = 星期 - 1  (周日 空格数为 6)
        # 获取 1 号 是星期几
        week, _ = self.__get_week()
        space_num = 6 if week == 0 else week - 1
        # 输出 空格数
        print("\t" * space_num, end="")
        # 获取 当前月的最大天数
        max_day = self.get_month_max_day()

        for d in range(1, max_day + 1):
            print(d, end="\t")
            if (space_num + d) % 7 == 0:
                print("\n")


if __name__ == "__main__":
    # 创建一个 日历
    calendar = Calendar(2026, 8, 7)

    # 获取 本月日期
    # calendar.show_calendar()
    print(calendar.is_leap())
    print(calendar.get_day_in_year())


