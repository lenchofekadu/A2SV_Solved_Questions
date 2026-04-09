class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x : x[1])
       
        count = 1
        current = points[0][1]
        for start, end in points:
            if start > current:
                count += 1
                current = end
        return count
