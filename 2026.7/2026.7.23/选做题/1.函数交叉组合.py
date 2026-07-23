#【函数】编写一个函数、使用循环将多个 列表中的数据 交叉组合。例如 [1, 2, 3] , [4, 5] ====>
# [ (1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5) ]
from typing import List,Any,Tuple
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
ls1 =[1,2,3]
ls2 =[4,5]
print(cross_combination(ls1,ls2))