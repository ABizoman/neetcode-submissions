class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = 999
        profit = 0
        j = 0  
        for price in prices:
            profit = max(profit, price - mi) 
            if price < mi:
                mi = price

        return profit
        