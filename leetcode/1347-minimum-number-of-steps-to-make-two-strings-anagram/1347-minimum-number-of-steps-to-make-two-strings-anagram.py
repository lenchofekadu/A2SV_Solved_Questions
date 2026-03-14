class Solution:
    def minSteps(self, s: str, t: str) -> int:

        s_counter = Counter(s)
        t_counter = Counter(t)

        lst = list(s_counter.keys() & t_counter.keys())

        common = 0 

        for i in lst:
            common += min(s_counter[i], t_counter[i])

        return len(s) - common