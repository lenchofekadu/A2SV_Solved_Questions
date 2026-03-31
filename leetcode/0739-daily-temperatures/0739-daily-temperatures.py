class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev, _ = stack.pop()
                res[prev] = i - prev

            stack.append([i, temp])
        
        return res