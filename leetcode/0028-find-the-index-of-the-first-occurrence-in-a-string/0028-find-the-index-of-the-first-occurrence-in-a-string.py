class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        idx = 0
        while idx < len(haystack):
            if haystack[idx] == needle[0]:
                i = idx
                if i + len(needle) > len(haystack):
                    break
                while i - idx < len(needle):
         
                    if needle[i - idx] != haystack[i]:
                        break
                    i += 1
                else:
                    return idx
            idx += 1
        return -1