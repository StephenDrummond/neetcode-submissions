class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for px, py in points:
            edist = math.sqrt(px**2 + py**2)
            heapq.heappush(heap, (-edist, (px, py)))
            if len(heap) > k:
                heapq.heappop(heap)

        return [list(node) for e, node in heap]