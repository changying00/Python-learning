
#【函数】编写一个函数，合并重叠的区间。例如，输入 [(1, 3), (2, 6), (8, 17), (15, 18)]，输出 [(1, 6), (8, 18)]。
"""
   第一次思考：#遍历取值、判断第一个元组的最后一位，和第下一个元组的第一位大小，如果后面元组的第一位大于第一个元组的第二位，则不合并
    #否则合并 把他们的俩个值都取出来，然后放到集合去重，在取出第一位和最后一位，放在一起
    第二次思考：考虑到set集合不能遍历所以上面的不好弄，但是直接把取的值进行对比不好了吗？ 当前的元组的第一个值和上个元组数据最后一个值对比，如果当前第一个值
    大于上一个则不合并，如果小于则有重叠，取俩个元组的最小和最大组成一个新的元组
"""
# #定义一个函数same_combine
# def same_combine(target):
#     #创建一个列表
#     ls = []
#     for i in range(1,len(target)):
#         if target[i][0] < target[i-1][1]:
#             #新的值
#             new_num = (target[i-1][0],target[i][1])
#             ls.append(new_num)
#     return ls
#
# #测试函数
# ls1 = [(1, 3), (2, 6), (8, 17), (15, 18)]
# print(same_combine(ls1))

# 定义函数
def same_combine(target):
    # 如果列表为空，直接返回
    if not target:
        return []
    # 保存合并后的结果
    result_num = []
    #先加入第一个区间
    result_num.append(target[0])
    #遍历剩余的区间
    for i in range(1,len(target)):
        #获取当前区间
        current = target[i]
        #获取已经合并结果中的最后一个区间
        last =  result_num [-1]
        #判断是否重叠
        if current[0] <= last[1]:
            #合并区间
            new_interval = (
                last[0],
                max(last[1],current[1])
            )
            #替换最后一个区间
            result_num[-1] = new_interval

        else:
            #没有重叠、直接添加
            result_num.append(current)
    return  result_num

# 测试
ls1 = [
    (1,3),
    (2,6),
    (8,17),
    (15,18)
]

print(same_combine(ls1))