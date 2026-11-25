class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        pal = [[False] * n for _ in range(n)]       # pal[i][j]: s[i..j] reads the same both ways
        start, length = 0, 1
        for i in range(n - 1, -1, -1):              # i downward: row i + 1 must be ready
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):    # ends match, inside is one
                    pal[i][j] = True
                    if j - i + 1 > length:
                        start, length = i, j - i + 1
        return s[start:start + length]