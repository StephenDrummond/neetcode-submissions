class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 1
        for n in nums:
            s *= n
        if s > 0:
            return 1
        if s < 0:
            return -1
        return 0