class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        dandi = []

        for i in paths:
            
            separate = i.split()
           
            for j in separate[1:]:

                dandi.append(f"{separate[0]}/{j}")
                
        freq = {}

        answer = []

        for i in range(len(dandi)):

            para = dandi[i].index("(")
            check = dandi[i][para + 1:-1]

            if check in freq:
                freq[check].append(i)
            else:
                freq[check] = [i]

        for key, value in freq.items():
            lst = []
            for j in value:
                para = dandi[j].index("(")
                lst.append(dandi[j][:para])
            if len(lst) > 1:
                answer.append(lst)
        return answer

        # answer = []
        # common = []
        
        # for i in range(len(dandi)):

        #     para = dandi[i].index("(")
        #     check = dandi[i][para + 1:-1]
        #     lst = []
        #     man = False
        #     for j in range(i + 1, len(dandi)):

        #         temp = dandi[j].index("(")
        #         current = dandi[j][temp + 1:-1]

        #         if check not in common:

        #             if current == check:
        #                 lst.append(dandi[j][:temp])
        #                 man = True
        #         else:
        #             break
             
        #     common.append(check)
        #     if man:
        #         lst.append(dandi[i][:para])

        #     if lst:
        #         answer.append(list(set(lst)))


        # return answer
