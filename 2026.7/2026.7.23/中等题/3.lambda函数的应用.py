#【lambda】编写一个 take_while函数、保留满足条件的元素、直到不满足条件元素位置。
# 例如 [1, 2, 3, 4, 1, 2] 保留 小于 3的元素，则返回 [1, 2]

定义take_while函数
def take_while(target, condition):
    """
    根据条件函数保留元素
    遇到第一个不满足条件的元素停止
    :param target: 传入的列表
    :param condition: 判断条件(lambda函数)
    :return: 满足条件的列表
    """
    # 保存结果
    result = []
    # 遍历列表中的元素
    for item in target:
        # 判断元素是否满足条件
        if condition(item):
            # 满足条件加入列表
            result.append(item)
        else:
            # 第一次不满足，立即停止
            break
    return result
# 测试
nums = [1, 2, 3, 4, 1, 2]
result = take_while(nums, lambda x: x < 3)
print(result)


#第二种使用生成器
def take_while(target, condition):
    for item in target:
        if condition(item):
            yield item
        else:
            break
nums = [1,2,3,4,1,2]
gen = take_while(nums,lambda x: x < 3)
print(list(gen))

#list(gen) 会不断调用生成器的 next()，把每一次 yield 出来的值收集起来，直到生成器结束。
#可迭代对象(iterable) → 迭代器(iterator) → next() → StopIteration

#因为 list() 接收的是一个可迭代对象（iterator），它内部的工作方式就是不断调用 next() 获取元素，直到遇到 StopIteration。

#不是 list() 专门针对生成器，而是 Python 的迭代协议规定的行为。
