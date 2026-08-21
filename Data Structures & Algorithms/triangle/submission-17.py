class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[] for _ in range(n + 1)]
        for i in range(len(triangle[-1]) + 1):
            dp[n].append(0)

        for i in range(n-1, -1, -1):
            for j in range(len(triangle[i])):
                dp[i].append(triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1]))

        return dp[0][0]