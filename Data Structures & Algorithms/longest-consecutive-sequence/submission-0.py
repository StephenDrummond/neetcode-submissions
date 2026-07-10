class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        possibilities = deque()

        for n in nums:
            seen.add(n)

        for n in seen:
            if n - 1 not in seen:
                possibilities.append(n)
        
        longest = 0
        while possibilities:
            cur = 0
            p = possibilities.pop()

            while p in seen:
                cur += 1
                p += 1
            longest = max(cur, longest)

        return longest
            