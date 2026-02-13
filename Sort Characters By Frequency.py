class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        lst = []
        for key, value in count.items():

            lst.append([value, key])

        lst.sort(reverse=True)

        an = ""
        for i in lst:
            an += i[1] * i[0]

        return an
