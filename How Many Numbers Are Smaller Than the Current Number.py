class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        lst = sorted(nums)

        answer = []

        for i in nums:
            answer.append(lst.index(i))

        return answer
