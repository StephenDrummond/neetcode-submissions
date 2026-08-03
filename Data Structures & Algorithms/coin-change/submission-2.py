class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hm = {}

        def bfs (amt):
            q = deque([(amt, 0)])
            visited = set([amt])

            while q:
                cur, step = q.popleft()
                print(cur, step)
                if cur == 0:
                    return step
                for coin in coins:
                    if cur - coin in visited or cur - coin < 0: continue
                    visited.add(cur-coin)
                    q.append((cur-coin, step + 1))

            return -1

        return bfs(amount)