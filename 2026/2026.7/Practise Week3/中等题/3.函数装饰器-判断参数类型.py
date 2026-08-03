#【装饰器】编写一个带参数的装饰器，用于检查传递给函数的参数类型是否正确。如果参数类型不正确，抛出异常。
#定义带参数的装饰器
def check_type(*types):
    """
    :param types: 接收参数的类型、列如(int，int)
    """
    #第二层函数、接收被装饰的函数
    def decorator(func):
        #第三层函数、接收真正传入的参数
        def wrapper(*args, **kwargs):
            #遍历参数和对应的类型
            for arg,expected_type in zip(args,types):
                #判断参数的类型是否正确
                if not isinstance(arg,expected_type):
                    raise TypeError(
                        f"参数{arg}类型错误，应为{expected_type.__name__}"
                    )
            #参数全部争取、执行圆函数
            return func(*args, **kwargs)
        #返回包装的函数
        return wrapper
    #返回装饰器
    return decorator

#使用装饰器
@check_type(int,int)
def add(a,b):
    return a+b

# 测试
print(add(10, 20))

print(add("10", 20))