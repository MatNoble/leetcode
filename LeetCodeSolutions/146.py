#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def move_node_to_tail(self, key):
        node = self.hashMap[key]
        # 断
        # prev  -- x -- > node <-- x -- next
        node.prev.next = node.next
        node.next.prev = node.prev
        # 连
        # prev <-- node --> tail
        node.next = self.tail
        node.prev = self.tail.prev
        # prev --> node <-- tail
        node.prev.next = node
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.move_node_to_tail(key)
            return self.hashMap[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].val = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashMap) == self.capacity:
                self.hashMap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new = ListNode(key, value)
            self.hashMap[key] = new
            # prev <-- new --> tail
            new.prev = self.tail.prev
            new.next = self.tail
            # prev --> new <-- tail
            new.prev.next = new
            self.tail.prev = new



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
