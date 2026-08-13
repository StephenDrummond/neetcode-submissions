class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        mx = 0

        for c in s:
            if c == '(':
                ans += 1
            elif c == ')':
                ans -= 1
            mx = max(mx, ans)

        return mx