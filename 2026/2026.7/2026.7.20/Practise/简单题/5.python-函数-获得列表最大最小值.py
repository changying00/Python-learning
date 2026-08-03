"""
简单题 【函数】编写一个函数 max_and_min(list) 获取列表中的最大、最小的元素 不允许使用内置 max , 和 min 函数

"""
#定义一个函数，名为max_and_min
def max_and_min(nums):
    """传入一个列表，返回列表中的最大值和最小值"""
    #首先赋值给最小值和最大值列表中的第一个元素
    max_num = min_num = nums[0]
    # 进行遍历列表
    for i in nums:
        #如果这个i值比最大值大，把这个值赋给最大值
        if i > max_num:
            max_num = i
        #如果这个i值比最小值小、把这个值给最小值
        if i < min_num:
            min_num = i
    return max_num,min_num
print(max_and_min([22,23,355,41521,25,36,77,8,9]))