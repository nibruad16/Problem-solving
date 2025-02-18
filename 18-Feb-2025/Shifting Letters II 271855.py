# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        presum = [0] * (n + 1) 
        
        for row in shifts:
            start, end, direction = row
            if direction == 1:
                presum[start] += 1
                presum[end + 1] -= 1
            else:
                presum[start] -= 1
                presum[end + 1] += 1
        
    
        for i in range(1, n):
            presum[i] += presum[i - 1]
        
        
        shifted_chars = []
        for i in range(n):
            new_char = chr(((ord(s[i]) - ord('a') + presum[i]) % 26) + ord('a'))
            shifted_chars.append(new_char)
        
        return "".join(shifted_chars)





        # presum = [0]* len(s)
        # chars = [ord(i) for i in s]
        
        # for row in shifts:
        #     for j in range(row[0],row[1]+1):
        #         if row[2] == 0:
        #             presum[j] -= 1
        #         else:
        #             presum[j] += 1
        # ans = ""
        # for i in range(len(chars)):
        #     temp = (chars[i] + presum[i]) 
        #     if temp > 122:
        #         temp = 97
        #     if temp < 97:
        #         temp = 122
        #     ans += chr(temp)
        # return ans



        