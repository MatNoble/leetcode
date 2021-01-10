class ListNode():
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = ListNode()

    # Adds new node containing 'data' to the end of the linked list
    def append(self, val):
        new_node = ListNode(val)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    # Returns the length (integer) of the linked list
    def length(self):
        cur = self.head
        sum = 0
        while cur.next != None:
            sum += 1
            cur = cur.next
        return sum

    # Prints out the linked list in traditional Python list format
    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.val)
        print(elems)

    # Returns the value of the node at 'index'
    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR, 'Get' Index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.val
            cur_idx += 1

    # Deletes the node at index 'index'
    def erase(self, index):
        if index >= self.length() or index < 0:
            print("ERROR, 'Get' Index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    # Allows for bracket operator syntax (i.e. a[0] to return first item)
    def __getitem__(self,index):
        return self.get(index)

    # Inserts a new node at index 'index' containing data 'data'.
    # Indices begin at 0. If the provided index is greater than or 
    # equal to the length of the linked list the 'data' will be appended.
    def insert(self, index, value):
        if index >= self.length() or index < 0:
            return self.append(value)
        cur_idx = 0
        last_node, cur_node = self.head, self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                new_node = ListNode(value)
                last_node.next = new_node
                new_node.next = cur_node
                return
            last_node = cur_node
            cur_idx += 1

    def set_(self, index, value):
        if index >= self.length() or index < 0:
            print("ERROR, 'set' Index out of range")
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                cur_node.val = value
                return
            cur_idx += 1

mat = LinkedList()
mat.display()
# Adds new node containing 'data' to the end of the linked list
for i in range(5):
    mat.append(i*i)
mat.display()

# Returns the length (integer) of the linked list
print(f"the length of mat is: {mat.length()}\n")

# Returns the value of the node at 'index'
k = 2
print(f"the value of node which index equals {k} is {mat.get(k)}")
print(f"the value of node which index equals {k} is {mat[k]}\n")

# Deletes the node at index 'index'
mat.erase(k)
print(f"the LinkedList deleted the node which index euqals {k} is: ")
mat.display()

# insert
mat.insert(3, 100)
mat.display()

# set_
mat.set_(3, 200)
mat.display()
