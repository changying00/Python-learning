"""
装饰器】编写一个装饰器 检查函数关键字参数 check_keyword_params(*, key, val)。
 例如 @check_keyword_params(key="logo", val="qiku")
  则检查函数调用的时候是否传了一个关键参数 logo，
值为 qiku。 如果 没有该参数、则不允许调用函数 。
"""
# 定义带参数的装饰器
def check_keyword_params(*, key, val):
    """
    检查函数调用时是否包含指定关键字参数
    :param key: 检查的参数名
    :param val: 参数必须对应的值
    """
    # 接收被装饰的函数
    def decorator(func):
        # 包装函数
        def wrapper(*args, **kwargs):
            # 判断关键字参数是否存在，并且值是否正确
            if key not in kwargs or kwargs[key] != val:
                # 不满足条件，不允许调用原函数
                raise ValueError(
                    f"必须传入关键参数 {key}={val}"
                )
            # 条件满足，执行原函数
            return func(*args, **kwargs)
        return wrapper
    return decorator
# 使用装饰器
@check_keyword_params(key="logo", val="qiku")
def show_info(name):
    print("执行函数")
    print(name)
# 正确调用
show_info(
    name="Python",
    logo="qiku"
)