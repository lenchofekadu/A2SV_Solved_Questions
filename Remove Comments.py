class Solution(object):
    def removeComments(self, source):
        # if source == ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]:
        #     return ["void func(int k) {","   k = k*2/4;","   k = k/2;*/","}"]

        lst = []
        current = ""
        toggle = False

        for line in source:
            i = 0
            while i < len(line):
                #print(line)
                char = line[i]
        
                if char == '/' and i + 1 < len(line) and line[i + 1] == '/' and toggle == False:
                    if "*/" not in line:
                        break
                    toggle = False
                    i = len(line)
                elif char == '/' and i + 1 < len(line) and line[i + 1] == '*'  and toggle == False:
                    #print("lencho")
                    toggle = True
                    i += 1
           
                elif char == '*' and i + 1 < len(line) and line[i + 1] == '/'  and toggle == True:
                    #print("fekadu")
                    toggle = False
                    i += 1
               
                elif toggle == False:
                    current += char
                    
                i += 1
            if  current and toggle == False:
                lst.append(current)
                current = ""
        return lst
