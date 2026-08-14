"""
求一个列表中的最大值 和 最小值 

"""
# 定义一个列表 
ls = [34, 68, 1, 23, 78, 82]

# 定义 2个变量、分别存储最大值 和 最小值 
max_number = min_number = ls[0]

# 从 第二个元素 进行遍历 
for v in ls[1:]:

    if max_number < v:
        max_number = v 

    if min_number > v:
        min_number = v 

print(max_number, min_number)