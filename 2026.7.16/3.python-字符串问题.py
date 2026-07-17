#【列表】定义一个存储字符串的列表，并实现按照字符串的长度 进行降序排列
#定义一个存储字符串的列表
ls_Str =["DGX","HANX","LOVEDAS1232131223","Python","javascript"]
# #定义一个外层循环for，定义循环次数
# for i in range(1,len(ls_Str)):
#     #内层循环，进行以此比较
#     for j in range(len(ls_Str)-i):
#         #判断字符串的长度，第一个跟第二个比较
#         if len(ls_Str[j]) < len(ls_Str[j+1]):
#             #第二个大，就替换位置
#             ls_Str[j],ls_Str[j+1] = ls_Str[j+1],ls_Str[j]
# #循环结束输出
# print(ls_Str)

# 定义一个存储字符串的列表
strList = ["DGX", "HANX", "LOVEDAS1232131223", "Python", "javascript"]

# 使用内置函数 sorted() 和 lambda 表达式进行降序排序
sortedStrList = sorted(strList, key=lambda x: len(x), reverse=True)

# 输出排序后的列表
print(sortedStrList)