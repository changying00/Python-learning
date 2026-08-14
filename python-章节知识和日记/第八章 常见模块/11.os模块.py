"""
OLLAMA_KEEP_ALIVE :  设置大模型存活时间 、值为 -1 代表 永久存活

os 模块 提供了 和 文件/目录 相关的 基本操作 

    os.environ : 获取 操作系统的环境变量、 返回一个形似字典的对象

    os.mkdir(path) : 创建 指定路径对应的 文件夹、如果 文件夹已经存在 、则 报错 、父级目录 必须存在，否则 也会报错 

    os.makedirs(path) : 创建 指定路径对应的 文件夹、支持 多级目录的创建, 如果目录存在，则报错，可以通过设置 exist_ok=True 解决报错问题

    os.rmdir(path) :  创建 指定路径 对应的 空目录 ,  目录不存在，则抛出 错误 

    os.removedirs(path) : 递归 删除指定路径 对应的 空目录

    os.listdir(path) :  获取 指定 目录下的 所有内容(不包含子目录下的内容)对应的 名字

    os.remove(path) :  删除 指定路径 对应的文件 

"""

import os 

# 操作 环境变量 
# print(os.environ.get("OLLAMA_KEEP_ALIVE"))
# print(os.environ.get("DEEPSEEK_API_KEY"))

# 使用 os 模块 创建一个 文件夹 
#  需要 设置 文件夹的 路径 、 路径支持 绝对路径 和 相对路径 
#  绝对路径 以 D:/ (window) 或者 以  / （Linux）开头 
#  相对路径 以 ./  或者  ../ 开头 。   ./ 代表 当前位置 ,  ../  上一级目录


# 获取 当前工作区对用的 路径 
# print(os.getcwd())

# 在 当前 工作区 下 创建一个 xyz 文件夹 
# os.makedirs("./abc/xyz", exist_ok=True)

# 删除 xyz 目录 
# os.rmdir("./abc/xyz")

# os.removedirs("./abc/xyz")

# for v in os.listdir("./"):
#     print(v)

# 删除 当前工作区 下的 requirements.txt 文件 

# os.remove(r"C:\Users\Administrator\Desktop\网盘配置方式 - 副本.txt")