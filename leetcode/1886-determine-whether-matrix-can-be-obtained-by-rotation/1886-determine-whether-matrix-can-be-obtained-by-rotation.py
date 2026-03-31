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
        if check == target:
            return True
        check2 = rotate(check, n)
        if check2 == target:
            return True
        check3 = rotate(check2, n)
        if check3 == target:
            return True
        check4 = rotate(check3, n)
        if check4 == target:
            return True
        return False
        
