"""
位或运算 | :  相同位 只要有 1 结果为 1， 否则 为 0
    (一真即真)
    
    
位或的应用场景 
    
    合并权限 


现要求设计一个 文件权限系统 、包含的权限 有  可读、可写、可执行 ~~~

可读 使用 数字 4 (0b0100) 表示、 二进制 从 右到左 第三位 如果 为 1、则代表 可读
可写 使用 数字 2 (0b0010) 表示、 二进制 从 右到左 第二位 如果 为 1、则代表 可写
可执行使用数字 1 (0b0001) 表示、 二进制 从 右到左 第一位 如果 为 1、则代表 可执行 

"""


# 定义一个数字、用来表示 当前的签到情况 
number = 234367

print(bin(number))

n = 8
# 判断 8号是否签到 
mash = 2 ** (n - 1)

if number & mash == 0:
    # 如果没有签到 
    print(n, "号未签到、正在补签中...")
    # 进行补签 
    number = number | mash
    print(bin(number))
else:
    print(n, "号已签到")


class File:   
    # 定义一个类属性 代表读权限
    READ = 4
    # 定义一个类属性 代表写权限
    WRITE = 2
    # 定义一个类属性 代表可执行权限
    EXECUTOR = 1
    
    def __init__(self, path, number):
        self.path = path 
        self.number = number 
    
    def can_read(self):
        """判断是否可读"""
        return self.number & self.READ == self.READ
        
    def can_write(self):
        """判断是否可写"""
        return self.number & self.WRITE == self.WRITE
        
    def can_execute(self):
        """判断是否可执行"""
        return self.number & self.EXECUTOR == self.EXECUTOR
        
# 创建一个文件对象、并设置该文件的权限为 读写可执行
file = File("D:/abc/123.py", File.READ | File.WRITE | File.EXECUTOR)
print(file.can_read())
print(file.can_write())
print(file.can_execute())




