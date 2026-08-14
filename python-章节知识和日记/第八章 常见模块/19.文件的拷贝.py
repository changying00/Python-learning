
# file = r"E:\EV\01.math数学模块.mp4"
from ntpath import isfile
import os


def copy_file(file, dest):
    """将一个文件拷贝到 指定的目录中"""
    # 采用 边读 编写的模式 进行 文件拷贝 
    with open(file, "rb") as f:
        dest_path = os.path.join(dest, os.path.basename(file))
        # 打开一个 写入通道 
        with open(dest_path, "wb") as w:
            # 一次性读取 8kb 
            while (data := f.read(8 << 10)) != b"":
                w.write(data)


#  将一个 文件夹 下的所有内容 拷贝到 指定的 目录中 

def copy_directory(src, dest):
    """
    将 src 目录中的内容 拷贝到 dest 目录中 
    """
    # 遍历 src 目录下的所有内容 
    for name in os.listdir(src):
        # 获取 name 的 路径 
        path = os.path.join(src, name)

        if os.path.isfile(path):
            copy_file(path, dest)
        else:
            # 如果 是文件夹 、创建该文件夹 
            dest_path = os.path.join(dest, name)
            # 创建目录 
            os.mkdir(dest_path)
            # 将 path 文件夹中所有的内容 拷贝到 dest_path 目录中
            copy_directory(path, dest_path)


if __name__ == "__main__":
    
    src = r"C:\Users\Administrator\Desktop\coffee-manage-sys"

    dest = "./qiku00001"

    copy_directory(src, dest)





