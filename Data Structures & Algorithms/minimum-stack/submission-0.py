class MinStack:

    def __init__(self):
        self.nums = deque()
        self.minheap = []

    def push(self, val: int) -> None:
        self.nums.append(val)

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return min(self.nums)
