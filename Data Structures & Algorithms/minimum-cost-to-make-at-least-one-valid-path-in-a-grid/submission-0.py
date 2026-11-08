import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]    # sign 1: right, 2: left, 3: down, 4: up

        dist = [[float("inf")] * COLS for _ in range(ROWS)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]                           # (cost, row, col)
        while heap:
            d, r, c = heapq.heappop(heap)
            if d > dist[r][c]:                       
                continue
            if (r, c) == (ROWS - 1, COLS - 1):
                return d
            for k, (dr, dc) in enumerate(DIRS):
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    nd = d + (0 if grid[r][c] == k + 1 else 1)   # free if it follows the arrow
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heapq.heappush(heap, (nd, nr, nc))
                