from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []                             # tails[k]: smallest tail of a run of length k + 1
        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)                # x extends the longest run
            else:
                tails[i] = x                   # x is a smaller tail for runs of length i + 1
        return len(tails)