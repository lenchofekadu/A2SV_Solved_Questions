class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums) - 1
        for i in range(n - 2, -1, -1):
       
            if nums[i + 2]  < nums[i + 1] + nums[i]:
                return nums[i + 2] + nums[i + 1] + nums[i]

        return 0 
