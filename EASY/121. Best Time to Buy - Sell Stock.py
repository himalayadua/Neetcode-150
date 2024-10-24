from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy,sell =0,1
    
        while sell < len(prices):
            maxProfit = max(maxProfit, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]: buy = sell
            sell += 1
            
        return maxProfit

