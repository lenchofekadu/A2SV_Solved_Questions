class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]

        for word in strs:

            i = 0 

            while i < len(word) and i < len(common):

                if word[i] == common[i]:
                    
                    i += 1
                
                else:

                    break

            common = common[:i]
        return common
