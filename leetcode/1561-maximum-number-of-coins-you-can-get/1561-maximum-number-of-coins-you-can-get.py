class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort(reverse=True)
        check = []
     
        start = 0 
        for i in range(n // 3):

            for j in range(start, start + 2):
                check.append(piles[start])
                start += 1
            check.append(piles[n - 1 - i])
            
        total = 0 
        start = 1 
     
        while start < n:
            total += check[start]
            start += 3
        return total