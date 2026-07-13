class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        greatest = 0
        hm = {}

        while r < len(s):
            c = s[r]
            if c not in hm or hm[c] == 0:
                hm[c] = 1
            else:
                hm[c] += 1
            
            if hm[c] > 1:
                while l < r and hm[c] > 1:
                    hm[s[l]] -= 1
                    l += 1
            greatest = max(greatest, 1 + r - l)    
            r += 1
            


        return greatest