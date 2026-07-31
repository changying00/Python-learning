"""
【字符串】编写一个函数 unique_sub_str(string),
获取字符串中所有可能的不重复的连续子串。
例如 abcac ===> [a, ab, abc, b, bc, bca, c, ca, ac]
"""
#定义一个函数 unique_sub_str
def unique_sub_str(string):
    """获取字符串中所有可能的不重复的连续子串。"""
    #定义一个变量、存储最终的结果
    result  = []
    #定义一个变量、存储临时字符串
    temp = ""
    #遍历
    for i,v in enumerate(string):
        #把v的值直接赋值给temp
        temp = v
        #判断result 是否已经有了一样的
        if temp not in result:
            result.append(temp)
        #在进行遍历，取i后面的字符串
        for j in string[i+1:]:
            #现在temp已经取了一个值，只需要判断下一个是否在temp里面
            if j not in temp:
                #不在的话就相加
                temp += j
                #把加过的值直接加到result，
                result.append(temp)
            else:
                #遇见一个不一样的直接跳出这循环说明，没有连续不重复的了
                break
    return result
if __name__ == "__main__":
    string = "abcacf"
    print(unique_sub_str(string))
