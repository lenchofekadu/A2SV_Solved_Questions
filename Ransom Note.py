class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if Counter(ransomNote) <= Counter(magazine):
            return True

        return False
