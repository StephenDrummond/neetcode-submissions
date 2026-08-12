class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r1 = [1]
        r2 = r1
        for i in range(rowIndex):
            r2 = [0] * (len(r1) + 1)
            for j in range(len(r1)):
                r2[j] += r1[j]
                r2[j+1] += r1[j]
            r1 = r2

                

        return r2
            
