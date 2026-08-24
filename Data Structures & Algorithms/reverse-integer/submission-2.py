class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 2**31 - 1, -2**31
        ans = 0
        abs_x = abs(x)

        tens = 1
        while 10**(tens-1) <= abs(x):
            digit = abs_x % 10
            abs_x //= 10
            ans = ans * 10 + digit

            tens += 1
        
        ans = ans if x >= 0 else -ans
        if MIN > ans or MAX < ans:
            return 0
        return ans
        

