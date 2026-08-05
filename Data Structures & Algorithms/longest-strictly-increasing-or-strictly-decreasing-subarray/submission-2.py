class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        direction = 0
        l = 0
        mx = 1

        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                if direction != 1:
                    l = r-1
                    direction = 1
            elif nums[r] < nums[r-1]:
                if direction != -1:
                    l = r-1
                    direction = -1
            else:
                l = r
                direction = 0
            mx = max(r - l + 1, mx)

        return mx
