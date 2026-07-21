class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        sc = Counter()
        l, r = 0, 0
        minwin = math.inf
        ans = ''

        while r < len(s):
            sc[s[r]] += 1
            if tc <= sc:
                while tc <= sc:
                    sc[s[l]] -= 1
                    l += 1
                if r - l < minwin:
                    ans = s[l-1:r+1]
                    minwin = r - l
            r += 1
        return ans