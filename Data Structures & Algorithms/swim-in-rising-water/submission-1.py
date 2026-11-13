class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(grid), len(grid[0])

        if ROWS == 1 and COLS == 1 : 
            return grid[0][0]

        heap = [(grid[0][0], 0,0)]
        crtTime = 0 
        visited = set()
        visited.add((0,0))
        while heap : 
             
            weight, r, c = heapq.heappop(heap)
            for dr, dc in directions : 
                newR, newC = r + dr, c + dc
                if newR == ROWS -1 and newC == COLS -1 : 
                    return max(weight, grid[newR][newC]) 
                if newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS or (newR, newC) in visited: 
                    continue
                
                heapq.heappush(heap,(max(weight, grid[newR][newC]), newR, newC))

                visited.add((newR, newC))
            
        return -1
        
