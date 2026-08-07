"""
【静态方法】编写一个类 ListUtils , 并提供如下 静态方法，完成对应的代码编写
"""

from typing import List, Any, Callable


class ListUtils:
    """
    列表工具类
    """

    @staticmethod
    def filter(array: List[Any], predicate: Callable[[Any, int], bool]) -> List[Any]:
        """
        过滤 并获取满足条件的所有数据、并返回一个新列表对象
        """
        return [item for i, item in enumerate(array) if predicate(item, i)]

    @staticmethod
    def map(array: List[Any], functional: Callable[[Any, int], Any]) -> List[Any]:
        """
        将 列表 中的 数据 按照 指定的规则 映射为 新的数据、并返回 新的列表对象
        """
        return [functional(item, i) for i, item in enumerate(array)]

    @staticmethod
    def find(array: List[Any], predicate: Callable[[Any, int], bool]) -> Any:
        """
        查找 列表中 第一个满足 条件的 数据, 找不到 返回 None
        """
        for i, item in enumerate(array):
            if predicate(item, i):
                return item
        return None

    @staticmethod
    def index(array: List[Any], predicate: Callable[[Any, int], bool]) -> int:
        """
        查找 列表中 第一个满足 条件的 数据 索引，如果找不到 返回 -1
        """
        for i, item in enumerate(array):
            if predicate(item, i):
                return i
        return -1

    @classmethod
    def flat(cls, array: List[Any]) -> List[Any]:
        """
        对列表中的数据 进行扁平化处理、例如 [1, 2, [3,4, 5], [[6, 7], 8]] ===> [1, 2, 3, 4, 5, 6, 7, 8]
        """
        result = []
        for item in array:
            if isinstance(item, list):
                result.extend(cls.flat(item))
            else:
                result.append(item)
        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(ListUtils.filter(nums, lambda x, i: x % 2 == 0))
    print(ListUtils.map(nums, lambda x, i: x * 2))
    print(ListUtils.find(nums, lambda x, i: x > 3))
    print(ListUtils.index(nums, lambda x, i: x > 3))
    print(ListUtils.flat([1, 2, [3, 4, 5], [[6, 7], 8]]))
