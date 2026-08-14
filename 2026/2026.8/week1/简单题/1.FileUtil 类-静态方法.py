"""
class FileUtils:

    @classmethod
    def get_files(cls, path: str,  predicate: Callable[[str], bool] = None) -> List[str]:
        """根据 predicate条件获取指定目录下所有满足条件的文件"""
        pass 

    @classmethod
    def remove(cls, path: str) -> None:
        """删除文件或目录"""   
        pass

    @classmethod
    def get_parent(cls, path: str) -> str:
        """获取上一级路径"""   
        pass
    
    @classmethod
    def get_name(cls, path: str) -> str:
        """获取路径对应的文件名"""
        pass 

    @classmethod
    def get_size(cls, file: str) -> int:
        """ 获取文件的大小 """
        pass

    @classmethod
    def is_dir(cls, path: str) -> bool:
        """判断路径是否是目录"""
        pass 

    @classmethod
    def is_file(cls, path: str) -> bool:
        """判断磁盘路径是否是 文件"""
        pass 

    @classmethod
    def exists(cls, path: str) -> bool:
        """判断路径是否存在 """
        pass 

    @classmethod
    def get_ext(cls, file: str) -> str:
        """获取 文件 后缀名"""
        pass 

    @classmethod
    def copy_file_to_dir(cls, file: str,  directory: str)-> None:
        """拷贝一个文件到目录"""

    @classmethod
    def copy_file(cls, srcfile: str,  destfile: str) -> None:
        """拷贝一个文件内容到 destfile文件中"""
        pass 

    @classmethod
    def copy_directory(cls, src: str,  dest: str) -> None : 
        """将 src 文件夹中的内容拷贝到 dest 目录中 """
        pass 

    @classmethod
    def read_to_string(cls, file: str, encoding="utf-8") -> None:
        """读取一个字符文件中的内容，并返回字符串"""
        pass 

    @classmethod
    def chunks(cls, file: str,  chunk_size: int=8192) -> None:
        """编写一个生成器、用来读取一个大文件中的内容、每次读取 chunk_size 字节"""
        pass

    @classmethod
    def writestr(cls, string: str,  file: str, encoding="utf-8") -> None:
        """将指定的字符串写入到指定的文件中"""
        pass

"""