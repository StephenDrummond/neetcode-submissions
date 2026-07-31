class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                ans += 2
            else:
                seen.add(c)
        return ans + 1 if seen else ans