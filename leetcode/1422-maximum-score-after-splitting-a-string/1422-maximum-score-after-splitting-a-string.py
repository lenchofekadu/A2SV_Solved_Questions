class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = s.count("1")
        large = 0 
        for x in range(len(s) - 1):
            if s[x] == "0":
                zeros += 1
            else:
                ones -= 1
            large = max(large, ones + zeros)

        return large
            