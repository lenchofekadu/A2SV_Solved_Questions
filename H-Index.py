class Solution:
    def hIndex(self, citations: List[int]) -> int:
       
        
        citations.sort()
        h = 0
        p = 0   
        num = 0 
        large = 0 
        answer = [0]
        while h <= len(citations):
            num = 0 
            p = 0
            while p < len(citations):

                if citations[p] >= h:
                    num += 1
                
                if num >= h:
                    answer.append(h)
                    break
                p += 1
            h += 1

        return answer[-1]


