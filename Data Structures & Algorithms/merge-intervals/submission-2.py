class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        crtS, crtE = intervals[0]
        for a, b in intervals[1:] : 
            if a > crtE : 
                res.append([crtS, crtE])
                crtS, crtE = a , b
            else : 
                crtE = max(crtE, b)
        res.append([crtS, crtE])
        return res