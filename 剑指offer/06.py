#==================================================
#==>      Title: 剑指 Offer 06. 从尾到头打印链表
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/28/2021
#==================================================

"""
https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None: return []
        return self.reversePrint(head.next) + [head.val]
