class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        answer = []
        for i in order:
            if i in s:
                temp = s.count(i)
                for j in range(temp):
                    answer.append(i)

        for i in s:
            if i not in answer:
                temp = s.count(i)

                for j in range(temp):
                    answer.append(i)


        return "".join(answer)
