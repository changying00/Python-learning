"""
创建一个包含字典的列表，尝试访问列表中索引为 5 的元素的键 "name"。捕获 IndexError 和 KeyError 异常，并分别打印适当的消息
"""
try:
    ls = [{'age':21},
          {'gender':"男"},
          {'birth':20040619},
          {"time":8.17},
          {"name":"dgx"},
          {"color":"bule"}]
    print(ls[5]["name"])

except (IndexError) as e:
    print("索引超过列表范围",str(e))

except KeyError as e:
    print("字典键名错误",e.args[0])

