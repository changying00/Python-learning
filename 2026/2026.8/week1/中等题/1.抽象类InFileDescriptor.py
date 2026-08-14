"""
定义一个抽象类 InFileDescriptor 类
提供 read(self , n=1)  抽象方法 、实现一次读取指定长度的数据
提供 readall(self) 抽象方法、  实现一次性读取所有数据
提供 chunks(self,  chunk_size=None) 、一次性读取 chunk_size 数据,默认读取 8192 (8 * 1024)、并返回一个生成器对象
提供 close(self)抽象方法 、负责关闭通道
定义一个 FileReader类继承InFileDescriptor 、专门负责 读取字符文件，并提供如下属性和方法 私有属性： path (文件路径) ， encoding (编码方式)

初始化函数 __init__(path , *,  encoding="UTF-8")
成员方法有：
1. read(self,  n=1) :  读取n个字符, 默认 一次读取一个
2. readline(self) :   读取一行内容
3. readlines(self) :  读取所有行内容、返回列表
4. readall(self)  :  读取所有内容、返回字符串
5. close(self) : 	关闭文件管道
定义一个 FileInputStream 类继承InFileDescriptor 、专门负责 读取字节文件，并提供如下属性和方法 私有属性： path (文件路径)

初始化函数 __init__(path)
成员方法有：
1. read(self,  n=1) :     读取n个字节, 默认 一次读取一个字节
2. readall(self)  :  读取所有内容、返回字符串
3. close(self) : 关闭文件管道
编写 类的测试代码、完成 文件的读取
"""
from abc import ABC ,abstractmethod
#定义抽象类
class InFileDescriptor(ABC):

    @abstractmethod
    def read(self,n = 1):
        pass

    @abstractmethod
    def readall(self):
        pass

    def chunks(self, chunk_size=None):
        if chunk_size is None:
            chunk_size = 8 * 1024
        while True:
            content = self.read(chunk_size)
            if content == '' or content == b'':
                break
            yield content
    @abstractmethod
    def close(self):
        pass

class FileReader(InFileDescriptor):
    def __init__(self,path ,*,encoding="UTF-8"):
        self._path = path
        self._encoding = encoding
        self._file = None

    #定义打开 读取 文本文件
    def open_path(self):
        self._file = open(self._path, "rt", encoding=self._encoding)
        return self._file
    #读取n 个字符、默认 一次读取一个
    def read(self,n= 1):
        content = ""
        f = self.open_path()
        while (text := f.read(100)) != '':
           content += text
        self.close()
        return content
    #读取一行内容
    def readline(self):
        content = ""
        f = self.open_path()
        while (text := f.readline()) != '':
            content += text
        self.close()
        return content
    #读取所有行内容、返回列表
    def readlines(self):
        content = self.open_path().readlines()
        self.close()
        return content
    #读取所有内容、返回字符串
    def readall(self):
        f = self.open_path()
        content = f.read()
        self.close()
        return content
    #关闭文件通道
    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None
class FileInputStream(InFileDescriptor):

    def __init__(self,path):
        self.__path = path
        self.__file = None
# 打开字节文件
    def open_path(self):
        self.__file = open(self.__path, "rb")
        return self.__file

    # 读取 n 个字节
    def read(self, n=1):
        f = self.open_path()
        content = f.read(n)
        self.close()
        return content

    # 读取所有内容
    def readall(self):
        f = self.open_path()
        content = f.read()
        self.close()
        return content

    # 关闭文件
    def close(self):
        if self.__file is not None:
            self.__file.close()
            self.__file = None

if __name__ =="__main__":
    path = r"C:\Users\QK\Desktop\open code\txt\ch01.txt"

    reader = FileReader(path)

    # print("read(5)：")
    # print(reader.read(5))

    print("readline()：")
    print(reader.readline())
    #
    # print("readlines()：")
    # print(reader.readlines())
    #
    # print("readall()：")
    # print(reader.readall())