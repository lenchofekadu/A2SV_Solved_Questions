class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0 
        dominant = 0 
        count = defaultdict(int)

        left = 0 
        right = 0 
        while right < n:
            count[s[right]] += 1
            dominant = max(dominant, count[s[right]])

            while right - left + 1 - dominant > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res