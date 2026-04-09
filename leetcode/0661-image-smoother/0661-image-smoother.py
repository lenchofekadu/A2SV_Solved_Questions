class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        res = []
        for i in range(row):
            temp = []
            for j in range(col):

                total = 0 
                count = 0 

                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        x_axis, y_axis = i + x, j + y
                        
                        if 0 <= x_axis < row and 0 <= y_axis < col:
                            total += img[x_axis][y_axis]
                            count += 1
                temp.append(total // count)
            res.append(temp)
        return res
