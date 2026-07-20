"""

【函数】编写一个函数 has_letter 、获取指定的字符串中是否包含字母
"""
#定义一个函数
def has_letter(str_num):
    """
    :param str_num:参数用于接收用户输入的字符串
    :return: 返回一个值如果 为False则不包含字母
    如果True 则包含字母
    """
    #遍历str_num 的每个字符
    for i in str_num:
        if not("a" <= i <="z") and not ("A" <= i <="Z"):
            return False
    return True
print(has_letter("1112")) #False
print(has_letter("aab")) #True