class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        lst = []

        while x:
            lst.append(x % 10)
            x = x // 10

        for i in range(len(lst)):

            if lst[i] != lst[len(lst) - 1 - i]:
                return False
        return True

