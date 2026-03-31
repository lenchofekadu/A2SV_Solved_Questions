class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate(matrix, m):
            for i in range(m):
                for j in range(i + 1, m):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            for i in range(m):
                matrix[i].reverse()
            return matrix
            
        check = rotate(mat, n)
        for i in range(4):
            if check == target:
                return True
            check = rotate(check, n)
        return False
        