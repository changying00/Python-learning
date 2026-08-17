from abc import ABC, abstractmethod


class InFileDescriptor(ABC):

    @abstractmethod
    def read(self, n=1):
        """读取指定的长度内容"""
        pass

    @abstractmethod
    def readall(self):
        """一次性读取所有数据、适用于小文件的读取"""
        pass

    @abstractmethod
    def close(self):
        """关闭通道"""
        pass

    def chunk(self, chunk_size=None):
        """一次读取指定的长度、返回一个生成器、适用于大文件的读取"""
        if chunk_size is None:
            # 设置 默认读取的块的大小 8kb
            chunk_size = 8 << 10

        while len(chunk_data := self.read(chunk_size)) != 0:
            yield chunk_data


class FileReadMixins:

    def read(self, n=1):
        return self.pipeline.read(n)

    def readall(self):
        return self.pipeline.read()

    def close(self):
        return self.pipeline.close()


class FileReader(FileReadMixins, InFileDescriptor):

    def __init__(self, path, *, encoding="utf-8"):
        # 创建一个读取文件的管道对象
        self.__pipeline = open(path, "rt", encoding=encoding)

    @property
    def pipeline(self):
        return self.__pipeline

    def readline(self):
        return self.__pipeline.readline()

    def readlines(self):
        return self.__pipeline.readlines()


class FileInputStream(FileReadMixins, InFileDescriptor):

    def __init__(self, path):
        self.__pipeline = open(path, "rb")

    @property
    def pipeline(self):
        return self.__pipeline


if __name__ == "__main__":
    # 创建 一个专门用来读取 字符文件的 流
    # reader = FileReader("./第八章 常见模块/1.数学math模块.py")

    # 一次读取一行
    # for chunk in reader.chunk():
    #     print(chunk, end="")
    # reader.close()

    inputstream = FileInputStream("./第八章 常见模块/1.数学math模块.py")

    print(inputstream.readall())

    inputstream()

