"""
【函数】编写一个函数 count_vowels(string)，接受一个字符串string，并返回其中元音字母的数量。 元音字母有 A、E、I、O、U (不区分大小写)
"""
# def count_vowels(string):
#     #定义一个空列表ls1
#     ls1 = []
#     #for 遍历这个字符串
#     for i in  string:
#         #判断是否为元音字符
#         if i in ["A","E","I","O","U","a","e","i","o","u"]:
#             #符合的增加进去
#             ls1.append(i)
#     #返回列表的长度即数量
#     return len(ls1)
# #测试
# if __name__ == "__main__":
#     result = count_vowels("abcddgx52111231zhendexihuanni")
#     print(result)
"""
【函数】编写一个函数 count_vowels，用于统计字符串中元音字母的个数。
"""

# 定义一个函数
def count_vowels(string):
    # 定义一个变量，用于记录元音字母的数量
    count = 0

    # 遍历字符串中的每一个字符
    for i in string:

        # 判断当前字符是否为元音字母
        if i in "AEIOUaeiou":

            # 如果是元音字母，数量加 1
            count += 1

    # 返回元音字母的总数量
    return count


# 测试代码
if __name__ == "__main__":

    # 调用函数
    result = count_vowels("abcddgx52111231zhendexihuanni")

    # 输出结果
    print(result)