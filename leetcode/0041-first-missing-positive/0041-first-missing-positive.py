class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = set(nums)
        print(check)
        for i in range(1, len(nums) + 1):
            if i not in check:
                return i

        return max(nums) + 1    