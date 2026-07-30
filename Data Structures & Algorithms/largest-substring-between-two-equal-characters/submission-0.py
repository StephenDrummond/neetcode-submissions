class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mx = -1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    mx = max(mx, j-i-1)

        return mx