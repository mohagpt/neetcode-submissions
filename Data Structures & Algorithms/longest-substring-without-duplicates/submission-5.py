class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex = {}
        res = 0 
        crtLength = 0 

        for i, c in enumerate(s) : 
            lastI = lastIndex.get(c, -1)
            if lastI == -1 :
                crtLength += 1
            else : 
                if i - crtLength > lastI : 
                    crtLength += 1
                else : 
                    res = max(res, crtLength)
                    crtLength = i - lastI
            lastIndex[c] = i
        
        res = max(res, crtLength)
        return res