class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        previous = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in previous:
                return [previous[diff], idx]

            previous[num] = idx