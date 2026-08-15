"""
定义一个抽象类 OutFileDescriptor 类
提供 write(self , data: Union[str, bytes] ,  start = 0 ,  length: int = None)  抽象方法 、写入指定长度的内容，默认写入所有传入的数据
提供 flush()  抽象方法、实现强制写入
提供 close(self)  抽象方法 、负责关闭通道
定义一个 FileWriter类继承OutFileDescriptor 、专门负责写入数据到字符文件，并提供如下属性和方法 私有属性： path (文件路径) ， encoding (编码方式) ， append （是否追加内容、默认覆盖文件内容）

初始化函数 __init__(path , *,  encoding="UTF-8",  append=False)
成员方法有：
1. write(self , data: str ,  start = 0 ,  length: int = None) :  写入指定长度的内容
2. newline(self) :   写入一个换行符
3. flush(self) :   强制写入
4. close(self) : 关闭文件管道
定义一个 FileOutputStream 类继承OutFileDescriptor 、专门负责写入数据到字节文件，并提供如下属性和方法 私有属性： path (文件路径) ， append （是否追加内容、默认覆盖文件内容）

初始化函数 __init__(path)
成员方法有：
1. write(self , data: str ,  start = 0 ,  length: int = None) :  写入指定长度的内容
2. flush(self) :   强制写入
3. close(self) : 关闭文件管道
编写 类的测试代码、完成 文件的读取
"""
from typing import  Union
from abc import ABC ,abstractmethod
class OutFileDescriptor(ABC):

    @abstractmethod
    #写入指定长度的内容，默认写入所有传入的数据
    def write(self, data: Union[str, bytes] , start: int = 0, length: int = None):
        pass

    @abstractmethod
    #实现强制写入
    def flush(self):
        pass
    @abstractmethod
    #抽象方法 、负责关闭通道
    def close(self):
        pass
#专门负责写入数据到字符文件，并提供如下属性和方法 私有属性： path (文件路径) ， encoding (编码方式) ， append （是否追加内容、默认覆盖文件内容）
class  FileWriter(OutFileDescriptor):

    def __init__(self,path,*,encoding = "UTF-8",append = False):
        self.path = path
        self.encoding = encoding
        self.append = append
        self.__file = None
    def open_txt(self):
        if self.append:
            mode = "at"
        else:
            mode = "wt"
        self.__file = open(self.path,mode,encoding=self.encoding)
        return self.__file
    #写入指定长度的内容
    def write(self, data: Union[str, bytes] , start: int = 0, length: int = None):
       f =  self.open_txt()
       if length is None:
           data = data[start:]
       else:
           data = data[start:start + length]
       f.write(data)
    #写入一个换行符
    def  newline(self):
        if self.__file is None:
            self.open_txt()
        self.__file.write("\n")
    # flush(self) :   强制写入
    def flush(self):
        if self.__file is not None:
            self.__file.flush()

    def close(self):
        if self.__file is not None:
            self.__file.close()
            self.__file = None
#
class FileOutputStream(OutFileDescriptor):

        def __init__(self,path,append= False):
            self._path = path
            self._append = append
            self.__file = None

        def open_file(self):
            if self._append:
                mode = "ab"
            else:
                mode = "wb"

            self.__file = open(self._path, mode)
            return self.__file
        def write(self,data :str,start =0,length: int =  None):
            f = self.open_file()
            if length is None:
                data = data[start:]
            else:
                data = data[start:start + length]
            if isinstance(data, str):
                data = data.encode()
            f.write(data)
        def flush(self):
            if self.__file is not None:
                self.__file.flush()
        def close(self):
            if self.__file is not None:
                self.__file.close()
                self.__file = None
if __name__ == "__main__":
    test = FileWriter("./test.txt",append =True)
    test.write(
        "heshichangying",
        length=10
    )
    test.newline()
    test.flush()
    test.close()


    test1 = FileOutputStream("./test2.txt")
    test1.write(
        "徒步的骑手，youtube我最喜欢的博客",
        length=12
    )
    test1.flush()
    test1.close()