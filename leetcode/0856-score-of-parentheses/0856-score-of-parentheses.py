class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                temp = stack.pop()
                stack[-1] += max(1, 2 * temp)

        return sum(stack)