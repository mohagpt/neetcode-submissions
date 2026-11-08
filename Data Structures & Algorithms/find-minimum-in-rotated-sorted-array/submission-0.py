class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        
        while nums[r] < nums[0] :
            r -= 1
        
        if r == len(nums) - 1 :
            return nums[0]
        else :
            return nums[r + 1]
        