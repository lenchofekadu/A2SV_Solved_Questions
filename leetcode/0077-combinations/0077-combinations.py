class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        lst = [x for x in range(1, n + 1)]
        print(lst)
        def subarray(arr, i, curr):
            if i == len(arr):
                res.append(curr[:])
                return 

            subarray(arr, i + 1, curr + [arr[i]])
            subarray(arr, i + 1, curr)
        
        subarray(lst, 0, [])
        return [x for x in res if len(x) == k]