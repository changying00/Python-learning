"""
【静态方法】编写一个模块 qikux, 定义一个工具类 QikuxUtils、并提供如下静态方法
a)  sum(a, *args) :  计算多个数字的 和 (至少传入一个数字)
b)  max(a, *args) :  计算多个数字的最大值 (至少传入一个数字)
c)  min(a, *args) : 计算多个数字的最小值 (至少传入一个数字)
d)  is_leap_year(year) :  获取年份是否是闰年
e)  is_tel(string) :  验证传入的字符串是否是 手机号
f)  is_email(string) : 验证传入的字符串是否是邮箱
g)  tel_secure(string) :  如果是手机号进行脱敏(中间4位使用 ****)操作、否则直接返回原字符串
h)  email_secure(string) : 如果是邮箱进行脱敏（账号保留第一个字符、账号其他字符串使用 6个 * 代替）
					操作、否则直接返回原字符串
i)  is_even(num) :  判断是否是偶数
j)  is_odd(num) :  判断是否是 奇数 
"""
import re


class QikuxUtils:
    """工具类：全部使用静态方法"""

    @staticmethod
    def sum(a, *args):
        """计算多个数字的和（至少传入一个数字）"""
        total = a
        for num in args:
            total += num
        return total

    @staticmethod
    def max(a, *args):
        """计算多个数字的最大值（至少传入一个数字）"""
        result = a
        for num in args:
            if num > result:
                result = num
        return result

    @staticmethod
    def min(a, *args):
        """计算多个数字的最小值（至少传入一个数字）"""
        result = a
        for num in args:
            if num < result:
                result = num
        return result

    @staticmethod
    def is_leap_year(year):
        """判断是否为闰年"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def is_tel(string):
        """验证是否为手机号：1开头，第二位3-9，共11位数字"""
        pattern = r"^1[3-9]\d{9}$"
        return bool(re.match(pattern, str(string)))

    @staticmethod
    def is_email(string):
        """验证是否为邮箱"""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, str(string)))

    @staticmethod
    def tel_secure(string):
        """手机号脱敏：中间4位用 **** 代替；非手机号原样返回"""
        string = str(string)
        if QikuxUtils.is_tel(string):
            # 前3位 + **** + 后4位
            return string[:3] + "****" + string[7:]
        return string

    @staticmethod
    def email_secure(string):
        """
        邮箱脱敏：账号保留第一个字符，其余用 6 个 * 代替
        例如 abc@qq.com -> a******@qq.com
        非邮箱原样返回
        """
        string = str(string)
        if QikuxUtils.is_email(string):
            local, domain = string.split("@", 1)
            return local[0] + "******@" + domain
        return string

    @staticmethod
    def is_even(num):
        """判断是否为偶数"""
        return num % 2 == 0

    @staticmethod
    def is_odd(num):
        """判断是否为奇数"""
        return num % 2 != 0


# ========== 测试代码 ==========
if __name__ == "__main__":
    u = QikuxUtils  # 通过类名直接调用静态方法

    print("sum:", u.sum(1, 2, 3, 4, 5))
    print("max:", u.max(1, 9, 3, 7))
    print("min:", u.min(1, 9, 3, 7))
    print("is_leap_year(2024):", u.is_leap_year(2024))
    print("is_leap_year(2026):", u.is_leap_year(2026))
    print("is_tel('13812345678'):", u.is_tel("13812345678"))
    print("is_tel('12345'):", u.is_tel("12345"))
    print("is_email('abc@qq.com'):", u.is_email("abc@qq.com"))
    print("is_email('not-email'):", u.is_email("not-email"))
    print("tel_secure:", u.tel_secure("13812345678"))
    print("tel_secure(非手机):", u.tel_secure("hello"))
    print("email_secure:", u.email_secure("abc@qq.com"))
    print("email_secure(非邮箱):", u.email_secure("hello"))
    print("is_even(4):", u.is_even(4))
    print("is_odd(4):", u.is_odd(4))
