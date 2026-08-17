class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                while nums and idx < len(nums) and nums[idx] == val :
                    if idx == len(nums) - 1:
                        nums.pop()
                    else:
                        nums[idx] = nums.pop()


            idx += 1

        return len(nums)