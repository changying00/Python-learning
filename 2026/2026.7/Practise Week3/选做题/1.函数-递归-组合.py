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
def split_number(n):
    # 用集合去重，因为不同递归路径可能得到相同组合
    result = set()
    def dfs(num):
        """
        返回 num 的所有拆分方式
        每一种拆分都是一个元组(tuple)
        """
        # ---------- 递归结束 ----------
        # 0没有拆分
        if num == 0:
            return [()]
        ans = []
        # 枚举
        # num = i + (num-i)
        for i in range(1, num + 1):
            # 求剩余数字所有拆法
            rest = dfs(num - i)
            # 将 i 放进去
            for item in rest:
                # 排序以后避免
                # (5,1)
                # (1,5)
                # 被认为不同
                temp = tuple(sorted((i,) + item))
                ans.append(temp)
        return ans
    # 去重
    for item in dfs(n):
        result.add(item)
    # 按长度、字典序排序
    return sorted(result, key=lambda x: (len(x), x))
print(split_number(6))