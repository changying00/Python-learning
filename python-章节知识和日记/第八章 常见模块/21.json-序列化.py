"""
JSON :
    是一种 轻量级的数据传输格式 、可以 用来 存储、数据传输 。 这种格式 人可以很好的理解、机器 也能非常便捷的进行解析

    是一个 跨语言的 数据格式 、几乎 所有主流的 编程语言 都支持 该数据格式


JSON 支持的数据类型

    字符串、 数字、 布尔、 null 、 {} ,  []


JSON 和 Python 的关系

    JSON                             Python

字符串（只能用双引号）                 字符串

数字                                 int / float

true / false                        True / False

null                                 None

{}                                   字典

[]                                   列表

NaN                                  float("nan")

Infinity                             float("inf")

-Infinity                            float("-inf")

==============================================================

JSON 支持的数据格式 主要 有 2 种

第一种 :  {}

第二种 :  []

==============================================================

JSON 的 序列化 :

    将 python 内存种的 列表/字典 转成 JSON 格式的 字符串


实现 JSON 的序列化 操作

json.dumps(obj, *, skipkeys=False, ensure_ascii=True,
        allow_nan=True, cls=None, indent=None,
        default=None) :


    obj : 要序列化的 字典/列表 等对象

    ensure_ascii : 是否 将 超出 ascii 范围的 字符 以 unicode 编码 表示

    skipkeys:  是否 允许 跳过 无法 进行序列化的 键

    allow_nan :  允许 非数、无穷

    indent : 设置 缩进的 数量 、以 更加优雅的方式 展示 JSON格式的 字符串

    default :  处理 无法 序列化的数据 、例如 日期

        default 它的值 是一个 功能型函数、 消费 1个 无法序列化的数据 、返回 处理后的数据

        通常 临时性 解决某个值 无法序列化的问题

    cls :  处理 无法 序列化的数据 、例如 日期

        cls 它的值 是一个类型 、且该类型 必须 继承 JSONEncoder 、 并重写 父类中的 default 方法

        通常 永久性 解决 某些 类型 无法序列化的问题


"""
import json
from datetime import date, datetime, timedelta


class QikuJSONEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")

        if isinstance(o, date):
            return o.strftime("%Y-%m-%d")

        if isinstance(o, timedelta):
            return o.total_seconds()

        if hasattr(o, "__dict__"):
            return o.__dict__

        return str(o)


class Dog:
    def __init__(self, name):
        self.name = name


ls = [1, 2, 3, 4, 5, True, False, None, 'hello']

# 对 列表 进行 JSON 序列化，并返回 序列化后的 JSON 字符串
ret = json.dumps(ls)

print(ret)

# 定义 一个字典
dct = {
    "name": "张三",
    "birth": date(2000, 10, 10),
    "gender": "男",
    (1, 2): 100,
    "test": (1, 2, 3),
    "createAt": datetime.now(),
    "duration": timedelta(days=2),
    "dog": Dog("小黑")
}

# 将一个 字典 进行 JSON 序列化
print(json.dumps(dct, ensure_ascii=False, skipkeys=True, indent=4, cls=QikuJSONEncoder))
