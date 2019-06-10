# -*- coding: utf-8 -*-
# @createTime    : 2019/6/10 20:08
# @author  : Huanglg
# @fileName: 2_删除倒数第n个节点.py
# @email: luguang.huang@mabotech.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lengh = 0
        temp = head
        while temp:
            lengh += 1
            temp = temp.next
        if lengh == 1:
            return []
        index = 0
        target = lengh - n
        temp = head
        while temp:
            index += 1
            if index == target:
                temp.next = temp.next.next
            temp = temp.next

        return head

if __name__ == '__main__':
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)
    head = ListNode(0)
    head.next = node1
    node1.next = node2
    node2.next = node3

    s = Solution()
    s.removeNthFromEnd(head, 1)
