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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 前后指针
        frontNode = head
        behindNode = head
        length = 0

        # 前指针先走n步
        for i in range(n):
            frontNode = frontNode.next
            length += 1

        # 代表要删除的是第一个元素
        if frontNode == None:
            return head.next

        # 前后指针同时走
        while (frontNode.next):
            frontNode = frontNode.next
            behindNode = behindNode.next
            length += 1

        # 删除元素
        behindNode.next = behindNode.next.next
        return head





class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 链表长度
        length = 0
        currentNode = head
        # 遍历一次，得出链表长度
        while (currentNode):
            length += 1
            currentNode = currentNode.next

        # 算出要删除元素的位置（从0开始计算）
        index = length - n
        currentNode = head

        # 如果要删除的是第一个元素
        if index == 0:
            return currentNode.next

        # 删除元素
        for i in range(length):
            # 遍历到要删除元素的前一个元素
            if i == index - 1:
                currentNode.next = currentNode.next.next
                return head
            else:
                # 继续遍历
                currentNode = currentNode.next



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




