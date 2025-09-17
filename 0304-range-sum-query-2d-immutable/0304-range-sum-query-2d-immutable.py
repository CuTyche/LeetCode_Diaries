class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        self.summat = [[0]* (cols+1) for r in range (rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.summat[r][c+1]
                self.summat[r+1][c+1] = prefix + above

    def sumRegion(self, r1, c1, r2, c2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r1, r2, c1, c2 = r1+1, r2+1, c1+1, c2+1
        BR = self.summat[r2][c2]
        above = self.summat[r1-1][c2]
        left = self.summat[r2][c1-1]
        TL = self.summat[r1-1][c1-1]

        return BR - above - left + TL

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)