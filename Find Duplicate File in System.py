class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ### migerm approach believe me
        dandi = []
        # ezi part ly 1 folder wust yalutn file ke ene directoryachew endiyaskemt enaregewalen: every file is treated separately 
        for i in paths:
            
            separate = i.split()  # notice directory ena malet file name mehal space ale. so ezach space tetekmen file name le bcha enawetalen
           
            for j in separate[1:]:

                dandi.append(f"{separate[0]}/{j}")   # yhe dmo file directory + / + file name aynet ngr nw miseraw malet nw


        """this is the intersting part. I am not even sure how it fully works. So we count how many times the content of the file repeated itself.
        lemisale: (abcd) mil content staaay[see], (abcd) yalebetn index save taregalek. Yhe nw interesting partu(save maregu malet nw). 
        So indexun save mnaregibat bota ye dictionary value ga, list create enaregalen ena eza wust enezin index save enaregalen.
        keza 'key' dmo yhen (abcd) enaregalen keza (abcd) sntegna sntegna index ly 
        endemeta count mareg nw beqa. So ahun abcd ayachua keza dictionary wust: key = abcd, value = [abcd`n yagegnachubet index] keza melisachu lela abcd stayu
         ye ahunu: key = abcd yalnibet bota tmetuna adis index append mareg Done """
        freq = {}

        answer = []

        for i in range(len(dandi)):

            para = dandi[i].index("(")
            check = dandi[i][para + 1:-1]

            if check in freq:
                freq[check].append(i) # ayesha, freq wust kale append enaregewalen ye ahunun index malet nw
            else:
                freq[check] = [i] # kalela dmo adis list ye ahunun index ende first element yzo create enaregalen

        # beqa ahun dmo dictionary ly iterate argen value wust yaskemetnachewun index refer eyaregn, ke original list wust(which is dandi) file paths 
        # extract mareg nw

        for key, value in freq.items():
            lst = []
            for j in value:    # so this j is the index in the value of the freq dictionary malet nw. 
                para = dandi[j].index("(") # yhe ye first parantheses index nwa return miyaregaw? notice dmo j nw ende index use eyaregn yalenaw
                lst.append(dandi[j][:para]) # keza slice yaregnawun part append mareg

            if len(lst) > 1: # ye lst length 1 nw malet crash mimesasel bota altegegneletm malet nw.so there is no need to append. We can't append it enji endewum
                answer.append(lst)
        return answer
