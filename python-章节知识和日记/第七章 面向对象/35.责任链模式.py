"""
 编写一段代码， 根据 图片的后缀 ，使用 不同的方式 进行图片的读取

"""
from abc import ABC, abstractmethod
import re


class AbstractImageReader(ABC):

    def __init__(self, path, reader=None):
        # 将 传入 的 reader 作为 下一个要读取图片的类
        self.__next = reader
        self.__path = path

    @property
    def path(self):
        return self.__path

    @abstractmethod
    def is_support(self) -> bool:
        """是否支持读取图片"""
        pass

    @abstractmethod
    def _read(self):
        """读取图片内容"""
        pass

    def read(self):
        """负责读取图片"""
        if self.is_support():
            # 读取图片内容
            return self._read()

        # 如果 不支持读取、则委托下一个 ImageReader 读取
        if self.__next is not None:
            return self.__next.read()


class JpegImageReader(AbstractImageReader):
    """专门用来读取 Jpeg 图片的类"""

    regex = r"\.jpe?g$"

    def is_support(self) -> bool:
        return bool(re.search(self.regex, self.path, re.I))

    def _read(self):
        print("正在读取 jpg 图片.....")


class GifImageReader(AbstractImageReader):
    """专门用来读取 gif 图片的类"""

    regex = r"\.gif$"

    def is_support(self) -> bool:
        return bool(re.search(self.regex, self.path, re.I))

    def _read(self):
        print("正在读取 gif 图片.....")


class PngImageReader(AbstractImageReader):
    """专门用来读取 png 图片的类"""

    regex = r"\.png$"

    def is_support(self) -> bool:
        return bool(re.search(self.regex, self.path, re.I))

    def _read(self):
        print("正在读取 png 图片.....")


class DefaultImageReader(AbstractImageReader):
    """专门用来读取 未知格式 图片的类"""

    def is_support(self) -> bool:
        return True

    def _read(self):
        print("正在读取 未知格式 图片.....")


class ImageReader:
    """将 读取图片的类 进行 组装、形成链、并提供读取图片的能力"""

    def __init__(self, path):
        # 创建 DefaultImageReader 对象
        default_reader = DefaultImageReader(path)
        # 创建 JpegImageReader
        jpeg_reader = JpegImageReader(path, default_reader)
        # 创建 PngImageReader
        png_reader = PngImageReader(path, jpeg_reader)
        # 创建一个 GifReader、并作为 链的头部 做成 当前类的属性
        self.__image_reader = GifImageReader(path, png_reader)

    def read(self):
        return self.__image_reader.read()


if __name__ == "__main__":
    path = "D:/abc/xxx.bmp"

    reader = ImageReader(path)
    reader.read()