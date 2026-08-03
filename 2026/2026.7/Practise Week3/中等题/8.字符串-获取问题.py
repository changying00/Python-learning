"""
【函数】编写一个函数、获取一个字符串的所有 子字符串，例如 abc ==> ["a", "ab", "abc", "b", "bc", "c"]。
尝试使用 循环、递归、生成器三种手段实现
"""
#方法一，循环函数实现获得子字符串
def cycle_string(string = "abc") :
    #定义一个ls空列表
    result1  = []
    #循环遍历每一个元素
    for i in range(len(string)):
            #控制结束位置
            for j in range(i+1,len(string) +1):
                #截取子字符串
                result1.append(string[i:j])

    return result1

# 测试
print(cycle_string("abc"))

#方法2、生成器实现
def string_generator(string = "abc") :
     for i in range(len(string)):
         for j in range(i+1,len(string)+1):
             yield string[i:j]

#测试
gen = string_generator("abc")
ls = []
for item in gen:
    ls.append(item)
print(ls)

#方法三、递归实现
def recursive_string(string):
    # 空字符串结束
    if len(string) == 0:
        return []
    result = []
    # 获取当前字符串所有开头子串
    for i in range(1, len(string) + 1):
        result.append(string[:i])
    # 递归处理剩余字符串
    result.extend(
        recursive_string(string[1:])
    )
    return result
print(recursive_string("abc"))