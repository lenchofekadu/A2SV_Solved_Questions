class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        # ans = (5 ** (n // 2) % (10 ** 9 + 7)) 
        # ans *= (4 ** (n // 2) % (10 ** 9 + 7))
        # ans *=  5 ** (n % 2) 
        # return ans 

        one = pow(5, n//2, 1000000007)
        two = pow(4, n//2, 1000000007)
        three = pow(5, n%2)
        
        return one*two*three % 1000000007