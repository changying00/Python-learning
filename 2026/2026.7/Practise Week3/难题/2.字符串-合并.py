#【字符串】编写一个函数，对给定的字符串进行压缩，例如将 "aabcccccaaa" 转换为 "a(2)b(1)c(5)a(3)"
"""刚开始思路：思路是创建一个空字典，遍历字符串如果这个字符串的值不在字典中，我把这个值当字典的键，然后count统计这个值一共多少，为字典的值，但是不好处理aa 后面的aaa，
问题:题目不是统计每个字符出现的总次数，而是统计连续出现的次数。而且用字典的话，它的键还不能重复。

"""
#定义一个函数string_zip对字符串进行压缩
def string_zip(string ="aabcccccaaa"):#设置参数的默认值为"aabcccccaaa"
    #定义一个空列表
    result = []
    current = string[0]  # 当前连续字符
    count = 1  # 当前连续次数
    #从第二个字符开始遍历
    for i in range(1,len(string)):
        #如果当前字符和之前的字符相同
        if current  == string[i]:
            #次数加1
             count += 1
        else:
            #输出上一组字符
            result.append(f"{current}({count})")
            #更新当前的字符
            current = string[i]
            #重置次数
            count = 1
    #循环结束后，还需要将最后一组字符添加到列表
    result.append(f"{current}({count})")
    # 将列表拼接成字符串并返回
    return "".join(result)

# 测试
print(string_zip())

