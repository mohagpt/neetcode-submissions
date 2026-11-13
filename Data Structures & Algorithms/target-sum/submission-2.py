class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def sumFromIndex(i, crtSum) : 
            if i == len(nums) :
                return 1 if crtSum == target else 0 
            if (i, crtSum) in memo:
                return memo[(i, crtSum)]
            total = sumFromIndex(i + 1, crtSum + nums[i])
            total += sumFromIndex(i + 1, crtSum - nums[i])
            memo[(i, crtSum)] = total
            return total
        

        return sumFromIndex(0, 0)