class MinStack:

    def __init__(self):
        self.nums = []

    def push(self, val: int) -> None:
        if not self.nums or val < self.nums[-1][1]:
            self.nums.append((val, val))
        else:
            self.nums.append((val, self.nums[-1][1]))


    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1][0]

    def getMin(self) -> int:
        return self.nums[-1][1]
