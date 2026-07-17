class File:
    # 定义一个类的属性，代表读权限
    READ = 4

    # 定义一个类的属性，代表写权限
    WRITE = 2

    # 定义一个类的属性，代表执行权限
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


# 创建一个文件对象，并设置权限：读 + 写 + 执行
file = File(
    "D:/abc/123.py",
   10
)

print(file.can_read())
print(file.can_write())
print(file.can_execute())