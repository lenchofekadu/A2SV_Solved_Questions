class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()

        for i in range(len(nums) + 1):
            print(i)
            if i not in nums:
                return i


        
