class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(r, c, i) :
            if i == len(word) : 
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in visited :
                return False
            
            visited.add((r,c))
            result = False
            for dr, dc in directions : 
                result = result or dfs(r + dr, c + dc, i + 1)
            visited.remove((r,c))

            return result

        for r in range(ROWS) : 
            for c in range(COLS) : 
                if dfs(r,c, 0) : 
                    return True

        return False