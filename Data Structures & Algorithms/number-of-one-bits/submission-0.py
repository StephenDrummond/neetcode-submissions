class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for c in str(bin(n)):
            if c == '1':
                ans += 1
            
        return ans
            