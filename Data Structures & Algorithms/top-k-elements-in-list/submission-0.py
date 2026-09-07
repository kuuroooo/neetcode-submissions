import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [(b,a) for a, b in c.items()]
        heapq.heapify_max(freq)
        res = []
        for i in range(0,k):
            res.append(heapq.heappop_max(freq)[1])
        return res
