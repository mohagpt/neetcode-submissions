class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low, high = 0, len(nums) -1 

        while low <= high : 
            mid = (low + high) // 2

            if nums[mid] == target : 
                strt = end = mid 
                while strt - 1 >= 0 and nums[strt - 1] == target : 
                    strt -=1
                while end + 1 < len(nums) and nums[end + 1] == target : 
                    end +=1
                return [strt, end]
            elif nums[mid] < target : 
                low = mid + 1
            else :
                high = mid - 1
                

        return [-1,-1]
        