class Solution:
    # return a result array: result[i] number of days after day i before a 
    # a warmer temperature appears

    # sort temperatures
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # something about a stack
        # 40, 38, 36, 35 
        stack = list()
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                index = stack.pop()[1]
                answer[index] = i - index
            stack.append([temperatures[i], i])


        return answer

# [30 0]     

