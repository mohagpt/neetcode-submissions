class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(leftBias):
            low, high = 0, len(nums) - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    idx = mid                 # found one, but maybe not the first/last
                    if leftBias:
                        high = mid - 1        # keep looking left
                    else:
                        low = mid + 1         # keep looking right
            return idx

        return [search(True), search(False)]