#【装饰器】编写一个装饰器 repeat(n = 1)、能够让函数执行 n 次
#定义一个带参数的装饰器
def repeat(n):
    #接收被装饰的函数
    def decorator(func):
        #包装函数、接收原函数的参数
        def wrapper(*args, **kwargs):
            #保存函数的返回结果
            result =  None
            for i in range(n):
                print(f"循环{i + 1}次")
                #调用原函数
                result  = func(*args, **kwargs)
            return result

        return wrapper

    return decorator

@repeat(n = 3)
def add(a,b):
    print("执行add函数")
    return a+b

if __name__ == '__main__':
    print(add(1,2))