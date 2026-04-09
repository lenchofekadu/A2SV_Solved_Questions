class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        up = 1
        row = col = 0

        for _ in range(m * n):

            res.append(mat[row][col])

            row -= up
            col += up

            if row == m:
                row = m  - 1
                col += 2
                up *= -1
            if col == n:
                col = n - 1
                row += 2
                up *= - 1
            
            if row < 0:
                row = 0 
                up *= -1

            if col < 0:
                col = 0 
                up *= -1
        return res