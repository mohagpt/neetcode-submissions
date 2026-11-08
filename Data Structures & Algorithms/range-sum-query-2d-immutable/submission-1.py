class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.prefixSum = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS) : 
            for c in range(COLS) : 
                crtSum = matrix[r][c] 
                if r > 0 : 
                    crtSum += self.prefixSum[r-1][c]
                if c > 0 : 
                    crtSum += self.prefixSum[r][c-1]
                if r > 0 and c > 0 : 
                    crtSum -= self.prefixSum[r-1][c-1]
                self.prefixSum[r][c] = crtSum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        crtSum = self.prefixSum[row2][col2]
        if row1 > 0 : 
            crtSum -= self.prefixSum[row1-1][col2]
        if col1 > 0 : 
            crtSum -= self.prefixSum[row2][col1-1]
        if row1 > 0 and col1 > 0 : 
            crtSum += self.prefixSum[row1-1][col1-1]
        return crtSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)