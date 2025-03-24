# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        stack = []
        if x == 1:
            return 1
        if x == 0:
            return 0
        stack.append(1)
        count = 2
        temp = 0
        while temp < x:
            temp = count * count
            if temp  == x:
                return count
            elif temp < x:
                stack.append(count)
                count +=1
            elif temp > x:
                return stack.pop()

