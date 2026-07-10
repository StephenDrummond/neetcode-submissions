class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = c.most_common(k)

        return [x[0] for x in c]
