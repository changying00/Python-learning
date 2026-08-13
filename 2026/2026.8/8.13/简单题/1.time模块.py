"""【time模块】编写一个函数 get_last_week() 、获取最近7天的所有日期, 返回的格式为 %Y-%m-%d 组成的列表

"""
import time
def get_last_week():
    # 创建一个空列表，用来保存最近7天的日期
    result = []
    # time.time() 获取当前时间的时间戳
    now = time.time()
    # 循环7次，分别获取今天、昨天、前天……前6天
    for i in range(7):
        # 一天 = 24 * 60 * 60 = 86400秒
        # 每循环一次，就从当前时间戳中减去一天
        timestamp = now - i * 24 * 60 * 60
        # time.localtime() 将时间戳转换成本地时间的结构化时间
        local_time = time.localtime(timestamp)
        # time.strftime() 按照指定格式将时间转换成字符串
        date = time.strftime("%Y-%m-%d", local_time)
        # 将日期添加到列表中
        result.append(date)
    # 返回最近7天的日期列表
    return result
print(get_last_week())