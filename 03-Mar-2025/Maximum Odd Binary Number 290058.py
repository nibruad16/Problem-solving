# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        contone = s.count("1")
        contzero = s.count("0")

        ans = ""
        for i in range(contone-1):
            ans += "1"
        for i in range(contzero):
            ans += "0"
            
        ans += "1"
        return ans

        