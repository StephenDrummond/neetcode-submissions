class Node:
    def __init__(self, val=-1, key=-1, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0
        self.head = Node()
        self.cur = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.push(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.cache[key].val = value
            self.remove(node)
            self.push(node)
        else:
            node = Node(val=value, key=key)
            self.cache[key] = node
            self.push(node)
            self.count += 1
            if self.count > self.capacity:
                del self.cache[self.head.next.key]
                self.remove(self.head.next)
    
    def remove(self, node):
        if node is self.cur:
            self.cur = node.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def push(self, node):
        self.cur.next = node
        node.prev = self.cur
        node.next = None
        self.cur = node
