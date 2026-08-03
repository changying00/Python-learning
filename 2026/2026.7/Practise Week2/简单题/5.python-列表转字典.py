#【字典】把列表 ['Tom', 'Jerry'] 转换为字典，key 是索引，value 是名字：{0:'Tom',1:'Jerry'}。
#定义一个变量储存列表值
ls1 = ['Tom', 'Jerry']
#range(2),得到0，1，通过zip打包，最后通过dict转成字典
#range(2)不通用改成len(ls1）
dic = dict(zip(range(len(ls1)),ls1))
#打印结果
print(dic)