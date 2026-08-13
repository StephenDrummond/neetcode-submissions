class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                sp = i - c
                if sp < 0:
                    continue
                dp[i] = min(dp[i] if i in dp else math.inf, dp[sp] + 1 if sp in dp else math.inf)
        if amount in dp and dp[amount] == math.inf:
            dp[amount] = -1

        return dp[amount] if amount in dp else -1