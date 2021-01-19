import sys
sys.path.append('./Data Structures and Algorithms')
from LinkedLists import *

def printLinkedList(head):
    if head == None: return
    printLinkedList(head.next)
    print(head.val)

def reverse(head):
    pre, cur = None, head
    while cur != None:
        next = cur.next
        cur.next, pre = pre, cur
        cur = next
    return pre

def isPalindrome(head):
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    if fast != None: slow = slow.next
    left, right = head, reverse(slow)
    while right != None:
        if left.val != right.val: return False
        left, right = left.next, right.next
    return True

mat = LinkedList()
# for i in range(5):
#     mat.append(i)
# mat.display()

mat.head = ListNode(3)
e1 = ListNode(3)
e2 = ListNode(3)
e3 = ListNode(4)
mat.head.next = e1
# e1.next = e2
# e2.next = None

current_node = mat.head
while current_node != None:
    print(current_node.val)
    current_node = current_node.next

isPalindrome(mat.head)
