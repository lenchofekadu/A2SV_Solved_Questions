class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        st = ""

        for i in nums:
            st += str(i)

        output = []

        for j in st:
            output.append(int(j))

        return output
