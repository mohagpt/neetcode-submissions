class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(lo, hi):                    # grow while the ends match; return the final bounds
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return lo + 1, hi                  # s[lo + 1:hi] is the palindrome

        start, end = 0, 0
        for center in range(len(s)):
            for lo, hi in (expand(center, center), expand(center, center + 1)):   # odd, even length
                if hi - lo > end - start:
                    start, end = lo, hi
        return s[start:end]