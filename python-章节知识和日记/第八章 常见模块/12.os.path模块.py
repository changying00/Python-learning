"""
os.path : 和 路径相关的 操作 

该模块 常见的方法:

    - os.path.abspath(path) :  获取 指定路径的 绝对路径

    - os.path.exists(path) :  判断指定的路径在磁盘中 是否存在
    - os.path.isfile(path) :  判断指定的路径 是否是 一个文件
    - os.path.isdir(path) :  判断指定的路径是否是一个目录 

    - os.path.basename(path) : 获取指定的文件/目录 对应的名字 
    - os.path.dirname(path) :  获取指定的文件/目录的 上一级目录 
    - os.path.split(path) :  将一个指定的路径 进行拆分、并获取 对应的 上一级目录路径 和 (目录/文件)名字
    - os.path.join(path, path2) : 将 2个路径 进行拼接 、path2 必须是一个 相对路径 

    - os.path.getsize(file) :  获取 一个 指定文件的 大小、返回 字节数
    
    - os.path.ctime(path) : 获取一个 文件/目录的 创建时间 
    - os.path.mtime(path) : 获取一个 文件/目录的 修改时间
    - os.path.atime(path) : 获取一个 文件/目录的 访问时间


"""
import os.path 
from datetime import datetime 


print(os.path.abspath("./abc"))

print(os.path.exists("./abc"))

print(os.path.isfile("./第一章 Pytthon入门基础/1.初始模块化编程.py"))

print(os.path.isdir("./第一章 Pytthon入门基础"))

# 获取 路径中 文件/目录 的名字 
print(os.path.basename("./第一章 Pytthon入门基础/1.初始模块化编程.py"))

# 获取 指定路径的 父目录 
print(os.path.dirname("./第一章 Pytthon入门基础/1.初始模块化编程.py"))

print(os.path.split("./第一章 Pytthon入门基础/1.初始模块化编程.py")) 

print(os.path.join("./abc", "D:/ttt/xyz"))

print(os.path.getsize("./第一章 Pytthon入门基础/1.初始模块化编程.py"))

# atime 访问时间   ctime 创建时间  mtime 修改时间
print( datetime.fromtimestamp( os.path.getatime("./第一章 Pytthon入门基础/1.初始模块化编程.py")))
print( datetime.fromtimestamp( os.path.getctime("./第一章 Pytthon入门基础/1.初始模块化编程.py")))
print( datetime.fromtimestamp( os.path.getmtime("./第一章 Pytthon入门基础/1.初始模块化编程.py")))