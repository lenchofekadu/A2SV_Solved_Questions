class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def sub(arr, i , curr):
            if i == len(arr):
                res.add(tuple(sorted((curr[:]))))
                return 

            sub(arr, i + 1, curr + [arr[i]])
            sub(arr, i + 1, curr)

        sub(nums, 0, [])
        return [list(x) for x in res]