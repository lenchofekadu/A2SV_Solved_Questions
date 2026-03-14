class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        left = 0
        right = len(skill) - 1
        check = skill[0] + skill[-1]
        res = 0 
        while left < right:
            
            if skill[left] + skill[right] != check:
                return -1

            res += skill[left] * skill[right]

            left += 1
            right -= 1
        
        return res