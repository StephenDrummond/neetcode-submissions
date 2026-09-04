class Solution:
    def customSortString(self, order: str, s: str) -> str:
        bucket = [0] * 26
        ans = ''

        for c in s:
            i = ord(c) - ord('a')
            bucket[i] += 1
        
        for c in order:
            i = ord(c) - ord('a')
            if bucket[i] > 0:
                ans += c * bucket[i]
                bucket[i] = 0

        for i in range(len(bucket)):
            if bucket[i] > 0:
                ans += chr(i + ord('a')) * bucket[i]     

        return ans