class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(ord("a"), ord("z"))
        print(ord("A"), ord("Z"))
        # ord(a) = 97     ord(A) = 65
        # ord(z) = 122    ord(Z) = 90

        left = 0 
        right = len(s) - 1
        while left < right:
            if not (65 <= ord(s[left]) <= 90 or 97 <= ord(s[left]) <= 122 or s[left].isnumeric()):
                left += 1
                continue
            if not (65 <= ord(s[right]) <= 90 or 97 <= ord(s[right]) <= 122 or s[right].isnumeric()):
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True