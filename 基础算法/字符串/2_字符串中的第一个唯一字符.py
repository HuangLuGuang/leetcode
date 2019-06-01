# -*- coding: utf-8 -*-
# @createTime    : 2019/6/1 20:10
# @author  : Huanglg
# @fileName: 2_字符串中的第一个唯一字符.py
# @email: luguang.huang@mabotech.com
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

# time out limit
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#
#         for index, char in enumerate(s):
#             count = s.count(char)
#             if count == 1:
#                 return index
#         return -1

# 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for index, char in enumerate(s):
            count[char] = count.get(char, 0) + 1

        for k, v in count.items():
            if v == 1:
                return s.index(k)
        return -1

# 3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        l = []
        for x in abc:
            if s.find(x)!=-1 and s.find(x)==s.rfind(x):
                l.append(s.find(x))
        if len(l)!=0:
            return min(l)
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    res = s.firstUniqChar("loveleetcode")
    print(res)
