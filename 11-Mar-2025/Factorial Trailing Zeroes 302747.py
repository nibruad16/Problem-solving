# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def me(n):

            if n == 1 or n == 0:
                return 1
           
            return n*me(n-1)

        ans = 0
        temp = me(n)
   
        while temp % 10 == 0:
            ans += 1
            temp //= 10
        return ans



        