class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        target = sum(nums) // 2
        n = len(nums)
        dp = [[False] * (n + 1) for _ in range(target + 1)]
        for i in range(len(dp[0])):
            dp[0][i] = True

        for i in range(1, target + 1):
            for j in range(1, n + 1):
                if i - nums[j-1] >= 0:
                    dp[i][j] = dp[i-nums[j-1]][j-1] or dp[i][j-1]


        return dp[target][n]
        