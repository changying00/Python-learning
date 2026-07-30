"""
【字符串】编写一个函数 first_unique_char(string)
查找字符串中第一个不重复的字符的索引位置，如果找不到返回 -1
 "aabbccdgxdd" "aabbccdd"
"""
#定义一个函数first_unique_char
def first_unique_char(string):
    for i in range(len(string)):
        # 如果该字符在整个字符串中只出现1次
        if string.count(string[i]) == 1:
            return i
    # 如果整个循环结束都没找到，才返回 -1
    return -1
print(first_unique_char("aabbccdnd"))