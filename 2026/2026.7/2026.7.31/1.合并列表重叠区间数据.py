from typing import List,Tuple


def combine_list(data:List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    """合并 列表中 重叠区间的数据"""
    #对传入的列表 进行 排序
    data = sorted([tuple(tp) for tp in data])
    #定义一个容器、用来存储最终的结果
    result = []
    #定义一个变量、用来存储 临时要处理的数据
    temp  = ()
    #遍历整个数据
    for a,b in data:
        #如果 临时数据 是空的、将当前数据 作为临时数据
        if len(temp) == 0:
            temp = (a,b)
        elif temp[0] <= a <= temp[1]:
            #合并区间
            temp = (temp[0],max(b,temp[1]))
        else:
            #没有重叠区间、降临时数据添加到结果中
            result.append(temp)
            temp = (a,b)
    #整个循环结束后、将临时数据 添加到结果中
    if len(temp) > 0:
        result.append(temp)

    return result

if __name__ == '__main__':
    #测试函数
    ls = [(1,3),(2,3),(6,7),(8,12)]
    print(combine_list(ls))