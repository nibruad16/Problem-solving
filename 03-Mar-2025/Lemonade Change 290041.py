# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        # [5,5,5,10,20]
        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1
            if i == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
                




        