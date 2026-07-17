"""
【列表】给定列表 ['Python','is','fun']，生成所有单词长度的列表 [6,2,3]。
"""
#定义列表
ls1 = ['Python','is','fun']
#创建一个空列表lis2
lis2 = []
#定义一个for循环遍历ls1里面的元素
for i in range(len(ls1)):
    #len(lis[i])每一项的长度，增加到lis2列表
        lis2.append(len(ls1[i]))
#循环遍历，完成输出结果
print(lis2)