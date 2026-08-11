"""
【责任链模式】编写一个抽象类 AbstractImageReader ，接收path, next 两个必传参数，
def __init__(self,  path, next):
	self.__path = path   # 私有属性 , 提供 只读 property 属性
	self.__next = next  # 私有属性

def  read(self) :
	# 如果 当前类支持读取、则 调用 read_file 读取文件
	if  self.issupport():
		self._read_file()
	else:
		# 如果不支持读取、使用下一个类 读取文件
		if self.__next:
		      self.__next.read()

path 代表 读取文件的路径
next 代表 当前类无法读取后的 下一个读取文件的 AbstractImageReader 子类对象

并提供 两个抽象方法
（1）、issupport() :  是否支持 读取， 返回 bool ，
（2）、_read_file()  :  受保护的方法、读取文件中数据的方法，外部调用 read 负责读取

编写一个子类 GifImageReader 、只能用来读取 .gif 后缀的 文件, read_file()   方法可以做简单打印即可
编写一个子类 PngImageReader、只能用来读取 .png 后缀的图片，read_file()   方法可以做简单打印即可
编写一个子类 JpegImageReader、用来读取 .jpg 或者 .jpeg 后缀的图片，read_file()  方法可以做简单打印即可
编写一个子类 DefaultImageReader、 用来读取 未知格式的 文件

编写一个类 ImageReader, 该类 需要唯一一个参数 path 。 提供read 方法  可以读取任何文件

读取规则如下：
GifImageReader ---> PngImageReader  --->  JpegImageReader --->  DefaultImageReader
先尝试用 GifImageReader 读取 ，如果不能读取，使用 PngImageReader 读取，依次类推。
"""
from abc import ABC, abstractmethod
class AbstractImageReader(ABC):
    def __init__(self,path,next):
        self.__path = path #私有属性、提供 只读property属性
        self.__next = next #私有属性

    def read(self):
        #如果 当前类支持 读取、 则调用read_file读取文件
        if self.issupport():
            self._read_file()
        else:
            #如果不支持读取、使用下一个类读取文件
            if self._next:
                self._next.read()
    @abstractmethod
    def issupport(self):
        pass
    @abstractmethod
    def _read_file(self):
        pass

#编写一个子类
class GifImageReader(AbstractImageReader):
    def __init__(self,path):
        super().__init__(path)

    def issupport(self):
        

class PngImageReader(AbstractImageReader):
class JpegImageReader(AbstractImageReader):

class DefaultImageReader(AbstractImageReader):