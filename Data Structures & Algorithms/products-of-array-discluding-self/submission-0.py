class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * (n + 1)
        suf = [1] * (n + 1)

        for i in range(n):
            pre[i + 1] = pre[i] * nums[i]
            ni = -i-1
            suf[ni - 1] = suf[ni] * nums[ni]

        return [x * y for x, y in zip(pre[:n], suf[1:n+1])]