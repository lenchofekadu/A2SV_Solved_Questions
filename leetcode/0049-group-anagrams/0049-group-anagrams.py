class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        another = {}

        for num in strs:
            temp = "".join(sorted(num))
            if temp in another:
                another[temp].append(num)
            else:
                another[temp] = [num]

        res = []

        for value in another.values():
            res.append(value)

        return res