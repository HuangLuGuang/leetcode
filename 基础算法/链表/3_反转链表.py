# -*- coding: utf-8 -*-
# @createTime    : 2019/6/11 22:37
# @author  : Huanglg
# @fileName: 3_反转链表.py
# @email: luguang.huang@mabotech.com

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        newhead = ListNode
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        temp = newhead
        for i in range(len(nums)-1, -1, -1):
            temp.next = ListNode(nums[i])
            temp = temp.next
        return newhead.next
