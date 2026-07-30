class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hm = {}
        mx = -1

        for i in range(len(s)):
            c = s[i]
            if c in hm:
                mx = max(mx, i - hm[c] - 1)
            else:
                hm[c] = i
        
        return mx