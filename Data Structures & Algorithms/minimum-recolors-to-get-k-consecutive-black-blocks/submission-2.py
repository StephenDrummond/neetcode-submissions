class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0,k
        c = Counter(blocks[:k])
        mx = c['B']

        while r < len(blocks):
            c[blocks[r]] += 1
            if r + 1 >= k:
                c[blocks[l]] -= 1
                l += 1
            
            r += 1
            mx = max(mx, c['B'])
            
        return k - mx