class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        freq = {}
        lst = []
        for j in cpdomains:

            rep = j.split()
            interest = rep[-1]
            for i in range(len(interest) - 1, -1, -1):

                if interest[i] == "." or i == 0:
                    temp = interest[i + 1:]
                    if i == 0:
                        temp = interest
                    if temp in freq:

                        freq[temp] += int(rep[0])
                    else:

                        freq[temp] = int(rep[0])
        #print(freq)
        for key, value in freq.items():
            #print(value, key)
            lst.append(f"{value} {key}")

        return lst
