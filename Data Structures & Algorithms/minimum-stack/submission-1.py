class MinStack:

    def __init__(self):
        self.nums = deque()
        self.mins = deque()

    def push(self, val: int) -> None:
        self.nums.append(val)
        if not self.mins or val < self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])


    def pop(self) -> None:
        self.nums.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.mins[-1]
