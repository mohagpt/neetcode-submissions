class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        if not prices : 
            return 0

        crtBuy = prices[0]
        for price in prices : 
            if price < crtBuy : 
                crtBuy = price
            maxProfit = max(maxProfit, price - crtBuy)

        
        return maxProfit