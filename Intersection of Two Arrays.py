class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        first = list(set(nums1) - (set(nums1) - set(nums2)))
        second = list(set(nums2) - (set(nums2) - set(nums1)))

        return list(set(first + second))
