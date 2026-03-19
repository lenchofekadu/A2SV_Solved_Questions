class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        res = []
        changed.sort()
        if len(changed) % 2 == 1:
            return []

        for i in changed:
            if count[i] == 0:
                continue

            if count[2 * i] == 0:
                return []

            res.append(i)
            count[i] -= 1
            count[2 * i] -= 1
        return res