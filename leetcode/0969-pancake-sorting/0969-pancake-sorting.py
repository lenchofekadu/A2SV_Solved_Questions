class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        i = 0
        temp = arr[:]
        for i in range(len(arr)):

            large = max(temp)
            idx = temp.index(large)

            res.append(idx + 1)
            temp[:idx + 1] = reversed(temp[:idx + 1])
         
            res.append(len(temp))
            temp.reverse()
            temp.pop()
            
        return res