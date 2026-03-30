class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0 
        right = int(c ** 0.5)

        while left <= right:
            current = left * left + right * right
            if current == c:
                return True
            if current > c:
                right -= 1
            else:
                left += 1
        return False