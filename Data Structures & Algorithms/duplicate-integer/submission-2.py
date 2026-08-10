class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = defaultdict(int)

        for n in nums:
            hm[n] += 1
            if hm[n] > 1:
                return True

        return False