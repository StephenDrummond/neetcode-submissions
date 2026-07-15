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
        
        while mn <= mx:
            mid = (mn + mx) // 2
            finished = can_finish(mid)
            if finished and not can_finish(mid - 1):
                return mid
            elif finished:
                mx = mid - 1
            elif not finished:
                mn = mid + 1
            

        return -1