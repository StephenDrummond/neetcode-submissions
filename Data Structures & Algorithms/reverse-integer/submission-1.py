class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 2**31 - 1, -2**31
        ans = 0

        tens = 1
        while 10**(tens-1) <= abs(x):
            cur = abs(x) % 10**tens
            cur -= abs(x) % 10**(tens-1)
            cur //= 10**(tens-1)
            
            ans *= 10
            ans += cur
            
            tens += 1
        ans = ans if x >= 0 else -ans
        if MIN > ans or MAX < ans:
            return 0

        return ans
        

