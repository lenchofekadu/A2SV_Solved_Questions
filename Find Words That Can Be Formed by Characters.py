class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        charsc = Counter(chars)

        s = 0
        toggle = True
        for i in words:
            toggle = True
            for j in i:
                if j in charsc:
                    if i.count(j) > charsc[j]:
                        toggle = False
                        
                else:
                    toggle = False
                    
            if toggle:
                s += len(i)

        return s
