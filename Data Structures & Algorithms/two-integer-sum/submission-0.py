class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i in range(len(nums)):
            cur = target - nums[i]

            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[cur] = i

        return [0, 0]