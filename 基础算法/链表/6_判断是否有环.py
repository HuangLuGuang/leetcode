# -*- coding: utf-8 -*-
# @createTime    : 2019/6/14 14:31
# @author  : Huanglg
# @fileName: 6_判断是否有环.py
# @email: luguang.huang@mabotech.com

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         temp = set()
#         while head:
#             if head in temp:
#                 return True
#             temp.add(head)
#             head=head.next
#         return False
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = 'huanglg'
        while head:
            if head.val == temp:
                return True
            else:
                head.val = temp
                head = head.next
        return False
