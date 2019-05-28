# -*- coding: utf-8 -*-
# @createTime    : 2019/5/28 15:54
# @author  : Huanglg
# @fileName: 8_移动0.py
# @email: luguang.huang@mabotech.com
class Solution:
    """
    300ms
    """
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            temp = nums[i]
            if temp == 0:
                nums.remove(temp)
                nums.append(temp)

#2
class Solution:
    def moveZeroes(self, nums: list) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        for i in range(index, len(nums)):
            nums[i] = 0

if __name__ == '__main__':
    nums = [0,0,1,0,3,5,0,2]
    nums.sort(key=bool, reverse=True)
    # s = Solution()
    # s.moveZeroes(nums)
    print(nums)
