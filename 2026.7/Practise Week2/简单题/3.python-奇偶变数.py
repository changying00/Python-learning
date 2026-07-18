# #【字典】将列表 [1,2,3,4]
# # 中偶数变为 'even'，奇数变为 'odd'，并生成形如 {1:'odd',2:'even',...} 的字典。
# #定义一个列表
# ls1 = [1,2,3,4]
# #定义一个空列表，用于存储值
# ls2 = []
# #用for循环遍历
# for i in ls1:
#     #判断奇偶，
#     if  i & 1 ==0:
#         #如为偶数则为"even"
#          ls2.append("even")
#     else:
#         #奇数增加为"odd"
#          ls2.append("odd")
# print(ls2)
# #把俩个列表对应的值通过zip打包一下，通过dict变成字典
# dir1 = dict(zip(ls1,ls2))
# print(dir1)

#字典列表推导式
ls1 = [1,2,3,4]
dir1 = { i: "even" if i & 1 == 0 else "odd" for i in ls1}
print(dir1)