"""
【lambda】编写一个函数 list_filter 、
具备按照索引和元素 过滤 列表中元素的能力。
a: 获取列表中 索引为 奇数的所有元素

b. 获取列表中 索引为奇数且元素为偶数的元素

c. 获取列表中 字符串长度大于 3且小于10的元素

20分钟
"""
# 定义过滤函数
def list_filter(target, condition):
    result = []
    # 同时遍历索引和元素
    for index, item in enumerate(target):
        # 如果满足条件，就加入结果列表
        if condition(index, item):
            result.append(item)
    return result

# 测试数据
ls1 = [1, 2, 23, 41, "bibiw", 41, 23, "ni", "hxshisb", "dgx521"]

# a. 获取索引为奇数的所有元素
result1 = list_filter( ls1,lambda index, item: index & 1 !=0)
print("a:", result1)

# b. 获取索引为奇数且元素为偶数的元素
result2 = list_filter(ls1,lambda index, item: index % 2 == 1 and isinstance(item, int) and item % 2 == 0)
print("b:", result2)

# c. 获取字符串长度大于3且小于10的元素
result3 = list_filter(ls1,lambda index, item: isinstance(item, str) and 3 < len(item) < 10)
print("c:", result3)
