class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        distance = [[0]* len(grid[0]) for _ in range(len(grid))]
        distance[0][0] = grid[0][0]

        for r in range(len(grid)) : 
            for c in range(len(grid[0])) :
                if r == 0 and c == 0 : 
                    continue 
                distance[r][c] = min(distance[r-1][c] if r>0 else float("inf"), distance[r][c-1] if c > 0 else float("inf")) + grid[r][c]
        
        return distance[len(grid) -1][len(grid[0]) -1]