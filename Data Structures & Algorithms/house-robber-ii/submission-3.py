class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        one, two = 0, 0
        for n in nums[:-1]:
            temp = max(one + n, two)
            one = two
            two = temp
        mx = two
        one, two = 0, 0
        for n in nums[1:]:
            temp = max(one + n, two)
            one = two
            two = temp
        return max(mx, two)
        