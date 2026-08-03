import time
import random
def record_time(func):
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result
    return wrapper
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

download = record_time(download) #调用 record_time(download)，进入装饰器内部，创建 wrapper 函数，然后 record_time 返回这个 wrapper，最后把返回值赋值给 download。
upload = record_time(upload)
download('MySQL从删库到跑路.avi')#相当于wrapper("MySQL从删库到跑路.avi")
upload('Python从入门到住院.pdf')

"""
所以三种写法其实是同一个东西
方法1：手动装饰
upload = record_time(upload)
upload(...)
方法2：@语法糖（推荐）
@record_time
def upload():
    ...
upload(...)
方法3：临时调用
record_time(upload)('文件名')
意思：
先装饰 upload，再立即调用。
"""