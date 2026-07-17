#【列表】有一份学生成绩列表 例如 [[小明, 80], [小红, 95], [小强, 70]]，按成绩降序输出。

# #定义列表储存数据
# ls_sort  = [["小明",80],["小红",95],["小强",70]]
# #定义一个for 循环遍历每个学生的成绩
# for i in range(len(ls_sort)):
#     #定义一个for 循环遍历每个ls_sort[i]里面的第二哥元素
#     for j in range(len(ls_sort[i])-i):
#             if ls_sort[i][j]<ls_sort[i+1][j]:
#              ls_sort[i],ls_sort[i+1]= ls_sort[i+1],ls_sort[i]
# #输出结果
# print(ls_sort)
#
# 定义列表储存数据
ls_sort = [["小明", 80], ["小红", 95], ["小强", 70]]

# 使用内置的 sort() 方法进行成绩降序排序
ls_sort.sort(key=lambda x: x[1], reverse=True)

# 输出结果
print(ls_sort)