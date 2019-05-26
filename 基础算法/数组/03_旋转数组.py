# -*- coding: utf-8 -*-
# @createTime    : 2019/5/26 13:23
# @author  : Huanglg
# @fileName: 03_旋转数组.py
# @email: luguang.huang@mabotech.com

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
"""
class Solution:
    def rotate(self, nums: list, k: int) -> None:

        import copy
        temp = copy.deepcopy(nums)
        for i in range(len(nums)):
            if i - k < 0 :
                nums[i] = temp[i - k + len(nums)]
            else:
                nums[i] = temp[i - k]


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    solution.rotate(nums=nums, k=3)
    print(nums)


