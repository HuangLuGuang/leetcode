# -*- coding: utf-8 -*-
# @createTime    : 2019/6/1 20:40
# @author  : Huanglg
# @fileName: 4_验证回文字符串.py
# @email: luguang.huang@mabotech.com
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

# # 1
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         import re
#         s = re.sub('[^0-9a-zA-Z]+', '', s)
#         if len(s)  == 0:
#             return True
#         right = 0
#         left = len(s) -1
#         while right != left:
#             if s[right].lower() != s[left].lower():
#                 return False
#             right += 1
#             left -= 1
#             if right == len(s) / 2 + 1:
#                 break
#         return True

# 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter(str.isalnum, s)
        s = "".join(s).lower()
        return s == s[::-1]

if __name__ == '__main__':
    S = Solution()
    res = S.isPalindrome("aaaaaab")
    print(res)
