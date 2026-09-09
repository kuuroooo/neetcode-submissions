import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        buckets = []
        for x in range(len(nums) + 1):
            buckets.append([])
        for item, count in c.items():
            buckets[count].append(item)
        res = []
        for x in range(len(buckets) - 1, 0, -1):
            for i in buckets[x]:
                res.append(i)
                if len(res) == k:
                    return res
        return res