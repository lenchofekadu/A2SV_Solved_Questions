class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        def winner(m, z):
            if m == 1:
                return 0 

            starting = winner(m - 1, z)

            return (starting + z) % m

        return winner(n, k) + 1