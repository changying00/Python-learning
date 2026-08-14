"""
【随机模块】编写一个函数 generator_ordernum(num=5) 生成一个随机的唯一的不重复订单编号 。
 订单编号格式为  yyyyMMddHHmmss + 长度为 num 的随机数字组成， 例如 2024080911223356789
yyyyMMddHHmmss 代表年月日时分秒组成的字符串
"""
import random
from datetime import datetime
#定义一个函数
def generator_ordernum(num=5) :
    str_num = ''
    #循环num次
    for _ in range(num) :
        #将随机生成的数字加起来
        str_num += str(random.randint(0,9))
        #由模块datetime.now()生成当前时间，然后格式化一下
    prefix = datetime.now().strftime('%Y%m%d%H%M%S')
    #把当前时间 + 随机生成长度为num的数相加
    result = prefix + str_num
    #返回结果
    return result

if __name__ == '__main__':
    print(generator_ordernum())


