"""
 使用 递归 获取 某个 目录下所有的内容 
"""
from typing import List
import os 
 


def get_contents(directory: str) -> List[str]:
    """
    获取 一个 指定目录下的所有 内容 
    """
    # 存储 所有的 资源路径 
    files = []
    # 获取 该目录 下的所有 内容 (不包含子目录)
    contents = os.listdir(directory) 
    # 遍历 所有的 名字 
    for name in contents:
        # 获取 name 代表的 资源 它的完整路径 
        path = os.path.abspath(os.path.join(directory, name)) 
        # 判断 当前路径 是文件 还是 文件夹 
        files.append(path)
        if os.path.isdir(path):
            # 递归的获取该目录下的所有内容
            files += get_contents(path)

    return files 


if __name__ == "__main__":
    
    files = get_contents("./")

    for v in files:
        print(v)
