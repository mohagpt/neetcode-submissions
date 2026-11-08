class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        
        l, r = 1, max(piles)
        minRes = r
        while l <= r:
            mid = (l + r) // 2

            #Compute nb of hours
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid

            if hours <= h: 
                minRes = mid
                r = mid - 1
            else: 
                l = mid + 1
        return minRes