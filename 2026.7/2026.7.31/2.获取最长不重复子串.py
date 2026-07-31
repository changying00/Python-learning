def get_norepeat_max_substring(string:str)->str:
    """获取字符串第一个最长的不重复子串"""
    #定义一个变量、用来存储 最长的不重复子串
    max_substring = ""
    #基于 索引和值的遍历
    for i,v in enumerate(string):
        #将 第一个 字符默认作为 最长的不重复的子串
        temp = v
        # 如果 当前max_substring 它的长度 已经大于剩余 要求的 子串长度
        if len(max_substring) > len(string[i+1:]):
            break
        #从 i+1 索引位置 开始 遍历字符串
        for x in string[i+1:]:
            #如果 x 不在 已知的最长子串中、说明 当前temp 不是最长
            if x not in temp:
                temp += x
            else:
                break
        if len(temp) > len(max_substring):
            #此时 将 temp 赋值给 max_substring
            max_substring = temp
    return max_substring

if __name__ == '__main__':
    print(get_norepeat_max_substring('abcaeaf'))