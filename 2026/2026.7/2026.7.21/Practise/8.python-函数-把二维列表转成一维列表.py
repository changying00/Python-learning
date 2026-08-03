#【递归】已知一个列表、存储的数据中 可能包含 列表 且子列表中仍旧可能包含列表、
# 先编写一个函数 flat_list ,实现将列表进行扁平化处理。
# 例如 [ [1, 2, 3] , [ 4, [5, 6] ] , [7, [8, [9, 10]]]]
# 转换成 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def flat_list(ls):
    result = []
    for item in ls:
        if type(item) == list:
            result += flat_list(item)
        else:
            result.append(item)
    return result


ls1 =[ [1, 2, 3] , [ 4, [5, 6] ] , [7, [8, [9, 10]]]]
print(flat_list(ls1))