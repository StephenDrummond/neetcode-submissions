class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getdistance(x1, x2, y1, y2):
            return (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
        heap = []
        for p in points:
            heapq.heappush(heap, (getdistance(0, p[0], 0, p[1]), p))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans