class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0,0
        numblacks = 0
        mx = 0

        while r < len(blocks):
            c1 = blocks[r]
            c2 = blocks[l]
            if c1 == 'B':
                numblacks += 1
            
            
            if r+1 >= k:
                l += 1
                mx = max(numblacks, mx)
                if c2 == 'B':
                    numblacks -= 1
                
            r += 1
            
        return k - mx