from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        l, r = 0, 0
        minwin = inf
        ct = Counter(t)
        cs = Counter()

        while r < len(s):
            cs[s[r]] += 1
            if ct <= cs:
                while ct <= cs:
                    cs[s[l]] -= 1
                    l += 1
                if minwin > (r + 1) - (l - 1):
                    ans = s[l-1:r+1]
                    minwin = (r + 1) - (l - 1)
            r += 1

        return ans