from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # for i in range(len(numbers)):
        #     need = target - numbers[i]
        #     if need in numbers[i:]:
        #         print(need, numbers.__getitem__(1))
        #         return [i, numbers.__getitem__(need)]

        numberDict = defaultdict(int)
        numbers = numbers[::-1]
        for i in range(len(numbers)):
            need = target - numbers[i]
            if numberDict[need] != 0:
                return [len(numbers) - i, numberDict[need]]
            numberDict[numbers[i]] = len(numbers) - i 
