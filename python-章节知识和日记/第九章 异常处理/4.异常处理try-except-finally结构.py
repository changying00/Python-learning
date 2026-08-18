"""

try:  尝试 进行 异常捕获、 将 可能产生异常的代码 放到 try块中


except: 捕获 并处理 指定的异常 


finally: 无论是否产生异常 、都会执行的代码 



当 程序 执行了 try 块中的 代码，  就一定会执行 finally , 无论是否有异常 ~~~

finally 结构 通常 可以用来 关闭 连接、释放通道 等 资源 。 


python 中 也支持 直接使用 try - finally 结构 、 不处理异常、 使用 finally 关闭资源

"""

# def test():
#     a = 10
#     try:
#         a += 1

#         #  return a 这行代码 是 2 次运算 、 第一次运算 计算 a 表达式的结果 、第二次运算 将 计算的结果 返回给 调用者 
#         #  这 两个运算 不是 原子操作 、在 finally 中 这 2个运算 被 拆开 了，  
#         #  先 计算 表达式 a 的结果 、 在 执行 finally 中的 代码 、 最后 返回 计算的结果 给调用者
#         return a 
#     finally:
#         a += 1
    
# print(test())


# def test():
#     a = [10, 20, 30]
#     try:
#         a.append(40)
#         return a 
#     finally:
#         a.append(50)

# 输出列表 
# print(test())


# def test():
#     try:
#         return 10
#     finally:
#         try:
#             return 11
#         finally:
#             return 12
#         return 13
# print(test())





# try:
#     number = int(input("请输入一个整数"))
#     print(number)
# except:
#     print(3 / 0)
# finally:
#     print("无论是否产生异常、都会执行的代码")




