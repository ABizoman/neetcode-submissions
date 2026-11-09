from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = dict()
        seen[nums[0]] = 0 
        for i in range(1,len(nums)):
            index = seen.get(target-nums[i], i)
            if index != i:
                return [index, i]
            seen[nums[i]] = i
            
            
            
        