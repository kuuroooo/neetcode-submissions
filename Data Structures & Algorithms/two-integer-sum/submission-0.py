class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, x in enumerate(nums):
            c = target - x
            if c in h:
                return [h[c], i]
            h[x] = i
