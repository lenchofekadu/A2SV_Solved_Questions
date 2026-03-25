class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        t = sorted(t)
        s = sorted(s)
        print(t)
        print(s)
        if t in s or t == s:
            return True

        return False