class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 0:
            return 0
            
        large = 0 
        first = 0 
        for i in range(len(nums) - 1):

            if nums[i + 1] - nums[i] != 1:
                first = i + 1
            
            else:

                if i + 1 - first > large:
                    large = i + 1 - first

        return large + 1
