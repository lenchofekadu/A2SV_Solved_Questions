class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        i = 0
        temp = arr[:]
        for i in range(len(arr)):

            large = max(temp)
            idx = temp.index(large)

            res.append(idx + 1)

            first = temp[:idx + 1]
            first.reverse()

            second = temp[idx + 1:]
         
            res.append(len(temp))
            temp = first + second
            temp.reverse()
            temp = temp[:-1]
      
        return res