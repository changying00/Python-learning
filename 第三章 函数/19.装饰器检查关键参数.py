"""
检查关键参数

装饰器 外部函数中的 代码  在初始化  每个目标函数 对象 的时候 都 会执行一次 。  内部 函数 在 每次调用 目标函数的时候 都会执行。

外部函数中 定义的非局部变量 被 同一个目标函数 共享数据 、不同目标函数间 数据独立

内部函数 中 定义的数据 是 独立的 ~~~

"""
import functools


def check_keyword_params(*, key, value):
    a = 10
    print("===========================outter=============================")

    def check_keyword(func):
        print("==============================outter2=====================")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("====================inner=======================")

            # 检查 关键参数
            if key not in kwargs:
                raise Exception(f"目标函数 {func.__name__} 在调用的时候 丢失了 关键参数 {key}")

            # 检查 关键参数 对应的 值 是否 相同
            if value != kwargs.get(key):
                raise Exception(f"目标函数 {func.__name__} 在调用的时候 关键参数 {key} 的值 不正确、期待值为 {value}")

            # 调用 目标函数、完成函数调用
            return func(*args, **kwargs)

        return wrapper

    return check_keyword


@check_keyword_params(key="logo", value="qiku")
def test(*, logo):
    print("logo")


@check_keyword_params(key="logo", value="qiku")
def sum():
    pass


if __name__ == "__main__":
    pass
    # test(logo="qiku")

    # test(logo="qiku")
