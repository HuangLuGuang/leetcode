# -*- coding: utf-8 -*-
# @createTime    : 2019/6/13 20:55
# @author  : Huanglg
# @fileName: 5_验证回文字符串.py
# @email: luguang.huang@mabotech.com
"""
回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = []
        while head:
            val = head.val
            s.append(val)
            head = head.next
        return s == s[::-1]
