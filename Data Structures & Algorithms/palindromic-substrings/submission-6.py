class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[False] * (n + 1) for _ in range(n+1)]
        # for _ in range(n):dp[0][_] = True

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    ans += 1
                    dp[i][j] = True
                
        return ans