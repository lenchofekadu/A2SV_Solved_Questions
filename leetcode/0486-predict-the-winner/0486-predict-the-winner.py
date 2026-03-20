class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def find(left, right):

            if left == right:
                return nums[left]

            l = nums[left] - find(left + 1, right)
            r = nums[right] - find(left, right - 1)

            return max(l, r)

        return find(0, len(nums) - 1) >= 0