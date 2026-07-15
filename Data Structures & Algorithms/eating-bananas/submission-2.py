class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        mn = math.ceil(sum(piles) / h)
        n = len(piles)
        if n == h:
            return mx

        def can_finish(k):
            if k == 0:
                return False
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/k)
            return hrs <= h

        ran = range(mn, mx)
        l, r = ran[0], ran[len(ran) - 1]
        
        while l <= r:
            mid = (l + r) // 2
            finished = can_finish(mid)
            if finished and not can_finish(mid - 1):
                return mid
            elif finished:
                r = mid - 1
            elif not finished:
                l = mid + 1
            

        return -1