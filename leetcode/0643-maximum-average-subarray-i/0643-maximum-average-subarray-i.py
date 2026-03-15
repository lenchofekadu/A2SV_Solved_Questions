class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        first = sum(nums[:k])
        large = first

        left = 0 
        right = k

        while right < len(nums):
            first += nums[right] - nums[left]
            large = max(large, first)

            right += 1
            left += 1

        return large / k