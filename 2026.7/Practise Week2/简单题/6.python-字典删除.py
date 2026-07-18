#【字典】给定字典 {'a':1,'b':2,'c':3} 和列表 ['a','c']，删除字典中这些 key，返回新字典。
#定义一个变量dic 存储字典
dic = {'a':1, 'b':2, 'c':3}
#定义一个变量ls1 存储列表
ls1 = ['a','c']
#创建一个空字典
new_dic = {}
#遍历键和值
for key,value in dic.items():
    #判断键的值是否在列表中
    if key not in ls1:
        #如果不在把这个键，加到给空字典
        new_dic[key] = value

print(new_dic)