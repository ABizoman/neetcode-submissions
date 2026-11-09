from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = dict()
        seen[nums[0]] = 0 
        for i in range(1,len(nums)):
            try:
                index = seen[target-nums[i]]
                return [index, i]
            except: seen[nums[i]] = i
            
            
        