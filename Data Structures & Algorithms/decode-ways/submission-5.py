class Solution:
    def numDecodings(self, s: str) -> int:
        s = list(int(n) for n in s)
        dp = {len(s):1}
        print(dp)
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == 0:
                return 0
            
            ans = dfs(i+1)
            if i + 1 < len(s) and (s[i] == 1 or (s[i] == 2 and s[i+1] <= 6)):
                ans += dfs(i+2)
            dp[i] = ans
            print(dp)
            return ans
        return dfs(0)
