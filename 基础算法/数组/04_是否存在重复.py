# -*- coding: utf-8 -*-
# @createTime    : 2019/5/27 19:47
# @author  : Huanglg
# @fileName: 是否存在重复.py
# @email: luguang.huang@mabotech.com

"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""
# 1
class Solution:
    # over time
    def containsDuplicate(self, nums: list) -> bool:
        for item in nums:
            if (nums.count(item)) >= 2:
                return True
        return False
# 2
class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        set1 = set(nums)
        if (len(set1) == len(nums)):
            return False
        return True

# 3
class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        dict1 = {}
        for i in nums:
            # 每找到一次加一
            dict1[i] = dict1.get(i, 0) + 1
            if dict1[i] == 2:
                return True
        return False

