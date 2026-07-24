"""
带参数的装饰器
    需要 三层 嵌套 构建一个 闭包

        a) 最外层函数 定义 装饰器 需要的参数
        b) 第二层函数 定义 要装饰器的 目标函数
        c) 第三层函数 定义 目标函数需要的参数列表 且 处理 增强逻辑



定义一个装饰器、用来 检查 函数参数 类型 是否 合法 、如果 不合法、则 抛出错误


"""

def check_type(*, types=(), kwtypes={}):
    def check_type_target(func):
        def wrapper(*args, **kwargs):
            # 判断 types 是否为 空 、如果 不为空，则检查 对应的位置 参数类型
            if len(types) == 0 and len(args) > 0:
                raise Exception("需要使用 types 限定 位置参数的类型")

            if len(kwtypes) == 0 and len(kwargs) > 0:
                raise Exception("需要使用 kwtypes 限定 关键字参数的类型")

            if len(types) != len(args):
                raise Exception(f"types 限定 位置参数的类型数据 不匹配 传入的 参数格式, 期待传入 {len(types)} 个、实际传入 {len(args)}个")

            # 校验类型
            for t, v in zip(types, args):
                if t != type(v):
                    raise Exception(f"位置参数 {v} 类型不正确、期待 {t.__name__} 类型、实际为 {type(v).__name__}")

            # 检查 关键字类型
            for key, t in kwtypes:
                if t != type(kwargs.get(key)):
                    raise Exception(f"关键字参数 {key} 类型比正确、期待 {t.__name__} 类型、实际为 {type(kwargs.get(key)).__name__}")

            # 如果 符合要求、则调用 目标函数
            return func(*args, **kwargs)

        return wrapper
    return check_type_target


@check_type(types=(int, int))
def sum(a: int, b: int) -> int:
    return a + b


print(sum(1, "2"))