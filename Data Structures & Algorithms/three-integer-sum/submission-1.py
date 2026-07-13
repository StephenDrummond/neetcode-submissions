class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            n = nums[i]
            target = 0 - n
            l, r  = i + 1, len(nums) - 1

            while l < r:
                x = nums[l] + nums[r]

                if x > target:
                    r -= 1
                elif x < target:
                    l += 1
                else:
                    ans.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
        
        return list(ans)