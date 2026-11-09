class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for j in prices:
            profit = max(profit, j - mini)
            mini = min(mini, j)

        return profit