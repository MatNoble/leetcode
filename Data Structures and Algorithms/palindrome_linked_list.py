import sys
sys.path.append('./Data Structures and Algorithms')
from LinkedLists import *

def printLinkedList(head):
    if head == None: return
    printLinkedList(head.next)
    print(head.val)

def isPalindrome(head):
    def traverse(left, right):
        if not right: return True
        res = traverse(left.next, right.next)
        res = res and (left.val == right.val)
        return res
    traverse(head, head)


mat = LinkedList()
for i in range(5):
    mat.append(i)
# mat.display()

# printLinkedList(mat.head.next)

print(isPalindrome(mat.head.next))
