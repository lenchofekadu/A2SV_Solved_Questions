class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        prefix = []

        total = 0 
        for i in nums:
            total += i
            prefix.append(total)

        return 1 if min(prefix) > 0 else abs(min(prefix)) + 1