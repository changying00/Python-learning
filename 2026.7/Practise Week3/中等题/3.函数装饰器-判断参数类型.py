#【装饰器】编写一个带参数的装饰器，用于检查传递给函数的参数类型是否正确。如果参数类型不正确，抛出异常。
#定义带参数的装饰器
from zipfile import ZIP_LZMA


def check_type(*type):
    """
    :param type: 接收参数的类型、列如(int，int)
    """
    #第二层函数、接收被装饰的函数
    def decorator(func):
        #第三层函数、接收真正传入的参数
        def wrapper(*args, **kwargs):
            #遍历参数和对应的类型
            for arg,expected_type in zip(args,types):