class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, crt, crtSum):
            if crtSum == target:
                res.append(crt.copy())        # found one: store a copy
                return
            if idx == len(nums) or crtSum > target:
                return                        # out of numbers or overshot

            crt.append(nums[idx])
            dfs(idx, crt, crtSum + nums[idx]) # take nums[idx], and it can be taken again
            crt.pop()                         # undo the choice
            dfs(idx + 1, crt, crtSum)         # skip nums[idx] for good

        dfs(0, [], 0)
        return res