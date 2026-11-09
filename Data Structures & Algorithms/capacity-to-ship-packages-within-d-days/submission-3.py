class Solution:
    def __init__(self):
        self.days = None
        self.weights = []

    def possible(self, cap: int) -> bool:
            cur_weight = 0
            boats = 1
            for number in self.weights:
                if cur_weight + number <= cap:
                    cur_weight += number
                else:
                    boats += 1
                    cur_weight = number
            if boats <= self.days and cur_weight <= cap: 
                return True
            else: return False

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        self.days, self.weights = days, weights
        if days == 1:
            return sum(weights)

        search_space = [i for i in range(max(weights), sum(weights)+1)]
        

        while search_space:
            # Binary Search 
            i = len(search_space) // 2
            capacity = search_space[i]
            # print(capacity, search_space)
            if self.possible(capacity):
                best_found = capacity
                search_space = search_space[:i]
            else: search_space = search_space[i+1:]


        return best_found