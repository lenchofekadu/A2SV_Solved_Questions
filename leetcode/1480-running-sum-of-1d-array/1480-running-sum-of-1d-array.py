class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        total = 0 
        prefix = []

        for i in nums:
            total += i 
            prefix.append(total)

        return prefix