class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1)for _ in range(n+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[j][i] = dp[j+1][i+1] + 1
                elif dp[j][i+1] > 0 or dp[j+1][i] > 0:
                    dp[j][i] = max(dp[j][i+1], dp[j+1][i])
        for r in dp:
            print(r)

        return dp[0][0]