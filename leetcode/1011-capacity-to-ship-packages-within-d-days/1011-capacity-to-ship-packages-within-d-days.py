class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(capacity):
            day = 1
            current = 0
            for weight in weights:
                if current + weight > capacity:
                    day += 1
                    current = 0

                current += weight
            return day
        small = max(weights)
        large = sum(weights)
        ans = None
        while small <= large:
            mid = (small + large) // 2
            temp = check(mid)

            if temp <= days:
                ans = mid
                large = mid - 1
            else:
                small = mid + 1
        return ans