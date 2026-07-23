"""
【递归】编写一个函数、支持传入多个列表，使用递归的方式 实现数组的交叉组合 [1, 2], [3, 4] , [5, 6] ===>
 [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]
递归思路:
n 个列表的交叉组合 =  其中的任意一个列表  和  n - 1 个列表交叉组合的结果 进行 交叉组合

n -1 个列表的交叉组合 = 其中的任意一个列表  和 n - 2 个列表交叉组合的结果

3 个 列表的交叉组合  =  其中的任意一个列表   和    2 个列表交叉组合的结果

2 个 列表的交叉组合  =  其中的任意一个列表   和  1 个列表交叉组合的结果

收敛条件 -->>  当列表为1时结束
"""
from dis import RETURN_CONST

"""
递归实现多个列表交叉组合
"""
#
# def list_combination(*args):
#     # 收敛条件：
#     # 当只剩一个列表时，不需要继续递归
#     # 直接把列表里面的元素转换成元组返回
#     if len(args) == 1:
#         return [(i,) for i in args[0]]
#     # 取第一个列表
#     first = args[0]
#     # 剩余列表继续递归组合
#     rest = list_combination(*args[1:])
#     # 保存最终结果
#     result = []
#     # 第一个列表中的每个元素
#     for i in first:
#         # 和后面递归出来的每一个结果组合
#         for j in rest:
#             # 拼接成新的元组
#             result.append((i,) + j)
#     return result
#
# # 测试
# print(list_combination(
#     [1,2],
#     [3,4],
#     [5,6]
# ))
#老师解法
from typing import List,Any,Tuple

# def cross_combination(array: List[int],*args) -> List[Tuple[Any,...]]:
#     """ 计算 多列表交叉组合的结果"""
#     if len(args) == 0:
#         return [(v,) for v in array]
#
#     #如果 有多个列表、先计算 args中 多个列表的交叉组合
#     ret = cross_combination(args[0],*args[1:])
#     #将 array 和 ret 俩个列表 进行交叉组合
#     return [(v,*tp) for v in array for tp in ret]
# ls = [1,2]
# ls2 =[3,4]
# ls3 = [5,6]
# print(cross_combination(ls,ls2,ls3))

#基于循环的交叉组合
def cross_combination(array: List[int],*args) -> List[Tuple[Any,...]]:
    """实现 循环 多列表交叉组合"""
    #将 array 单列表 进行交叉组合
    ret = [(v,) for v in array]
    #遍历 剩余的所有的列表
    for rest in args:
        #rest 是一个列表、格式为[3,4]
        ret = [(*tp,v) for tp in ret for v in rest]
    #循环结束后、输出最终的结果
    return ret
ls = [1,2]
ls1 = [3,4]
ls2 = [5,6]
ls3 = [7,8,9]
print(cross_combination(ls,ls1,ls2,ls3))

