#【lambda】编写一个 lb_map 函数、能够实现将一个列表中的元素进行映射。 例如
# [1, 2, 3] ====> [3, 6, 9] 映射规则 原列表元素 乘以 3。

def lb_map(ls,consumer_func):
      return [consumer_func(v) for v in ls]
ls1= [1,2,3]
result_ls = lb_map(ls1,lambda x : x * 3)
print(result_ls)