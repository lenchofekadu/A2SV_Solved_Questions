class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        

        lst = []

        for i in grid:
            lst += i

        total = 0 
        for i in lst:
            if i < 0:
                total += 1

        return total
