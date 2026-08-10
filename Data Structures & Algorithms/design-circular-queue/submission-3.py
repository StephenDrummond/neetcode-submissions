class QNode:
    def __init__(self, val=-1, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.head = QNode()
        self.tail = self.head
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        self.size += 1
        self.tail.nxt = QNode(value, prev=self.tail, nxt=None)
        self.tail = self.tail.nxt
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.nxt
        return True
        
    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        if self.size == 0:
            self.tail = self.head
            self.head.nxt = None
        else:
            self.head.nxt = self.head.nxt.nxt
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.nxt.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()