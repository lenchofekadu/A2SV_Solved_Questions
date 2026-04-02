class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0 

        for key, value in count.items():
            temp = ceil(value / (key + 1))
            total += (key + 1) * temp

        return total