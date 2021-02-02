#==================================================
#==>      Title: reverse-linked-list
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/11/2021
#==================================================

"""
https://leetcode-cn.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseListR(self, head: ListNode) -> ListNode:
        if not head or head.next == None: return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
    
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
