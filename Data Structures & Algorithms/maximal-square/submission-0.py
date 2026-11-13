class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[int(x) for x in row] for row in matrix]
        crtMax = 0
        for r in range(ROWS):
            for c in range(COLS):
                if dp[r][c] == 0:
                    continue
                if r > 0 and c > 0:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                crtMax = max(crtMax, dp[r][c])
        return crtMax * crtMax