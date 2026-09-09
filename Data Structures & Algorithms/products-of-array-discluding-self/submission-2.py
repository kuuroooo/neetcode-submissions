class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,1,2,8]
        # [1,2,4,6]
        # [48,24,6,1]
        prefix = [1]
        for i, x in enumerate(nums[1:]): 
            # print(i + 1)
            prefix.append(prefix[i] * nums[i])
        # print(prefix)
        suffix = [1]
        for i in range(len(nums) - 1, 0, -1):
            # print(i)
            suffix.append(nums[i] * suffix[len(nums) - i -1])
        # print(suffix)
        result = [] 
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[len(nums) - i -1])
        return result