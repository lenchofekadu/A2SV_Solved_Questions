class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        i = 1

        while n % 2 != 0:
            n *= i
            i += 1
        return n 
