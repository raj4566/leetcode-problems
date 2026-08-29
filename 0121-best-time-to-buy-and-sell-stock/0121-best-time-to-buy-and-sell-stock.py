class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) <= 1:
            return 0
        
        # we need to save the historial lowest price
        lowest_price = prices[0]
        # lowest_price_index = -1
        max_profit = 0
        
        # start find
        for i in prices[1:]:
            if i < lowest_price:
                lowest_price = i
            current_profit = i - lowest_price
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit