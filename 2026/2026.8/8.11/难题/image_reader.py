"""
【责任链模式】图片读取器
读取顺序: GifImageReader -> PngImageReader -> JpegImageReader -> DefaultImageReader
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class AbstractImageReader(ABC):
    def __init__(self, path, next):
        self.__path = path
        self.__next = next

    @property
    def path(self):
        return self.__path

    def read(self):
        if self.issupport():
            self._read_file()
        else:
            if self.__next:
                self.__next.read()

    @abstractmethod
    def issupport(self) -> bool:
        """是否支持读取当前文件"""
        pass

    @abstractmethod
    def _read_file(self) -> None:
        """受保护方法：实际读取文件"""
        pass


class GifImageReader(AbstractImageReader):
    def issupport(self) -> bool:
        return self.path.lower().endswith(".gif")

    def _read_file(self) -> None:
        print(f"GifImageReader 正在读取: {self.path}")


class PngImageReader(AbstractImageReader):
    def issupport(self) -> bool:
        return self.path.lower().endswith(".png")

    def _read_file(self) -> None:
        print(f"PngImageReader 正在读取: {self.path}")


class JpegImageReader(AbstractImageReader):
    def issupport(self) -> bool:
        lower = self.path.lower()
        return lower.endswith(".jpg") or lower.endswith(".jpeg")

    def _read_file(self) -> None:
        print(f"JpegImageReader 正在读取: {self.path}")


class DefaultImageReader(AbstractImageReader):
    def issupport(self) -> bool:
        return True

    def _read_file(self) -> None:
        print(f"DefaultImageReader 正在读取未知格式文件: {self.path}")

class ImageReader:
    def __init__(self, path):
        default_reader = DefaultImageReader(path, None)
        jpeg_reader = JpegImageReader(path, default_reader)
        png_reader = PngImageReader(path, jpeg_reader)
        gif_reader = GifImageReader(path, png_reader)
        self.__reader = gif_reader

    def read(self):
        self.__reader.read()


if __name__ == "__main__":
    for file_path in [
        "demo.gif",
        "photo.png",
        "pic.jpg",
        "pic.jpeg",
        "data.bmp",
        "readme.txt",
    ]:
        print(f"--- {file_path} ---")
        ImageReader(file_path).read()
