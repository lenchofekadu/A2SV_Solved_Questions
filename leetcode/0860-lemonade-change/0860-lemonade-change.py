class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0 
        ten = 0 
        twenty = 0 

        for cash in bills:
            if cash == 5:
                five += 1
            elif cash == 10:
                ten += 1
                if five == 0:
                    return False
                five -= 1
            elif cash == 20:
                twenty += 1
                if ten:
                    ten -= 1
                    if five == 0:
                        return False
                    five -= 1
                else:
                    if five < 3:
                        return False
                    five -= 3
        return True