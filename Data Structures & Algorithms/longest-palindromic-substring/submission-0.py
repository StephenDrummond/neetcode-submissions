class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        mx = 0
        l, r = 0,0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > mx:
                        mx = j-i+1
                        l, r = i, j
        print(mx)
        return s[l:r+1]