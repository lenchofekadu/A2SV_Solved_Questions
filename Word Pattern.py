class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()

        if len(pattern) != len(s):

            return False

        correspond = {}

        for one, two in zip(pattern, s):
            if one in correspond:
                if correspond[one] != two:
                    return False
            else:
                correspond[one] = two
        temp = {}
        for two, one in zip(s, pattern):
            if two in temp:
                if temp[two] != one:
                    return False

            else:
                temp[two] = one

        return True
