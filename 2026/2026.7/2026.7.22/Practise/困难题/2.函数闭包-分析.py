#【闭包】阅读下面的代码 、请分析代码执行的结果

func_list = []
for x in  range(8):
    #定义一个函数、并让函数输出x
    # func = lambda:print(x)
    #一句话记住：lambda x=x 的作用，就是把当前循环中的 x 值“拍照保存”到函数的默认参数里，避免后面 x 变化时影响已经创建好的函数。
    func = lambda x=x: print(x)
    #将函数存储到列表中
    func_list.append(func)

#遍历列表、并调用里面的所有函数
"""
这时候 Python 开始查找 x：

先在 lambda 自己内部找 —— 没有。

再到外层作用域找 —— 找到了循环变量 x。

此时 x 的值已经是 3。
"""
for  func in func_list:
    # 调用函数
    func()
#代码执行的结果是0，1，2，3吗如果不是改造代码让其能够打印0，1，2，3
#func = lambda:print(x)等于下面的代码
# import functools
#
# def func_change(target):
#     @functools.wraps(target)
#     def func_print(*args,**kwargs):
#         result = target(*args,**kwargs)
#         for i in range(int(result)):
#             print(i)
#         return result
#     return func_print
#
# @func_change
# def func(x):
#     print(x)
# print(func(4))
#
# func_list = []
# for x in range(4):
#     def make_func(x):
#         return lambda: print(x)
#     func_list.append(make_func(x))
#
# for func in func_list:
#     func()
#
"""
(lambda: print(1))():

lambda: print(1) == 下面的写法
 def temp():
    print(1)

(lambda: print(1)) 这表示“这是一个函数对象”。
(lambda: print(1))() 最后的 () 就像你平时写的 temp() 一样，表示调用函数。


"""
