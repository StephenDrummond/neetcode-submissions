class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        cooldown = {}
        heap = []

        for t in tasks:
            if t in cooldown:
                cooldown[t] += n + 1
            else:
                cooldown[t] = 0
            heapq.heappush(heap, (cooldown[t], t))
        
        while heap:
            if cycles >= heap[0][0]:
                heapq.heappop(heap)
            cycles += 1
        return cycles