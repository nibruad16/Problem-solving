# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(x):
            if x == 0:
                return 1
            else:
                return x * fact(x-1)
        
        temp = fact(n)
        cnt = 0
    
        while temp % 10 == 0:
            cnt += 1
            temp = temp // 10
        return cnt

  


        