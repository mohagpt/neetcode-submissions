class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxCur = 0
        while l < r and r < len(prices) : 
            if prices[r] > prices[l] : 
                maxCur = max(prices[r] - prices[l], maxCur)
                r+=1
            else : 
                l = r
                r +=1
            
        return maxCur
