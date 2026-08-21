class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        ans, o, e = 0, 0, 0
        pre = 0

        for n in arr:
            pre += n

            if pre % 2: 
                ans += e + 1
                o += 1
            else:
                ans += o
                e += 1
                
        
        return ans