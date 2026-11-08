class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        crtSt, crtEn = intervals[0]
        
        for stI, enI in intervals : 
            if stI <= crtEn :
                crtEn = max(crtEn, enI)
            else : 
                res.append([crtSt, crtEn])
                crtSt, crtEn = stI, enI
        res.append([crtSt, crtEn])        
        return res
