class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        lst = [""]
        small = float("inf")
        first = 0 
        for i in list1:
            second = 0 
            for j in list2:
             
                if i == j:
                    if second + first < small:

                        small = second + first
                        lst[-1] = i
                    elif second + first == small:
                        lst.append(i)
                second += 1
            first += 1

        return lst
