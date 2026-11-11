class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        squares = defaultdict(set)
        rows = defaultdict(set)
        columns = defaultdict(set)

        for r in range(9) : 
            for c in range(9) : 
                if board[r][c] == ".":
                    continue
                elem = board[r][c] 
                if elem in rows[r] or elem in columns[c] or elem in squares[(r // 3, c // 3)] : 
                    return False
                rows[r].add(elem)
                columns[c].add(elem)
                squares[(r // 3, c // 3)].add(elem)

        return True