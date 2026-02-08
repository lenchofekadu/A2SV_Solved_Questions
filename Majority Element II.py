class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        answer = []

        for key, value in count.items():

            if value > len(nums) // 3:
                answer.append(key)

        return answer
