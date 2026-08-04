"""
给你一个整数数组 nums ，数组由若干 互不相同 的整数组成。

数组 nums 原本包含了某个范围内的 所有整数 。但现在，其中可能 缺失 部分整数。

该范围内的 最小 整数和 最大 整数仍然存在于 nums 中。

返回一个 有序 列表，包含该范围内缺失的所有整数，并 按从小到大排序。如果没有缺失的整数，返回一个 空 列表。
"""
from typing import List
def findMissingElements( nums: List[int]) -> List[int]:
        # nums1= sorted(nums)
        max_num, min_num = max(nums), min(nums)
        if (max_num - min_num ) + 1 == len(nums):
            return []
        ls = []
        while min_num <= max_num:
            if  min_num not in nums:
                ls.append(min_num)
            min_num += 1
        return ls
if __name__ =="__main__":
    print(findMissingElements([1,3,5]))
