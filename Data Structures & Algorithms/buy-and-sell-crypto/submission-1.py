class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])

        l, r = 0, 1
        res = 0

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            res = max(res, curr_profit)

            if prices[r] < prices[l]:
                l = r
            
            r += 1
        
        return res
            