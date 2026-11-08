class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])           # by pickup location
        active = [] # [start, numPassengers]
        crtPass = 0
        for numPass, fromI, toI in trips:
            while active and active[0][0] <= fromI:
                crtPass -= heapq.heappop(active)[1]   # these passengers got off already
            crtPass += numPass
            if crtPass > capacity:
                return False
            heapq.heappush(active, (toI, numPass))
        return True