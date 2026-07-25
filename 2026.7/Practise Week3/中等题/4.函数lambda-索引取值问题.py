#【lambda】编写一个find_index 函数、获取可迭代对象中满足条件的第一个元素的索引、如果找不到、则返回 -1
#定义一个函数find_index
def find_index(target,condition):
    #通过索引遍历
    for i in range(len(target)):
        #判断对应的值是否满足条件
        if condition(target[i]):
            # #满足返回索引的值
            # if target[i] not in ls:
            #     ls.append(target[i])
                return  i
    #不满足返回-1
    return -1

#定义一个列表ls1
ls1 = [1,12,32,15,86,52,34,73,21,22,41,97,32,21]

result  = find_index(ls1,lambda x:x>50) #一旦遇到第一个元素直接return i 循环就结束了
print(result)
"""
for index, item in enumerate(target):
    if condition(item):
        return index
或者写成这个
"""