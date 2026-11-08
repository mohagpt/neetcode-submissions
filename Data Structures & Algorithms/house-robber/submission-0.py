class Solution:
    def rob(self, nums: List[int]) -> int:
        
        profit = [0] * len(nums)

        for i, num in enumerate(nums) : 
            profit[i] = max(num + (profit[i-2] if i >= 2 else 0), profit[i-1] if i > 0 else 0)

        return profit[len(nums)-1]