class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        n = len(nums)
        target = s // 2
        dp = [[False] * (n+1) for _ in range(target + 1)]
        for i in range(n+1):
            dp[0][i] = True

        for i in range(1, target + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j-1] or nums[j-1] == i or (i - nums[j-1] >= 0 and dp[i-nums[j-1]][j-1])

        return dp[target][n]