class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check_inside(arr, t):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == t:
                    return True
                elif arr[mid] > t:
                    right = mid - 1
                else:
                    left = mid + 1

            return False
            
        m, n = len(matrix), len(matrix[0])
        left = 0 
        right = m - 1
        
        while left <= right:
            mid = (left + right) // 2
            if check_inside(matrix[mid], target):
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        