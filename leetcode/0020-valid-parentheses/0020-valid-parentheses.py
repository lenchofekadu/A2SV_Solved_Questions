class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        toggle = { ")":"(", "]":"[", "}":"{" }
        if len(s) < 2:
            return False

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
                continue

            if (stack and stack[-1] != toggle[i]) or not stack:
                return False

            stack.pop()
        return not stack