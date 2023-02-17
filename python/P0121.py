class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        min_price = prices[0]    # 当前最低估价
        max_profit = 0           # 当前最大收益

        for idx in range(1, len(prices)):
            price = prices[idx]
            profit = price - min_price

            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit