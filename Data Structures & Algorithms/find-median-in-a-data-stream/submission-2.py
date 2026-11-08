class MedianFinder:

    def __init__(self):
        self.leftPart = []
        self.rightPart = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftPart, -num)
        heapq.heappush(self.rightPart, -heapq.heappop(self.leftPart))   # keep the order
        if len(self.rightPart) > len(self.leftPart):                    # keep the sizes
            heapq.heappush(self.leftPart, -heapq.heappop(self.rightPart))

        

    def findMedian(self) -> float:
        if len(self.leftPart) > len(self.rightPart) : 
            return -self.leftPart[0]
        else :
            return (-self.leftPart[0] + self.rightPart[0]) / 2
        