class Listnode():
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = Listnode()

    def append(self, val):
        new_node = Listnode(val)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        sum = 0
        while cur.next != None:
            sum += 1
            cur = cur.next
        return sum

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.val)
        print(elems)

mat = LinkedList()
mat.display()
mat.append(1)
mat.append(2)
print(mat.length())
mat.display()
