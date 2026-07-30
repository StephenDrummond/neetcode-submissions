class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        r1, r2 = 0, 0

        for i in range(len(nums)-1):
            temp = max(r1 + nums[i], r2)
            r1 = r2
            r2 = temp

        mx = r2

        r1, r2 = 0, 0

        for i in range(1,len(nums)):
            temp = max(r1 + nums[i], r2)
            r1 = r2
            r2 = temp
        
        return max(mx, r2)