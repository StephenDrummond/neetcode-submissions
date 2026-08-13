class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, 0
        ans = 0

        for i in range(len(s)):
            if s[i] == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
                

        return (ans + 1) // 2

