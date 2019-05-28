# -*- coding: utf-8 -*-
# @createTime    : 2019/5/28 16:45
# @author  : Huanglg
# @fileName: 9_两数之和.py
# @email: luguang.huang@mabotech.com
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""

# 暴力超时
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        arrlen = len(nums)
        for i in range(arrlen):
            for j in range(1, arrlen):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]

# 字典
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dict1 = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in dict1:
                return [dict1.get(another_num), index]
            dict1[num] = index




if __name__ == '__main__':
    s = Solution()
    res = s.twoSum([2, 7, 11, 15], 9)
    print(res)
