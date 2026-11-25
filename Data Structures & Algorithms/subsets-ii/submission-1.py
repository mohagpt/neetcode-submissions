class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, current = [], []
        def build(start):
            result.append(current[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue                   # same value for the same position: skip
                current.append(nums[i])
                build(i + 1)
                current.pop()
        build(0)
        return result