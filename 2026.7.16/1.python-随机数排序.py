"""

"""
import random
ls = [1,43,76,2,3,71,5,9,7]
while True:
    #检查 列表是否已排序好
    check_list = [ls[i]>ls[i-1] for i in range(1,len(ls))]
    # 如果 False 在里面
    if False in check_list:
        #随机打乱
        ls.sort(key = lambda d:random.random())
    else:
        break
print(ls)