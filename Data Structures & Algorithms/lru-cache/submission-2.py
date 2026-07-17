class LRUCache:
    class Node:
        def __init__(self, key=-1, val=-1, last=None, next=None):
            self.key = key
            self.val = val
            self.last = last
            self.next = next

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.count = 0
        self.head = self.Node()
        self.cur = self.head  

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.push(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
        if key not in self.cache:
            node = self.Node(key=key, val=value)
            self.push(node)
            self.cache[key] = node 
            self.count += 1
            if self.count > self.capacity:
                if self.count > self.capacity:
                    del self.cache[self.head.next.key]
                    self.remove(self.head.next)
                    self.count -= 1
        else:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.push(self.cache[key])
                
    def remove(self, node: Node) -> None:
        if node is self.cur:
            self.cur = node.last
        node.last.next = node.next
        if node.next:
            node.next.last = node.last
    
    def push(self, node: Node) -> None:
        prev = self.cur
        self.cur = node
        self.cur.last = prev
        self.cur.next = None
        prev.next = self.cur

