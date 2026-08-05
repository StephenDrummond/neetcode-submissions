class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        b = Counter('balloon')
        ans = 0

        while b <= c:
            c -= b
            ans += 1

        return ans