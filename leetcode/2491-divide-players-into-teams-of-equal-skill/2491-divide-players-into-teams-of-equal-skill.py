class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
       
        skill.sort()
        left = 0 
        right = len(skill) - 1
        check = skill[0] + skill[-1]
        ans = 0
        while left < right:
            if skill[left] + skill[right] != check:
                ans = -1
                break
            else:
                ans += skill[left] * skill[right]
            left += 1
            right -= 1
        return ans