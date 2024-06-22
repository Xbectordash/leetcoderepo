class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_price = 0
        n = len(prices)
        for i in range(n-1):
            if prices[i+1] > prices[i]:
              total_price += prices[i+1] - prices[i]
        return total_price
        