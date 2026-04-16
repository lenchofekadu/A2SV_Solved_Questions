class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = Counter(nums)

        large = 0 
        res = None
        for key, value in freq.items():
            if value > large:
                large = value
                res = key

        return res