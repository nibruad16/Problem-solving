# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        new = Counter(answers)
        ans = 0
        for tot,feq in new.items():
            group = (tot + feq ) // (tot + 1)
            ans += group * (tot+1)
        return ans