"""
类型 标注:

    可以 在 定义函数 / 变量 的时候 进行一个 类型约束 、让 调用者 能够 直观 了解 需要传入的数据 类型

    也可以 让 编辑器 更智能的 推到 数据的类型 和 常见的代码 提示


函数的参数 可以 添加 类型 标注、 返回值 也可以 添加 类型标注

    a)  普通类型标注

            直接在 需要添加 标注 的位置 添加 对应的 真实数据类型

    b)  容器 类型标准 list, set, tuple, dict

            如果 想要 限定 容器中的数据类型，那么 需要 使用  typing 模块下的对应类

            List[int]  :  限定 列表中所有的元素 应该是 int 类型
            List[Any]  :  限定 列表中所有的元素 类型 不限

            Tuple[int] :  限定 元组中 有且 只有 1个元素、且 类型是 int
            Tuple[int, str] : 限定 元组中 有且 只有 2个元素、且 第一个类型是 int， 第二个是 str
            Tuple[int, ...] :  限定 元组中所有的元素 应该是 int 类型

            Set[int] :  限定 集合中 所有的元素 应该是 int 类型

            Dict[str, Any] :  限定 字典中的 键类型为 字符串， 值类型为 任意


    3)  可迭代对象 类型 标注
            Iterable[Any] :  限定类型是 可迭代对象

    4)  可调用对象 类型标注
            Callable[[int, str], Any] :  函数 需要 2个参数 第一个为 int, 第二个 字符串类型、且 函数返回值 任意

    5)  可选 类型标注



"""
from typing import List, Set, Tuple, Dict , Any


def test(ls: Set[int]) -> int:
    return sum(ls)


test({1, 2})

test({1, 2, 3, 4})

test((1.2, 2.3, 3))
test(("xyz", "zzz", "ttt", 3))
