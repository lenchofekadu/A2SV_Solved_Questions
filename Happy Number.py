class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n != 1:
            st = str(n)
            n = 0 

            for i in st:
                n += int(i) ** 2
            
            if n == 4 or n == 16 or n == 37 or n == 58 or n == 89 or n == 145 or n == 42 or n == 20:
                return False
            
        else:
            return True
        
