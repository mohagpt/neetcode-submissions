class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            num = nums[mid]

            if target == num:
                return mid
            elif nums[low] <= num:              # left half [low..mid] is sorted
                if nums[low] <= target < num:
                    high = mid - 1              # target is in the sorted left half
                else:
                    low = mid + 1
            else:                               # right half [mid..high] is sorted
                if num < target <= nums[high]:
                    low = mid + 1               
                else:
                    high = mid - 1

        return -1