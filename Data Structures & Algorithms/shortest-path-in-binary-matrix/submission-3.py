class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] : return -1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]

        queue = deque()
        
        queue.append([0,0])
        dist = [[-1] * COLS for _ in range(ROWS)]
        dist[0][0] = 1
        grid[0][0] = -1
        while queue : 
            r,c = queue.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return dist[r][c]
            for dr, dc in directions : 
                newR, newC = r + dr, c + dc
                if newR >= ROWS or newR < 0 or newC >= COLS or newC < 0 or grid[newR][newC] != 0 : 
                    continue
                if dist[newR][newC] == -1 : 
                    dist[newR][newC] = dist[r][c] + 1
                else :
                    dist[newR][newC] = min(dist[r][c] + 1, dist[newR][newC])
                queue.append([newR, newC])
                grid[newR][newC] = 1


        return dist[ROWS-1][COLS-1]
                