"""
位或/与运算符 实现权限校验

"""
permission = int(input("请输入一个 0 ~ 7 之间的任意整数"))

# 定义三个变量、分别代表 读写可执行权限 
r, w, x = 4, 2, 1
# 定义一个变量、存储是否可读
can_read = (permission & r) == r
can_write = (permission & w) == w 
can_execute = (permission & x) == x 

print("当前文件是否可读", can_read)
print("当前文件是否可写", can_write)
print("当前文件是否可执行", can_execute)

