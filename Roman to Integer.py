class Solution:
    def romanToInt(self, s: str) -> int:
        

        lst = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


        total = 0 

        i = 0 
        j = 1 

        while j < len(s):
            print(s[i])
            print(lst[s[i]])
            if lst[s[i]] < lst[s[j]]:

                total -= lst[s[i]]
            else:
                total += lst[s[i]]
            i += 1
            j += 1
        total += lst[s[-1]]

        return total
