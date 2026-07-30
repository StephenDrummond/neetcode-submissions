class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hm = defaultdict(list)
        mx = -1

        for i in range(len(s)):
            c = s[i]
            hm[c].append(i)

        for arr in hm.values():
            if arr[0] != arr[-1]:
                mx = max(mx, arr[-1] - arr[0] -1)
        
        return mx