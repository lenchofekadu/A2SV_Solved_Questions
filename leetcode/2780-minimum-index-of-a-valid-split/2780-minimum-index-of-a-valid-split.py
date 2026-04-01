class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        large = 0 
        for key, value in count.items():
            if value > large:
                large = value
                dominant = key

        r_dominant = large
        l_dominant = 0
        
        for idx, num in enumerate(nums):
           
            if num == dominant:
                l_dominant += 1
                r_dominant -= 1
            left = idx + 1
            right = len(nums) - left
            
            if l_dominant > left // 2 and r_dominant > right // 2:
                return idx
        return -1