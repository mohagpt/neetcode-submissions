class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strMin, strMax = min(strs), max(strs)
        for i in range(min(len(strMin), len(strMax))):
            if strMin[i] != strMax[i]:
                return strMin[:i]
        return strMin[:min(len(strMin), len(strMax))]