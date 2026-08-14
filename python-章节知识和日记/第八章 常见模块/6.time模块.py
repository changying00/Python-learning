"""
time 是一个专门用来表示 时间的模块 

- time.sleep(second) :  将程序进行睡眠、单位 秒   1s = 1000ms 

- time.time() : 时间戳 、 获取 距离 1970-01-01 0:0:0 经过了 多少 秒 

- time.localtime() : 获取当前 时间元组 对象 、时间元组 由 9个值组成 

     9个值分别代表  年、月、日、时、 分、秒、 星期、一年中的第几天 、 是否启用夏令时

     星期 :  0 代表 周一、 1 代表周二、 ... 6 代表周日 

     时间元组 对应值的 获取方式 
        a) 使用 索引 获取 

        b) 使用 属性名 获取
            tm_year : 年 
            tm_mon : 月
            tm_mday : 日 
            tm_hour : 时
            tm_min : 分
            tm_sec : 秒 
            tm_wday : 星期
            tm_yday : 一年中第几天

-  time.mktime(timetuple) : 获取 一个时间元组 对应的 时间戳

-  time.strftime(format, timetuple) :  将一个时间元组 对象 按照指定的 模式 转成 字符串 (日期的格式化)

        format : 是一个 模式匹配串 、支持的符号 

            %Y : 年份 
            %m : 月份
            %d : 日
            %H : 时   24进制、  %I  12进制 
            %M : 分
            %S : 秒

-  time.strptime(string, format) :  将一个表示 时间的指定格式的 字符串 转成 时间元组 对象 

"""

import random 
import time 

# 随机睡眠 0.1 ~ 0.3 秒
# time.sleep(random.uniform(0.1, 0.3))

# print(time.time())  # 1786607589.1192408

tp = time.localtime()
print(tp)

print(time.strftime("%Y-%m-%d %H:%M:%S", tp))

# 获取 距离 1970年 3000秒 后的 时间元组对象 
# tp2 = time.localtime(3000)
# print(tp2)

string = "2000年10月20日13点22分15秒"

print(time.strptime(string, "%Y年%m月%d日%H点%M分%S秒"))