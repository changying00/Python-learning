#【字典】给定列表 ['a', 'b', 'c'] 和 range(3)，生成字典 {'a': 0, 'b': 1, 'c': 2}
#定义一个变量存储列表
ls1 =  ['a', 'b', 'c']
#通过dict()和zip打包，生成对应的字典
dic1 = dict(zip(ls1,range(3)))
#打印结果
print(dic1)