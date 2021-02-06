#==================================================
#==>      Title: Leetcode-002-add-two-numbers                                   
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/6/2021
#==================================================

'''
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

======================================================
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
======================================================

链接： https://leetcode-cn.com/problems/add-two-numbers/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = l1.val + l2.val
        count = temp // 10
        res = ListNode(temp % 10)
        cur = res
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
            temp = l1.val + l2.val + count
            count = temp // 10
            cur.next = ListNode(temp % 10)
            cur = cur.next
        while l1.next:
            l1 = l1.next
            temp = l1.val + count
            count = temp // 10
            cur.next = ListNode(temp % 10)
            cur = cur.next
        while l2.next:
            l2 = l2.next
            temp = l2.val + count
            count = temp // 10
            cur.next = ListNode(temp % 10)
            cur = cur.next
        if count: cur.next = ListNode(count)
        return res

"""
时间复杂度：$O(max(m, n)$ # m, n 分别 l1 和 l2 的长度
空间复杂度：$O(max(m, n))$ 
"""
