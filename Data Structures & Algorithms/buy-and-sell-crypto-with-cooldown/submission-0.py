class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, rest = float("-inf"), 0, 0     # best profit in each state at the end of the day
        for price in prices:
            hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)
        return max(sold, rest)