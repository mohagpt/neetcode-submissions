class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}

        for c in s :
            count = map_s.get(c)
            if count == None :
                map_s[c] = 1
            else : 
                map_s[c] = count + 1 
        
        for c in t :
            count = map_t.get(c)
            if count == None :
                map_t[c] = 1
            else : 
                map_t[c] = count + 1

        for k in map_s:
            if map_s.get(k) != map_t.get(k):
                return False

        return True