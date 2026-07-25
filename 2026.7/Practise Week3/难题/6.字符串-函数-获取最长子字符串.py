#【函数】编写一个函数、用来获取字符串最长的不重复子串，例如 abcae 最长的子串是 bcae
"""思考：获得全部的字符串 ，然后在所有的子字符串中,挑选最长不重复的字串"""
def cycle_string(string = "abcae") :
    #定义一个ls空列表
    result  = []
    #循环遍历每一个元素
    for i in range(len(string)):
            #控制结束位置
            for j in range(i+1,len(string) +1):
                # 截取子字符串
                sub = string[i:j]
                # 判断是否没有重复字符
                if len(sub) == len(set(sub)):
                    result.append(sub)
    #假设最长的字符串为result1[0]
    max_string = result[0]
    # 找最长字符串
    for item in result:

        if len(item) > len(max_string):
            max_string = item
    return max_string


print(cycle_string("abcae"))
#我写的时间复杂度太高
#下面的是更完美的写法
"""
【函数】
获取字符串最长的不重复子串
"""
def longest_unique_substring(string):
    # 保存窗口内的字符
    window = set()
    # 左指针
    left = 0
    # 记录最长字符串
    max_string = ""
    # 右指针遍历字符串
    for right in range(len(string)):
        # 当前字符
        char = string[right]
        # 如果当前字符已经存在窗口中
        # 说明出现重复
        while char in window:
            # 删除左边字符
            window.remove(string[left])
            # 左指针向右移动
            left += 1
        # 当前字符加入窗口
        window.add(char)
        # 获取当前窗口字符串
        current_string = string[left:right + 1]
        # 更新最长字符串
        if len(current_string) > len(max_string):
            max_string = current_string
    return max_string
# 测试
print(longest_unique_substring("abcaee"))