from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = inf, 0

        for p in prices:
            if buy > p:
                buy = p
                sell = 0
            else:
                sell = max(sell, p)

            profit = max(profit, sell - buy)


        return profit