class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        check = []

        total = 0 

        for i in nums:
            if i % 2 == 0:
                check.append(True)
                total += i
            else:
                check.append(False)

        answer = []
        for j in queries:
            if check[j[1]]: # even kehone malet
                if j[0] % 2 == 0: # ahun midemerbetm even kehone the result would be even 
                    total += j[0] # mejemeria dmo even blen yedemernaw ly j[0] medemer

                else:
                    total -= nums[j[1]]
                    check[j[1]] = False

            else: # odd kehone dmo, temeliso even lemehon odd add medereg alebat
                if j[0] % 2 == 1:
                    total += j[0] + nums[j[1]] # eziga huletum nw midemerubet, why the first was odd and now even
                    check[j[1]] = True
                
            nums[j[1]] += j[0]

            answer.append(total)

        return answer
