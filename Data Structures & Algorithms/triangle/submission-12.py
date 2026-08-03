class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minheap = [(triangle[0][0], 0, 0)]
        ROWS = len(triangle)
        visited = set([(0, 0)])
        mn = math.inf

        while minheap:  
            cur, row, col =  heapq.heappop(minheap)
            if row == ROWS - 1:
                mn = min(mn, cur)
            
            if (row + 1, col + 1) not in visited and row + 1 <= ROWS - 1:
                visited.add((row+1, col + 1))
                heapq.heappush(minheap, (cur + triangle[row+1][col+1], row + 1, col + 1))
            if (row + 1, col) not in visited and row + 1 <= ROWS - 1:
                visited.add((row+1, col))
                heapq.heappush(minheap, (cur + triangle[row+1][col], row + 1, col))
            
        return mn
