class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums :
            return 0

        res, maxR = 1 , 1
        nums.sort()            
        prev = nums[0]
        for i in range(1, len(nums)) :
            if nums[i] == prev :
                continue
            if nums[i] == prev + 1 :
                res += 1
            else :
                maxR = max(maxR, res)
                res = 1
            prev = nums[i]
        maxR = max(maxR, res)
        return maxR


        