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
        res = ListNode(0)
        tempres = res
        flag = 0
        carry = 0
        while l1 != None and l2 != None:
            if flag == 0:
                temp = l1.val + l2.val
                res.val = temp % 10
                carry = int(temp / 10)
                flag += 1
            else:
                temp = l1.val + l2.val + carry
                tempres.next = ListNode(temp % 10)
                tempres = tempres.next
                carry = int(temp / 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp = l1.val + carry
            tempres.next = ListNode(temp % 10)
            tempres = tempres.next
            carry = int(temp / 10)
            l1 = l1.next
        while l2:
            temp = l2.val + carry
            tempres.next = ListNode(temp % 10)
            tempres = tempres.next
            carry = int(temp / 10)
            l2 = l2.next
        if carry != 0:
            tempres.next = ListNode(1)
        return res

# mat = Solution()


