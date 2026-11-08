class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        dp = [float("inf")] * COLS     # "previous row" before row 0: nothing reachable from above
        dp[0] = 0
        for row in grid:
            dp[0] += row[0]                                  # first column: can only come from above
            for c in range(1, COLS):
                dp[c] = min(dp[c], dp[c - 1]) + row[c]       # min(above, left) + current cell
        return dp[-1]