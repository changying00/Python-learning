"""

函数】编写一个函数 is_upper_letter : 获取一个字符串是否是纯大写字母
"""
#定义一个函数
def is_upper_letter(str_count):
    """
    :param str_count:参数用于接收用户输入的字符串
    :return: 返回是否为纯大写字母
    如果为False 则不是纯大写字母
    如果为True 则是纯大写字母
    """
    for i in  str_count:
        if  not ("A" <= i <="Z"):
            return False
    return True
print(is_upper_letter("ADAF1")) # False