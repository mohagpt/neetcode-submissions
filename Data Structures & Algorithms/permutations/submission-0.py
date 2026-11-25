class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, current = [], []
        used = [False] * len(nums)
        def build():
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i, x in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    current.append(x)
                    build()
                    current.pop()
                    used[i] = False
        build()
        return result