# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       

        if n <= 0:
            return False
        else:
            temp = log(n,4)
            if temp == int(temp):
                return True
            else:
                return False
           
        