"""
"""
import os
class FileUtils:
from typing import Callable, List
    @classmethod
    def get_files(cls, path: str,  predicate: Callable[[str], bool] = None) -> List[str]:
        """根据 predicate条件获取指定目录下所有满足条件的文件"""
        files = []
        for name in os.listdir(path):
            file_path = os.path.join(path, name)
            if os.path.isfile(file_path):
                if predicate is None or predicate(file_path):
                    files.append(file_path)
            elif os.path.isdir(file_path):
                files.extend(cls.get_files(file_path, predicate))
        return files

    @classmethod
    def remove(cls, path: str) -> None:
        """删除文件或目录"""
        #判断path 是否为文件，如果是文件使用os.remove删除
        if os.path.isfile(path):
            os.remove(path)
        else:
            #不是文件就是，目录删除
            os.rmdir(path)

    @classmethod
    def get_parent(cls, path: str) -> str:
        """获取上一级路径"""   
        return os.path.dirname(path)
    
    @classmethod
    def get_name(cls, path: str) -> str:
        """获取路径对应的文件名"""
        return os.path.basename(path)

    @classmethod
    def get_size(cls, file: str) -> int:
        """ 获取文件的大小 """
        return os.path.getsize(file)

    @classmethod
    def is_dir(cls, path: str) -> bool:
        """判断路径是否是目录"""
        if os.path.isdir(path):
            return True
        return False

    @classmethod
    def is_file(cls, path: str) -> bool:
        """判断磁盘路径是否是 文件"""
        return os.path.isfile(path)
    @classmethod
    def exists(cls, path: str) -> bool:
        """判断路径是否存在 """
        return os.path.exists(path)

    @classmethod
    def get_ext(cls, file: str) -> str:
        """获取 文件 后缀名"""
        return os.path.basename(file)[1]

    @classmethod
    def copy_file_to_dir(cls, file: str,  directory: str)-> None:
        """拷贝一个文件到目录"""
        filename = cls.get_name(file)
        destfile = os.path.join(directory, filename)
        cl s.copy_file(file, destfile)
    @classmethod
    def copy_file(cls, srcfile: str,  destfile: str) -> None:
        """拷贝一个文件内容到 destfile文件中"""
        with open(srcfile, "rb") as src:
            with open(destfile, "wb") as dest:
                while True:
                    data = src.read(8192)
                    if not data:
                        break
                    dest.write(data)
    @classmethod
    def copy_directory(cls, src: str,  dest: str) -> None : 
        """将 src 文件夹中的内容拷贝到 dest 目录中 """
        if not os.path.exists(dest):
            os.mkdir(dest)
        for name in os.listdir(src):
            src_path = os.path.join(src, name)
            dest_path = os.path.join(dest, name)
            if os.path.isfile(src_path):
                cls.copy_file(src_path, dest_path)
            elif os.path.isdir(src_path):
                cls.copy_directory(src_path, dest_path)

    @classmethod
    def read_to_string(cls, file: str, encoding="utf-8") -> None:
        """读取一个字符文件中的内容，并返回字符串"""
        with open(file, "rt", encoding=encoding) as f:
            return f.read()

    @classmethod
    def chunks(cls, file: str,  chunk_size: int=8192) -> None:
        """编写一个生成器、用来读取一个大文件中的内容、每次读取 chunk_size 字节"""
        with open(file, "rb") as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                yield data

    @classmethod
    def writestr(cls, string: str,  file: str, encoding="utf-8") -> None:
        """将指定的字符串写入到指定的文件中"""
        with open(file, "wt", encoding=encoding) as f:
            f.write(string)

