#【字典】给定字典 {'Tom': 80, 'Jerry': 95, 'Spike': 50}，
# 按分数从高到低排序，返回排序后的列表 [('Jerry',95), ('Tom',80), ('Spike',50)]
#定义一个变量存储字典

dic1 = {'Tom': 80, 'Jerry': 95, 'Spike': 50}
#由于sort是list的方法，元组字典集合用不了，所以使用sorted内置函数进行
tup = sorted(dic1.items(), key=lambda x: x[1],reverse=True)
print(tup)