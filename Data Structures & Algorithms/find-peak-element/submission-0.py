class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1


        while low <= high : 
            mid = (low + high) // 2

            left = nums[mid-1] if mid -1 >= 0 else  float("-inf")
            right = nums[mid+1] if mid +1 < len(nums) else  float("-inf")
            if left < nums[mid] and nums [mid] > right : #peak
                return mid
            elif left > nums[mid] : 
                high = mid - 1
            else :
                low = mid + 1
        return -1


                
                

                 
