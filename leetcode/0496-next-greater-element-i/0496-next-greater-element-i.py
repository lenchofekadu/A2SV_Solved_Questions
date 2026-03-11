class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        res = {}

        for n in nums2:
           res[n] = -1

        for num in nums2:
            while stack and num > stack[-1]:
                p = stack.pop()
                res[p] = num
            stack.append(num)
        ans = []
        for num in nums1:
            ans.append(res[num])

        return ans