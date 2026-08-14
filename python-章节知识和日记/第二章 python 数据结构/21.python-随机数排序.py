"""
随机数 排序 

    思路 :  
    
        a) 随机打乱 列表 
        b) 判断 列表 是否是排序后的列表 (从小到大)
        c) 如果 没有排序 、冲虚 上述过程

"""
import random 


ls = [1, 43, 76, 2, 3, 71, 5, 9, 7]

while True:
    # 检查 列表是否已排序好 
    check_list = [ls[i] >= ls[i-1] for i in range(1, len(ls)) ]

    # 如果 False 在 里面 
    if False in check_list:
        # 随机打乱 
        ls.sort(key=lambda d: random.random())
    else:
        break 

print(ls)