class Solution:
    def intToRoman(self, num: int) -> str:
        lst = []
        m = len(str(num))
        romans = {1000:"M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}

        for ind, n in enumerate(str(num)):
            current = int(n) * 10 ** (m - ind - 1)
            lst.append(str(current))

        print(lst)
        res = []
        for i in lst:
            first = int(i[0])
      
            if first != 4 and first != 9:
            
                if first < 5:
                    mult = 10 ** (len(i) - 1)
                    for i in range(first):
                        res.append(romans[mult])
                else:
                    mult = 10 ** (len(i) - 1)
                    res.append(romans[mult * 5])
                    for i in range(first - 5):
                        res.append(romans[mult])

            else:
                
                mult = 10 ** (len(i) - 1)
                res.append(romans[mult])
                res.append(romans[mult * first + mult])
           
                
        return "".join(res)