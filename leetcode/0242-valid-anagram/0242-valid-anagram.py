class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countT = Counter(t)
        countS = Counter(s)

        return countS == countT