class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        l = 0
        greatest = 0
        maxf = 0

        for r in range(len(s)):
            c = s[r]
            hm[c] += 1
            maxf = max(maxf, hm[c])

            while (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            greatest = max(greatest, r - l + 1)

        return greatest


            