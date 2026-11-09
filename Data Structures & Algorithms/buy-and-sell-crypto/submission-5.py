class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = i = 0
        mini = prices[0]
        profit = 0
        for j in range(1, len(prices)):
            if prices[j] > maxi:
                maxi = prices[j]
                while i < j:
                    i += 1
                    mini = min(prices[i], mini)
                print(f'maxi: {maxi},mini: {mini}')
                profit = max(maxi - mini, profit)
                maxi = 0

        return profit