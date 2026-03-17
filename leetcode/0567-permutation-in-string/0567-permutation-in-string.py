class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = Counter(s1)

        left = 0 
        right = len(s1) - 1

        while right < len(s2):
            current = s2[left:right + 1]
            co = Counter(current)

            if co == count:
                return True
            left += 1
            right += 1

        return False