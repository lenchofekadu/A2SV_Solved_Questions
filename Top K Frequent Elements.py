class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        lst = []

        for key, value in count.items():

            lst.append([value, key])

        lst.sort(reverse = True)

        ans = []

        return [lst[n][1] for n in range(k) ]
