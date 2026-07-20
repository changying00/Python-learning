"""
【函数】编写一个函数 has_number 、判断指定的字符串中是否包含数字
"""
#定义一个函数has_number
def is_lower_letter(str_count):
    """
    :param str_count: 参数用于接收传入的字符串
    :return: 返回一个字符串是否包含数字
    return 返回False 说明含有数字
    返回 True 说明不含数字
    """
    #遍历传入的字符串
    for i in str_count:
        if  not("a" <= i <="z") and not ("A" <= i <="Z"):
               return False
    return True
print(is_lower_letter("aAADDc"))