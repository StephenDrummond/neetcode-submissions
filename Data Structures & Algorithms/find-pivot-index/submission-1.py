class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)

        for i in range(n):
            pre[i+1] = nums[i] + pre[i]
        for i in range(n):
            pref = pre[i]
            suff = pre[n] - pre[i+1]
            if pref == suff:
                return i

        return -1