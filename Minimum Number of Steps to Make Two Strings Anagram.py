class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # I copied this from my neighbor, but I've grasped the concept clean and sheet tho...and thanks neighbor
        count = Counter(s)
        steps = 0
        for ch in t:
            if ch in count:
                count[ch] -= 1
                if count[ch] == 0:
                    del count[ch]
            else:
                steps += 1
        return steps
