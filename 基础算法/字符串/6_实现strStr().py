# -*- coding: utf-8 -*-
# @createTime    : 2019/6/5 22:51
# @author  : Huanglg
# @fileName: 6_实现strStr().py
# @email: luguang.huang@mabotech.com
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)  == 0:
            return 0
        return haystack.find(needle)

if __name__ == '__main__':
    s = Solution()
    res = s.strStr(haystack = "hello", needle = "ll")
    print(res)
