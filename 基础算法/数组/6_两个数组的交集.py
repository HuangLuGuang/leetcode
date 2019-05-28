# -*- coding: utf-8 -*-
# @createTime    : 2019/5/27 20:44
# @author  : Huanglg
# @fileName: 6_两个数组的交集.py
# @email: luguang.huang@mabotech.com
"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
"""
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        res = []
        temp = set(nums1) & set(nums2)
        for i in temp:
            res.extend([i] * min(nums2.count(i), nums1.count(i)))
        return res


# 2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == [] or nums2 == []:
            return []
        count_dict = {}
        for i in nums1:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        result_list = []
        for i in nums2:
            if i in count_dict and count_dict[i] > 0:
                result_list.append(i)
                count_dict[i] -= 1

        return result_list

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res = s.intersect(nums1, nums2)
    print(res)
