"""
【函数】编写一个函数 selectionSort(list) 实现 list 列表的选择排序
"""
#定义一个函数实现列表的选择排序
def selectionSort(list_num):
    """
    :param list_num: 用于接收列表的参数
    :return: 返回排序好的列表
    list = [1,3,42,21,33,12 ]
    """
    for i in range(len(list_num)-1):
        for j in range(i+1, len(list_num)):
            # 假设当前元素最小
            min_index = i
            if list_num[j] < list_num[min_index]:
                min_index = j
                # 交换最小值
            list_num[i], list_num[min_index] = list_num[min_index], list_num[i]
    return list_num
print(selectionSort([22,32,24,15,36,7]))