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
    def open_txt(self):
        if self.append == True:

            self.append = "at"
        else:
            self.append = 'wt'
        f = open(self.path,self.append,self.encoding)
        return f
    #写入指定长度的内容
    def write(self, data: Union[str, bytes] , start: int = 0, length: int = None):
       f =   self.open_txt()
       f.write(data)