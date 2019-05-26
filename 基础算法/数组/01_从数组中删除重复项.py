# -*- coding: utf-8 -*-
# @createTime    : 2019/5/26 9:58
# @author  : Huanglg
# @fileName: 01_从数组中删除重复项.py
# @email: luguang.huang@mabotech.com
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

注意: 排序数组

思路
数组完成排序后，我们可以放置两个指针 i 和 j，其中 i 是慢指针，而 j 是快指针。只要
     nums[i]=nums[j]，我们就增加 j 以跳过重复项
     当我们遇到 nums[j]≠nums[i] 时，跳过重复项的运行已经结束，因此我们必须把它（nums[j]）的值复
     制到 nums[i+1]。然后递增 i，接着我们将再次重复相同的过程，直到 j 到达数组的末尾为止。
"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if (nums[i] != nums[j]):
                i += 1
                nums[i] = nums[j]

        return i + 1

if __name__ == '__main__':
    soultion = Solution()
    res = soultion.removeDuplicates([1,1,2])
    print(res)
