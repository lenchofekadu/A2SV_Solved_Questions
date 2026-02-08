class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = {}


        for i in strs:

            temp = "".join(sorted(i))

            if temp in freq:
                freq[temp].append(i)
            else:
                freq[temp] = [i]

        answer = []
  
        for value in freq.values():
            lst = []
            for j in value:
                lst.append(j)
            answer.append(lst)

        return answer
