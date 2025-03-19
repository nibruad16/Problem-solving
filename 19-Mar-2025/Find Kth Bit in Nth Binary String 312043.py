# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(s):
                return "".join("1" if c == "0" else "0" for c in s)

        
        def generate(n):
            if n == 1:
                return "0"
            prev = generate(n - 1)  
            return prev + "1" + invert(prev)[::-1] 

       
        ans = generate(n)

        return ans[k - 1]

        
            

        