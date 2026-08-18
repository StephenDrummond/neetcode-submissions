class Solution:
    def uniquePaths(self, cols: int, rows: int) -> int:
        dp = [[0] * cols for _ in range(rows)]
        visited = set()
        q = deque((0, 0))
        direc = [[1, 0], [0, 1]]
        dp[0][0] = 1

        for r in range(rows):
            for c in range(cols):
                for dr, dc in direc:
                    if r - dr >= 0 and c - dc >= 0:
                        dp[r][c] += dp[r-dr][c-dc]
        print(dp)
        return dp[rows-1][cols-1]