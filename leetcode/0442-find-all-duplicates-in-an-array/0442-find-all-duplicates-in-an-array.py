class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        seen = set()
        res = set()
        for i in nums:
            if i in seen:
                res.add(i)
            seen.add(i)

        return list(res)