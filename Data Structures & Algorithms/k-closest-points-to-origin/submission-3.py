class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            distance = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(heap, (distance, p))
        
        print(heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans