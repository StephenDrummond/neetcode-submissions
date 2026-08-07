class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s // 2
        n = len(nums)
        dp = [[False] * (target+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]
        
        
        
