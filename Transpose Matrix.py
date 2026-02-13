class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        transpose = []
        first = 0 

        for i in range(len(matrix[0])):
            temp = []
            for i in matrix:
                temp.append(i[first])

            transpose.append(temp)
            first += 1
        return transpose
