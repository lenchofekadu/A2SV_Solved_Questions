class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        lst = [[value, key] for key, value in count.items()]

        lst.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(lst[i][-1])

        return res
