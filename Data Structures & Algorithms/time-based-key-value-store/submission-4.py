class TimeMap:

    def __init__(self):
        self.hMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hMap.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.hMap.get(key, [])
        res = ""
        low, high = 0, len(timestamps) - 1
        while low <= high:
            mid = (low + high) // 2
            val, t = timestamps[mid]
            if t <= timestamp:
                res = val          # valid candidate, look for a later one
                low = mid + 1
            else:
                high = mid - 1     # too late, look earlier
        return res