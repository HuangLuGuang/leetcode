# -*- coding: utf-8 -*-
# @createTime    : 2019/6/6 20:44
# @author  : Huanglg
# @fileName: 1_删除节点.py
# @email: luguang.huang@mabotech.com
"""
删除链表中的节点
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:
Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

def print_node(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)
    head = ListNode(0)
    head.next = node1
    node1.next = node2
    node2.next = node3
    print_node(head)
    s = Solution()
    s.deleteNode(node1)
    print("-" * 10)
    print_node(head)
