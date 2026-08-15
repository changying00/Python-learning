"""
【递归】编写一个函数 、获取指定目录下所有的文件（绝对路径）组成的列表、包含所有子目录下的内容
"""
from typing import List
import  os

def get_contents(directory:str) ->List[str]:
    """获取一个 指定目录下的所有内容"""

    #存储 所有的资源路径
    files = []
    #获取该目录 下的所有内容
    contents = os.listdir(directory)
    for name in contents:
        #获取name、代表的资源 它的完整路径
        path = os.path.abspath(os.path.join(directory, name))
        #判断 当前路径是文件还是文件夹
        files.append(path)
        if os.path.isdir(path):
            #递归获取 该目录下的所有内容
            files += get_contents(path)
    return files

if __name__ == "__main__":
    files =get_contents("./")
    for v in files:
        print(v)