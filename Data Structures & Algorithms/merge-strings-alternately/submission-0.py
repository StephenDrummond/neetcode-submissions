class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        i = 0
        while word1 and word2:
            if i % 2 == 0:
                ans += word1[0]
                word1 = word1[1:]
            else:
                ans += word2[0]
                word2 = word2[1:]
            i += 1

        if word1:
            ans += word1
        
        if word2:
            ans += word2
        
        return ans