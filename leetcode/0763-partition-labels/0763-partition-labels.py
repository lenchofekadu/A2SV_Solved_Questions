class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {}

        seen = set()

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in seen:
                last[s[i]] = i 
            seen.add(s[i])

        res = []
        size = 1
        end = 0 
        for idx, ch in enumerate(s):
            end = max(last[ch], end)
            if idx == end:
                res.append(size)
                size = 0 
        
            size += 1
        return res