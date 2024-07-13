from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day_i = sell_day_i = 0
        profit = prices[sell_day_i] - prices[buy_day_i]
        for i in range(1, len(prices)):
            if prices[i] < prices[buy_day_i]:
                buy_day_i = i
            if profit < prices[i] - prices[buy_day_i]:
                sell_day_i = i
                profit = prices[sell_day_i] - prices[buy_day_i]
        return profit
