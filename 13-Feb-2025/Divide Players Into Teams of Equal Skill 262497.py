# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        check = set()
        left  = 0
        right = len(skill) - 1
        leng = len(skill)//2
        temp = skill[left] + skill[right]
        check.add(temp)
        count = 0

        for i in range(leng):
            temp = skill[left] + skill[right]
            if temp in check:
                temp = skill[left] * skill[right]
                count += temp
                left += 1
                right -= 1

            else:
                return -1
            
        return count
    



  

        
        