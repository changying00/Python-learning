"""
【递归】编写一个函数、实现删除一个目录、不允许使用官方(shutil模块)自带删除目录方法！
"""
from typing import List
import  os

def remove_contents(directory:str) ->List[str]:
    """获取一个 指定目录下的所有内容"""

    #存储 所有的资源路径
    files = []
    #获取该目录 下的所有内容
    contents = os.listdir(directory)
    if contents == "":
        os.rmdir(directory)
    else:
        for name in contents:
            #获取name、代表的资源 它的完整路径
            path = os.path.abspath(os.path.join(directory, name))
            #判断 当前路径是文件还是文件
            if os.path.isdir(path):
                #递归获取 该目录下的所有内容
                os.remove(path)
            else:
                remove_contents(path)


if __name__ == "__main__":
    files =remove_contents("")