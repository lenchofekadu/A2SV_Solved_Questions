class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}  
        res = []
        left = 0
        right = 0
        
        for i, ch in enumerate(s):
            right = max(right, last[ch])  
            if i == right:  
                res.append(right - left + 1)
                left = i + 1
        return res