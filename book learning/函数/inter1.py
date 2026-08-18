"""
函数-求序列交集
"""


#定义 Definition
def intersect(seq1,seq2):
	res = []                #初始为空
	for i in seq1:			#for 遍历第一个列表				
		if i in seq2:		#遍历一次 取出的元素 与seq2判断是否有相同的
			res.append(i)	#相同则增加到新列表
	return res				#循环结束、输出结果
    
#调用 calls

#from inter1 import intersect     # 从模块获取函数，假如在其他模块想使用，就导入
s1 = 'HACK'
s2 = 'CHOK'
result = intersect(s1, s2)                # 传入两个字符串，并把返回结果赋值给result
print(result)    #打印结果

#列表推导式 list comprehension
result2= [x for x in s1 if x in s2]
print(result2)

#lambda 函数实现
intersect = lambda seq1,seq2: [x for x in seq1 if x in seq2]
print(intersect(s1,s2))


#传入混合类型，一个列表和一个元组（混合类型）
#对 intersect 来说，这意味着：第一个参数必须支持 for 循环，第二个参数必须支持 in 成员测试
x = intersect([1,2,3],(1,4))# 传入混合类型
print(x)                                 