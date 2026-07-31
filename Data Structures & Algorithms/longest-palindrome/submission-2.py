class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        has_odd = False
        
        for key, val in c.items():
            if not val % 2:
                ans += val
            else:
                ans += val - 1
                has_odd = True
        return ans + 1 if has_odd else ans
