from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # for i in range(len(numbers)):
        #     need = target - numbers[i]
        #     if need in numbers[i:]:
        #         print(need, numbers.__getitem__(1))
        #         return [i, numbers.__getitem__(need)]
        i = 0
        j = len(numbers) - 1
        somm = numbers[i] + numbers[j]
        while somm != target:
            if somm > target:
                j -= 1
            elif somm < target:
                i += 1
            somm = numbers[i] + numbers[j]
        return [i+1, j+1]