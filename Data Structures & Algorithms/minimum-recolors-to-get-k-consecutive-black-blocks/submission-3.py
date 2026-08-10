class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k-1
        numBlacks = 0

        for i in range(k):
            if blocks[i] == 'B':
                numBlacks += 1
        
        maxBlacks = numBlacks

        for i in range(k, len(blocks)):
            maxBlacks = max(maxBlacks, numBlacks)
            print(l, r, r-l)
            r += 1
            if blocks[r] == 'B': numBlacks += 1
            if blocks[l] == 'B': numBlacks -= 1
            l += 1
            
            print(numBlacks)
        return k - maxBlacks

