class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current = 0 
        large = nums[0]

        for i in nums:
            if current < 0:
                current = 0 
            
            current += i
            large = max(large, current)
        return large