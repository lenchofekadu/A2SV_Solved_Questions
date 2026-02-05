class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)

        lst = []
        for key, value in count.items():

            if value == 2:
                lst.append(key)

        return lst
