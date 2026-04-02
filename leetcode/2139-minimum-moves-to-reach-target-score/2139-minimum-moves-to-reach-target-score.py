class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        step = 0 
        while target != 1:
            if maxDoubles:
                if target % 2 == 0:
                    target //= 2
                    maxDoubles -= 1
                else:
                    target -= 1
            else:
                return step + target - 1
            step += 1
        return step