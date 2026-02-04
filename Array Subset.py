#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
    
        if len(b) > len(a):
            return False
        
        
        a_freq = {}
        b_freq = {}
        
        for i in a:
            if i in a_freq:
                a_freq[i] += 1
            else:
                a_freq[i] = 1

        for i in b:
            if i in b_freq:
                b_freq[i] += 1
            else:
                b_freq[i] = 1
        
        
        for key in b_freq.keys():
            
            if key not in a_freq or b_freq[key] > a_freq[key]:
                
                return False
                
        return True
