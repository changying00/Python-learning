#【列表】给定一个列表、判断该列表是否是已经排序好(升序)的~
# 定义一个列表，传入数据

ls1 = [1,2,3,12,23,24,25,42,32,44,55,62,74,234]
#如何判断列表 是否为排序好的？难道要用算法一个一个比吗？
#如果把一个列表用方法排序好，然后俩个对比，相同就是排序好了，不相同就是没排序好
ls2= sorted(ls1) #默认升序，reverse = True 是降序 ,reverse=False 升序，默认
if ls1 == ls2:
    print("该列表是已经排序好的(升序)")
else:
    print("该列表没有排序好")
print(ls2)


#第二种写法
# ls1 = [1,2,3,12,23,24,25,42,32,44]
# is_sorted = True
# for i in range(len(ls1) - 1):
#     if ls1[i] > ls1[i + 1]:
#         is_sorted = False
#         break
# if is_sorted:
#     print("已经排序")
# else:
#     print("没有排序")