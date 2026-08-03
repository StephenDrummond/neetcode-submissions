class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1][:]
        

        for row in range(n - 2, -1, -1):
            print(dp)
            temp = []
            for col in range(len(triangle[row])):
                temp.append(min(dp[col] + triangle[row][col], dp[col+1] + triangle[row][col]))
            dp = temp

        return dp[0]