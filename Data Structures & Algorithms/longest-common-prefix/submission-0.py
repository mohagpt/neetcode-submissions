class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        res = ""
        strMin, strMax = strs[0], strs[len(strs) -1]
        for i in range(min(len(strMin), len(strMax))) : 
            if strMin[i] == strMax[i] :
                res += strMin[i]
            else :
                break
        return res