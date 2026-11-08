class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = [0] * 128
        for c in t:
            countT[ord(c)] += 1

        need = len(t)
        have = 0
        countS = [0] * 128

        l = 0
        resL = float("inf")
        res = ""
        for r in range(len(s)):
            c = s[r]
            if not c in t:
                continue

            countS[ord(c)] += 1
            if countS[ord(c)] <= countT[ord(c)]:
                have += 1

            while have == need:
                if r - l + 1 < resL:
                    resL = r - l + 1
                    res = s[l:r+1]
                i = ord(s[l])
                if countT[i] > 0:
                    countS[i] -= 1
                    if countS[i] < countT[i]:
                        have -= 1
                l += 1

        return res