class RandomizedSet:

    def __init__(self):
        self.hm = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False

        self.nums.append(val)
        self.hm[val] = len(self.nums)-1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        
        idx = self.hm[val]
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.hm[self.nums[idx]] = idx
        
        del self.hm[val]
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        x = random.randint(0, len(self.nums)-1)
        return self.nums[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()