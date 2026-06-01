class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = n = 0

        while n < len(nums):
            if nums[n] != 0:
                nums[n], nums[zero] = nums[zero], nums[n]
                zero += 1
            n += 1