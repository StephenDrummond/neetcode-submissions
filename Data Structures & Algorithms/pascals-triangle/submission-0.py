class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            ans.append([1])
            for j in range(1, i+1):
                ans[i+1].append(ans[i][j] + ans[i][j-1])
            
            ans[i+1].append(1)
        
        return ans
