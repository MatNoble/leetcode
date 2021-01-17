import sys
sys.path.append('./Data Structures and Algorithms')
from LinkedLists import *

def reverse(head, b):
    pre, cur, nxt = None, head, head
    while cur != b:
        nxt, cur.next = cur.next, pre
        pre, cur = cur, nxt
    return pre

def reverseKGroup(head, k):
    if not head: return None
    a, b = head, head
    for i in range(k):
        if not b: return head
        b = b.next
    newHead = reverse(a, b)
    a.next = reverseKGroup(b, k)
    return newHead

def reverse_recursion(head):
    if not head or not head.next: return head
    last = reverse_recursion(head.next)
    head.next.next = head
    head.next = None
    return last

def reverseN(head, n):
    if n == 1: return head
    last = reverseN(head.next, n-1)
    succesor = head.next.next
    head.next.next = head
    head.next = succesor
    return last

def reverseMN(head, m, n):
    if m == 1: return reverseN(head, n)
    head.next = reverseMN(head.next, m-1, n-1)
    return head

mat = LinkedList()
for i in range(5):
    mat.append(i)
mat.display()

head = mat.head.next
# p = reverse(head)
# p = reverse_recursion(head)
# p = reverseN(head, 3)
# p = reverseMN(head, 2, 3)
p = reverseKGroup(head, 3)

nums = []
while p:
    nums.append(p.val)
    p = p.next
print(nums)
