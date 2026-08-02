"""
【正则表达式】将一个字符串中包含多个手机号的数据、手机号中间四位隐藏，
例如 Hello, My Telphone is 13384011981 。your phone is 13434672457
经过处理后为 Hello, My Telphone is 133****1981 。your phone is 134****2457
"""
import re
#定义函数
def phone_number_secure(strings):
    #编写正则表达匹配式
    regex = r"(1[3-9]\d)\d{4}(\d{4})"
    result = re.sub(regex, r"\1****\2", strings)
    #返回结果
    return result

if __name__ == '__main__':
    print(phone_number_secure("例如 Hello, My Telphone is 13384011981 。your phone is 13434672457,13303701853,my pthone is 17589737503"))

