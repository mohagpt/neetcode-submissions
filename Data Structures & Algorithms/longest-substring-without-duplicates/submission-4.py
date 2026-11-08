class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strt = 0
        maxL = 0
        for i in range(len(s)):
            c = s[i]
            if c in s[strt:i]:
                while s[strt] != c:
                    strt += 1
                strt += 1
            maxL = max(maxL, i - strt + 1)
        return maxL