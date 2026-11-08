class UndergroundSystem:
    def __init__(self):
        self.checkedIn = {}
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedIn.pop(id)
        key = (startStation, stationName)
        total, count = self.trips.get(key, [0, 0])
        self.trips[key] = [total + (t - startTime), count + 1]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.trips[(startStation, endStation)]
        return total / count
