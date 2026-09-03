class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(len(coins)+1) for _ in range(amount + 1)]
        for i in range(len(coins) + 1):
            dp[0][i] = 1

        for a in range(1, amount + 1):
            for c in range(1, len(coins) + 1):
                dp[a][c] += dp[a][c-1]
                coin = coins[c-1]
                if a - coin >= 0 and dp[a-coin][c] > 0:
                    dp[a][c] += dp[a-coin][c]

        return dp[amount][len(coins)]