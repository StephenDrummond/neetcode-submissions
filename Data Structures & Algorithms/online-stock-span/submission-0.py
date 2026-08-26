class StockSpanner:

    def __init__(self):
        self.days = []

    def next(self, price: int) -> int:
        self.days.append(price)
        for i in range(len(self.days) - 1, -1, -1):
            if self.days[i] > price:
                return len(self.days) - i -1
        return len(self.days)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)