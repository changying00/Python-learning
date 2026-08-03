"""
【递归】编写一个函数、实现将一个数字进行拆分、并获取它的所有组合 例如 6 ===> [(1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 2), (1, 1, 1, 3), (1, 1, 2, 2), (1, 1, 4), (1, 2, 3), (1, 5), (2, 2, 2), (2, 4), (3, 3), (6,)]
递归思路：
要 拆分 6的 数字组合，则 满足如下规则

6  和 数字 0 的组合 [()] 进行 组合
5  和 数字 1 的所有组合 进行 组合
4  和 数字 2 的所有组合 进行 组合
3  和 数字 3 的所有组合 进行 组合
2  和 数字 4 的所有组合 进行组合
1  和 数字 5 的所有组合 进行组合
将 上述 所有的组合 放到 统一的容器中 就是 最终 6 拆分的 所有组合 (可能存在重复情况)
"""

from typing import List, Tuple


def get_num_combines(number: int) -> List[Tuple[int, ...]]:
    """
    获取 一个数字的 所有组合
    """
    if number == 0:
        return [()]
    # 定义一个 容器、用来存储最终的结果
    result = []
    # 遍历 从 number ~ 1
    for x in range(number, 0, -1):
        # 获取 另一个数字
        n = number - x
        # 获取 n 数字的所有组合情况
        temp = [tuple(sorted((*tp, x))) for tp in get_num_combines(n)]

        # 遍历 temp 、并 判断 temp 中的元素 是否在 result 中存在， 如果不存在，则添加
        for tp in temp:
            if tp not in result:
                result.append(tp)

    return sorted(result)


if __name__ == "__main__":

    s = get_num_combines(6)
    print(s)
