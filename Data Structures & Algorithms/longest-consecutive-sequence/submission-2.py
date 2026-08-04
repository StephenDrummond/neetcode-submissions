class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        possibilities = deque()

        for n in nums:
            seen.add(n)

        for n in nums:
            if n-1 not in seen:
                possibilities.append(n)
        
        mx = 0
        for p in possibilities:
            cur = 0
            while p in seen:
                cur += 1
                p = p+1
            mx = max(mx, cur)
        
        return mx