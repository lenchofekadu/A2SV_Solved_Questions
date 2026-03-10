class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []

        for i in logs:
            if i[:2] == "..":
                if stack:
                    stack.pop()
                continue
            elif i[0] == ".":
                continue

            stack.append(i)
        return len(stack)

            