class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        double = 0
        for i in nums:
            if i in seen:
                double = i
            seen.add(i)
        n = len(nums)
        nums = set(nums)
        lost = int((n + n ** 2) / 2 - sum(nums))

        return [double, lost]