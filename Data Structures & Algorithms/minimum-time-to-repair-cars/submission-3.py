class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        


        def check(t):
            check_cars = 0
            for rank in ranks:
                check_cars += math.isqrt(t//rank)

            return check_cars >= cars

        # binary search in the range of smallest r and biggest r x cars x cars
        low, high = min(ranks),  max(ranks) * cars * cars
        def search(low, high):
            if low == high:
                return high
            mid = low + ((high - low) // 2)
            if check(mid) == True:
                return search(low, mid)
            else: 
                return search(mid + 1, high)

        
        return search(low, high)
