class Solution:
    def findValidPair(self, s: str) -> str:
        
        count = Counter(s)

        if len(s) < 2:
            return ""

    

        for i in range(len(s) - 1):

            if count[s[i]] == int(s[i]) and count[s[i + 1]] == int(s[i + 1]):
                if s[i] != s[i + 1]:
                    return f"{s[i]}{s[i + 1]}"

        return ""
