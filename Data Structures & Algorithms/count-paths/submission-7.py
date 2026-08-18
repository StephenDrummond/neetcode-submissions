class Solution:
    def uniquePaths(self, cols: int, rows: int) -> int:
        dp = [1] * cols
        for r in range(1, rows):
            for c in range(1, cols):
                dp[c] += dp[c-1]
        return dp[-1]