class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        low, high = 1, res
        while low < high:
            mid = (low + high) // 2
            duration = 0
            for p in piles:
                duration += math.ceil(p / mid)
            if duration <= h:
                res = mid
                high = mid
            else:
                low = mid + 1

        return res