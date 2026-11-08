class Solution:
    def simplifyPath(self, path: str) -> str:
        
        #replace all Multiple consecutive slashes by a single slash
        arr = path.split("/")

        res = []
        for s in arr : 
            if not s or s == ".": 
                continue 
            if s == "..": 
                if len(res) > 0 : res.pop()
                continue
            res.append(s)


        return "/" + "/".join(res)