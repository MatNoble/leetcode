#==================================================
#==>      Title: linked-list-cycle-ii
#==>     Author: Zhang zhen
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/23/2021
#==================================================

"""
https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        x = None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                x = slow
                break
        if x == None: return
        finder = head
        while finder != x: finder, x = finder.next, x.next
        return finder
