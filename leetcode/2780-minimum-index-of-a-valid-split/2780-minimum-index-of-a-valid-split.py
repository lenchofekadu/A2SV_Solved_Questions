class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        freq = {}
        for key, value in count.items():
            freq[value] = key
        large = 0 
        for value in count.values():
            large = max(large, value)
        r_dominant = large
        large = freq[large]

        left = []
        l_dominant = 0
        
        for idx, num in enumerate(nums):
            left.append(num)
            if num == large:
                l_dominant += 1
                r_dominant -= 1
            right = len(nums) - len(left)
            if l_dominant > len(left) - l_dominant and r_dominant > right - r_dominant:
                return idx
        return -1