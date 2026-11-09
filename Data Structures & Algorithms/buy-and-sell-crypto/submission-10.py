class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = 999
        profit = 0
        j = 0  
        for i in range(len(prices)):
            profit = max(profit, prices[i] - mi) 
            if prices[i] < mi:
                mi = prices[i]

        return profit
        