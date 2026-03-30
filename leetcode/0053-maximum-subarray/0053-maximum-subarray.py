class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        large = min(nums)
        upto = 0
        for i in nums:
            upto += i 
            large = max(large, upto)
            if upto < 0:
                upto = 0 
            
        return large