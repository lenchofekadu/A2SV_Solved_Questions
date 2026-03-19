class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        first = Counter(word1)
        second = Counter(word2)

        lst = [v for v in first.values()]
        lst2 = [v for v in second.values()]

        return sorted(lst) == sorted(lst2)