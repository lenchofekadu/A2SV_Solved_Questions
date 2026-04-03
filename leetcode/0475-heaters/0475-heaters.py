class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(heaters)
        houses.sort()
        heaters.sort()
        large = float("-inf")
        for house in houses:
            low = float("inf")
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                diff = abs(heaters[mid] - house)
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
                low = min(low, diff)
            large = max(large, low)
        return large