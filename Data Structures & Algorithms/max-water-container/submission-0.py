class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1

        res = (r - l) * min(heights[l], heights[r])

        while r > l :
            if heights[r] > heights[l] :
                l += 1
            else : 
                r -= 1 
            res = max(res, (r - l) * min(heights[l], heights[r]))

        return res

