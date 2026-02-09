class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        answer = [0] * len(s)

        char = 0 
        index = 0 

        while char < len(s) and index < len(s):

            answer[indices[index]] = s[char]

            index += 1
            char += 1


        return "".join(answer)
