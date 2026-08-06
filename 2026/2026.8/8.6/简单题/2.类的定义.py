"""
【类的定义】编写一个 日历类Calendar 、提供 年 、月、日 三个私有属性、 并提供 如下行为
要求 创建日历类的时候，必须提供 年月日三个属性
a) show_calendar(self)  :  显示 当月 日历
b) get_week(self) :  蔡乐公式获取星期、返回 (0,  “周日”)  这种格式
c) is_leap(self)  :  是否是闰年
d) get_month_max_day(self)  获取当月最大的天数
e) get_day_in_year(self)  获取当前日期是 年中的 第几天
f) get_week_num(self) : 获取星期、返回 0 这种格式
g) get_week_str(self) : 获取星期、返回 周日 这种格式
"""


class Calendar:
    """日历类：提供年月日私有属性及相关日历操作"""

    # 星期映射表：蔡勒公式结果 0=周六 ... 需要转换为 0=周日 的展示
    # 蔡勒公式：w=0 周六, 1 周日, 2 周一, 3 周二, 4 周三, 5 周四, 6 周五
    # 题目要求：0 对应周日，所以做一次转换
    _WEEK_STRS = ("周日", "周一", "周二", "周三", "周四", "周五", "周六")

    def __init__(self, year, month, day):
        """构造方法：必须提供年、月、日"""
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

    def is_leap(self):
        """判断是否为闰年：能被4整除但不能被100整除，或能被400整除"""
        y = self.__year
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def get_month_max_day(self):
        """获取当月最大天数"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.__month == 2 and self.is_leap():
            return 29
        return days_in_month[self.__month]

    def get_day_in_year(self):
        """获取当前日期是一年中的第几天"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total = 0
        for m in range(1, self.__month):
            if m == 2 and self.is_leap():
                total += 29
            else:
                total += days_in_month[m]
        total += self.__day
        return total

    def _zelor_week(self):
        """
        蔡勒公式计算星期
        返回：0=周六, 1=周日, 2=周一, 3=周二, 4=周三, 5=周四, 6=周五
        """
        y = self.__year
        m = self.__month
        d = self.__day
        # 1月、2月看作上一年的13、14月
        if m == 1 or m == 2:
            m += 12
            y -= 1
        c = y // 100       # 世纪数
        y = y % 100        # 年份后两位
        w = (y + y // 4 + c // 4 - 2 * c + (13 * (m + 1)) // 5 + d) % 7
        # Python 中 % 对负数会得到非负结果，但为保险再处理一次
        w = (w + 7) % 7
        return w

    def get_week_num(self):
        """获取星期数字：0=周日, 1=周一, ..., 6=周六"""
        z = self._zelor_week()
        # 蔡勒：0周六1周日2周一3周二4周三5周四6周五
        # 转换：周日=0, 周一=1, ..., 周六=6
        mapping = {0: 6, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
        return mapping[z]

    def get_week_str(self):
        """获取星期字符串，如 '周日'"""
        return self._WEEK_STRS[self.get_week_num()]

    def get_week(self):
        """蔡勒公式获取星期，返回 (0, '周日') 这种格式"""
        num = self.get_week_num()
        return (num, self.get_week_str())

    def show_calendar(self):
        """显示当月日历"""
        # 计算当月1号是星期几
        first = Calendar(self.__year, self.__month, 1)
        first_week = first.get_week_num()  # 0=周日
        max_day = self.get_month_max_day()

        print(f"\n{'=' * 28}")
        print(f"      {self.__year} 年 {self.__month} 月")
        print(f"{'=' * 28}")
        print("日  一  二  三  四  五  六")

        # 打印1号之前的空白
        line = "    " * first_week
        for day in range(1, max_day + 1):
            # 高亮当天
            if day == self.__day:
                line += f"[{day:2d}]"
            else:
                line += f"{day:2d}  "
            # 每到周六换行（week_num=6）
            if (first_week + day) % 7 == 0:
                print(line.rstrip())
                line = ""
        if line:
            print(line.rstrip())
        print(f"{'=' * 28}")


# ========== 测试代码 ==========
if __name__ == "__main__":
    cal = Calendar(2026, 8, 6)
    print(f"日期: {cal.year}-{cal.month}-{cal.day}")
    print(f"是否闰年: {cal.is_leap()}")
    print(f"当月最大天数: {cal.get_month_max_day()}")
    print(f"年中第几天: {cal.get_day_in_year()}")
    print(f"星期数字: {cal.get_week_num()}")
    print(f"星期字符串: {cal.get_week_str()}")
    print(f"get_week: {cal.get_week()}")
    cal.show_calendar()
