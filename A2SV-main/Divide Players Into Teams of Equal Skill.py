class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        ans = []
        while left < right:
            temp = []
            temp.append(skill[left])
            temp.append(skill[right])
            ans.append(temp)
            left += 1
            right -= 1
        temp1 = []

        for skil in range(len(ans)):
            temp1.append(sum(ans[skil]))
        temp = sum(ans[0])
        temp2 = set()
        temp2 = set(temp1)
        ans2 = []
        if len(temp2) == 1:
            for i in range(len(ans)):
                me = ans[i][0] * ans[i][1]
                ans2.append(me)
            return (sum(ans2))
        else:
            return (-1)

                    
            
