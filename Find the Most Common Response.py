class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        lst = []

        for i in responses:

            temp = set(i)

            lst.extend(temp)

        count = Counter(lst)

        large = 0
        answer = []

        for value in count.values():
            if value > large:
                large = value

        for key, value in count.items():
            if value == large:
                answer.append(key)

        return min(answer)            
