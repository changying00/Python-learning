import  sys

ls = [1,2,3,44.5,6,6]
try:
    index = int(input("请输入一个要获取的数据对应的索引值:"))

    print(ls[index])
    print(ls * "3")
#捕获所有异常 except + 类型错误 例如（IndexError,....）+ as e(获取类型错误的原因)
# -》3种方式 1. e.args[0] 2.str(e) 3.str(sys.exception())
except:
    print('捕获所有异常',str(sys.exception()))
