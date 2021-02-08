#==================================================
#==>      Title: 24. 两两交换链表中的节点
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/8/2021
#==================================================

"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:  
        if not (head and head.next): 
            return head
        res = ListNode()
        pre = res
        pre.next = head
        while pre.next and pre.next.next:
            former, latter = pre.next, pre.next.next
            pre.next, former.next = latter, latter.next
            latter.next = former
            pre = former
        return res.next
