"""
【多维列表】现有1个元组、 格式为 ("name", "age" , "sex") ，
 有 一个二维列表 [ ("张三", 20, "男" ), ("李四", 20, "女" ) ] 将 上述 二个格式的数据转换为 

[ [("name", "张三" ) , ("age", 20), ("sex", "男") ] , [("name", "李四" ) , ("age", 20), ("sex", "女") ] ]



zip 函数 
    a) 实现数据压缩:   
        将 多个 可迭代对象 同位置 元素 进行 合并 、并 使用 元组 进行存储 

    b) 实现数据解压缩

"""

# 定义一个 变量、存储 元数据 
meta_data = ("name", "age", "sex")

# 定义一个变量 、存储 数据 
data = [("张三", 20, "男" ), ("李四", 20, "女" )]


ret = [ list(zip(meta_data, d)) for d in data]

# 列表生成推导式 实现 2个 效果  
#  1.  实现 数据的过滤 、保留满足条件的数据 
#  2.  实现 数据的映射 

# 定义一个 列表、用来存储 最终的结果
# ret = [[(meta_data[x], d[x]) for x in range(len(d))] for d in data]

# new_ls = [] 

# 遍历 data 、将 data 中的数据 转换成 最终的数据格式 
# for d in data:
#     # 将 2 个元组 进行 同位 合并 
#     new_ls.append([(meta_data[x], d[x])  for x in range(len(d))])

print(ret)


#定义一个元组
tp = ("name", "age" , "sex") 
#定义一个二维列表
ls = [ ("张三", 20, "男" ), ("李四", 20, "女" ) ]

#使用 zip 函数 将数据 进行压缩
ret = [ list(zip(tp, tp1)) for tp1 in ls]
print(ret)

































