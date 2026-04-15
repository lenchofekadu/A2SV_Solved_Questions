class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # why wouldn't I sort it

        nums.sort(reverse=True)

        return nums[k - 1]