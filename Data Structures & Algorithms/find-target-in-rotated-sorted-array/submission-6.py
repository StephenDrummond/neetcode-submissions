class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1:
            return 0 if nums[0] == target else -1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        pivot = l
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            realm = (m + pivot) % n
            if target == nums[realm]:
                return realm
            elif nums[realm] < target:
                l = m + 1
            else:
                r = m - 1

        return -1