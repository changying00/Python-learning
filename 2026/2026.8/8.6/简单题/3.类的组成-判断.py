"""
【类的组成】编写一段代码，判断 某个对象 是否存在 指定的方法，如果 存在，则 获取该方法，否则 给对象添加一个方法，并返回 添加的 方法
"""
import types


def get_or_add_method(obj, method_name, default_func=None):
    """
    判断对象是否存在指定方法：
    - 存在：返回该方法
    - 不存在：给对象添加方法，并返回添加的方法
    :param obj: 目标对象
    :param method_name: 方法名（字符串）
    :param default_func: 不存在时要添加的默认函数（普通函数，会绑定到对象）
    :return: 方法对象
    """
    # 判断对象是否拥有指定名称的方法
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        # 确认是可调用的方法
        if callable(method):
            print(f"对象已存在方法: {method_name}")
            return method

    # 不存在则添加方法
    if default_func is None:
        # 默认添加一个空方法
        def default_func(self):
            print(f"这是动态添加的方法: {method_name}")

    # 将普通函数绑定为实例方法
    bound_method = types.MethodType(default_func, obj)
    setattr(obj, method_name, bound_method)
    print(f"对象不存在方法 {method_name}，已添加")
    return bound_method


# ========== 测试代码 ==========
class Student:
    """测试用学生类"""

    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} 正在学习")


def say_hello(self):
    """要动态添加的方法"""
    print(f"你好，我是 {self.name}")


if __name__ == "__main__":
    s = Student("张三")

    # 1. 获取已存在的方法
    method1 = get_or_add_method(s, "study")
    method1()  # 调用已存在的 study 方法

    # 2. 添加不存在的方法
    method2 = get_or_add_method(s, "say_hello", say_hello)
    method2()  # 调用新添加的 say_hello 方法

    # 3. 再次获取刚添加的方法（此时已存在）
    method3 = get_or_add_method(s, "say_hello")
    method3()
