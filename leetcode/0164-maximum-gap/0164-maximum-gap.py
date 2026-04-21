class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        nums.sort()
        large = 0 
        for i in range(1, len(nums)):
            large = max(large, nums[i] - nums[i - 1])

        return large