"""
【函数】编写一个函数 get_number_count 、获取字符串中 数字得个数
"""
#定义一个函数get_number_count

def get_number_count(str_num):
    """
    :param str_num:  传入一个字符串
    :return: 返回字符串中的数字个数
    """
    #定义一个变量存储字符串中的数字个数
    count = 0
    #遍历传入的字符串
    for i in str_num:
        #判断字符串是否有大小写字母
        if not("a" <= i <="z") and not ("A" <= i <="Z"):
            count += 1
    return count
print(get_number_count("a15454A"))
