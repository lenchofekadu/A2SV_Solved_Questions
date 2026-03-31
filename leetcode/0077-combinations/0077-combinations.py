class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        lst = [x for x in range(1, n + 1)]
        def subarray(arr, i, curr):
            if len(curr) == k:
                res.append(curr[:])
                return 
            if i == len(arr):
                return 

            subarray(arr, i + 1, curr + [arr[i]])
            subarray(arr, i + 1, curr)
        
        subarray(lst, 0, [])
        return res
