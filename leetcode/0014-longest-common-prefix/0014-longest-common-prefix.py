class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        current = min(strs)
        res = len(current)
        for word in strs:

            i = 0 
            while i < len(word) and i < len(current):
                if word[i] == current[i]:
                    i += 1
                else:
                    res = min(res, i)
                    break

        return current[:res]
                