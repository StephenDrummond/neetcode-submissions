class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        cur = 0

        for key, val in c.items():
            if val == 1:
                cur += 1
            if cur == k:
                return key
            
        return ""