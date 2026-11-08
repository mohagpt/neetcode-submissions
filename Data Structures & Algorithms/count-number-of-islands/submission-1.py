class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        nbOfIslands = 0 
        
        for r in range(ROWS) : 
            for c in range(COLS) : 
                if grid[r][c] == "1" : 
                    queue = deque()
                    queue.append([r,c])
                    grid[r][c] = "X" #visited island
                    nbOfIslands += 1
                    while queue : 
                        crtR, crtC = queue.popleft()
                        for dr, dc in directions : 
                            newR, newC = crtR + dr, crtC + dc

                            if newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS or grid[newR][newC] != "1" : 
                                continue
                            queue.append([newR,newC])
                            grid[newR][newC] = "X"


        return nbOfIslands