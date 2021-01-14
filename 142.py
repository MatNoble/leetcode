#==================================================
#==>      Title: linked-list-cycle-ii
#==>     Author: Zhang zhen
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/14/2021
#==================================================

"""
https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None: return
        slow, fast = head, head
        while True:
            if fast == None or fast.next == None: return
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        finder = head
        while finder != slow:
            finder, slow= finder.next, slow.next
        return finder
