class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)
            
            if prices[r] < prices[l]:
                l = r
            r += 1
            
        return max_profit