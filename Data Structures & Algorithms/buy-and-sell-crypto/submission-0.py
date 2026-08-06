class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = sell_price = prices[0]
        max_profit = 0
        for x in prices:
            if x > sell_price:
                sell_price = x
                max_profit = max(max_profit, sell_price - buy_price)
            else:
                if x < buy_price:
                    sell_price = buy_price = x
        return max_profit
