class TimeMap:

    def __init__(self):
        self.hMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hMap.setdefault(key, []).append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.hMap.get(key, [])
        res = ""
        l, r = 0, len(vals) - 1

        while l <= r:
            m = (l + r) // 2
            if vals[m][0] <= timestamp:
                res = vals[m][1]  
                l = m + 1
            else:
                r = m - 1      

        return res

