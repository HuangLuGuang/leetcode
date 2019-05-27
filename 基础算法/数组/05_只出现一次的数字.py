# -*- coding: utf-8 -*-
# @createTime    : 2019/5/27 20:17
# @author  : Huanglg
# @fileName: 05_只出现一次的数字.py
# @email: luguang.huang@mabotech.com

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗
"""
class Solution:
    def singleNumber(self, nums: list) -> int:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1

        for k, v in dict1.items():
            if v == 1:
                return k


# 2
"""
思路：根据异或运算的特点，相同的数字经过异或运算后结果为0，
除单独出现一次的数字外，其他数字都是出现两次的，那么这些数字经过异或运算后结果一定是0。
而任何数字与0进行异或运算都是该数字本身。
所以对数组所有元素进行异或运算，运算结果就是题目的答案。
"""

class Solution:
    def singleNumber(self, nums: list) -> int:
        num = 0
        for i in nums:
            num = num ^ i
        return num


if __name__ == '__main__':
    s = Solution()
    res = s.singleNumber([4,1,2,1,2])
    print(res)
