class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        increasing = False

        if nums[0] <= nums[1]:
            increasing = True
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i] and not increasing:
                return False
            if nums[i-1] > nums[i] and increasing:
                return False
            
        return True