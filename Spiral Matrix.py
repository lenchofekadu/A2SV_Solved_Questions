class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lst = []

        while matrix:
          
            lst += matrix.pop(0)
       
            for i in matrix:
                if i:
                    lst.append(i.pop())

            if matrix:
                temp = matrix.pop()
          
                lst.extend(temp[::-1])

            for i in range(len(matrix) - 1, -1, -1):
                if matrix[i]:
                    lst.append(matrix[i].pop(0))


        return lst



