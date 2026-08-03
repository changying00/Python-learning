#【lambda】编写一个函数 drop_while、具备删除满足条件的元素、直到不满足条件为止。
# 例如 [1,2,3,4,1,2] ， 要求删除 小于 3的元素，最后返回 [3, 4, 1, 2] 即可。

def drop_while(ls,predicate):
    result = []
    flag  = False
    for v in ls:
        if not flag and predicate(v):
            continue
        else:
            flag = True
            result.append(v)
    return result

ls1 = [1,2,3,4,1,2]
print(drop_while(ls1,lambda x: x < 3 ))