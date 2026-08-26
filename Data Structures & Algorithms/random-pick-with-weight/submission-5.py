class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        for i in range(len(w)):
            for j in range(w[i]):
                self.w.append(i)

    def pickIndex(self) -> int:
        return random.choice(self.w)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()