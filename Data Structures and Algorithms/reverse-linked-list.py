import sys
sys.path.append('./Data Structures and Algorithms')
from LinkedLists import *

def reverse(head):
    if not head or not head.next: return head
    last = reverse(head.next)
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

# p = reverse(mat.head.next)
# p = reverseN(mat.head.next, 3)
p = reverseMN(mat.head.next, 2, 3)

nums = []
while p:
    nums.append(p.val)
    p = p.next
print(nums)
