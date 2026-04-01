class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    first = arr[j] + arr[j + 1]
                    second = arr[j + 1] + arr[j]
                    if first > second:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
            return arr
        res = reversed(bubble_sort(nums))
        return str(int("".join(res)))
                    
        