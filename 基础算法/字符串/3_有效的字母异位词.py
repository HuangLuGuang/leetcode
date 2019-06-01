# -*- coding: utf-8 -*-
# @createTime    : 2019/6/1 20:30
# @author  : Huanglg
# @fileName: 3_有效的字母异位词.py
# @email: luguang.huang@mabotech.com
"""Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    S = Solution()
    res = S.isAnagram(s, t)
    print(res)

