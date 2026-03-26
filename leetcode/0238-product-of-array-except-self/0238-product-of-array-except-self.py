class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mult = 1
        before = []
        after = [0] * len(nums)

        for i in nums:
            before.append(mult)
            mult *= i 
        mult = 1
        for i in range(len(nums) - 1, -1, -1):
            after[i] = mult
            mult *= nums[i]
        res = []
        for first, sec in zip(before, after):
            res.append(first * sec)

        return res