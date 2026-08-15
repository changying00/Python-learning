"""
【递归】编写一个函数、实现删除一个目录、不允许使用官方(shutil模块)自带删除目录方法！
"""
from typing import List
import  os

def remove_contents(directory:str) ->List[str]:
    """删除 指定目录下的所有内容"""
    #获取该目录 下的所有内容
    contents = os.listdir(directory)
    for name in contents:
        path = os.path.join(directory, name)

        if os.path.isdir(path):
            remove_contents(path)
        else:
            os.remove(path)
    os.rmdir(directory)

if __name__ == "__main__":
    files =remove_contents(r"C:\Users\QK\Desktop\python\remove")