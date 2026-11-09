from collections import defaultdict

class Solution:
    def __init__(self):
        self.subarrayCount = 0


    def subarraySum(self, nums: List[int], k: int) -> int:

        # for [2,-1,1,2], 
        # [2, 1, 2, 4] so for every i keep the sum of 0 to i
        # then dance for a bit
        # then find a way to subtract the other 
        # how do I check that i -> j is blabla
        # in my second list: 
            # 0 is 2, I look for all 0s to the left, add that number of 0s found to the left to the result sum 
            # 1 is 2

        cummulativeDict = defaultdict(int)
        currentSum = 0
        for number in nums:
            currentSum += number
            wantedValue = currentSum - k
            if wantedValue == 0:
                self.subarrayCount += 1
                # print(cummulativeDict, "wantedValue:", wantedValue)
            self.subarrayCount += cummulativeDict[wantedValue]
            cummulativeDict[currentSum] += 1

        return self.subarrayCount





        