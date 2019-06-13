# -*- coding: utf-8 -*-
# @createTime    : 2019/6/13 20:04
# @author  : Huanglg
# @fileName: 4_合并两个有序链表.py
# @email: luguang.huang@mabotech.com
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return l1
        temp = []
        while l1:
            val = l1.val
            temp.append(val)
            l1 = l1.next
        while l2:
            val = l2.val
            temp.append(val)
            l2 = l2.next
        temp.sort()
        newhead = ListNode
        t = newhead
        for val in temp:
            t.next = ListNode(val)
            t = t.next
        return newhead.next
