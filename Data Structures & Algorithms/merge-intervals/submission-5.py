class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        crtS, crtE = intervals[0]
        for strt, end in intervals : 
            if strt <= crtE : 
                crtE = max(crtE, end)
                continue
            res.append([crtS, crtE])
            crtS, crtE = strt, end
        
        res.append([crtS, crtE])
        return res