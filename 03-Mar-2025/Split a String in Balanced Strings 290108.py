# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            countR= 0
            countL= 0
            for j in range(i,len(s)):
                if s[j] == "R":
                    countR += 1
                else:
                    countL += 1

                if countR == countL:
                    new = s[j+1:]
                    a = new.count("R")
                    b = new.count("L")
                   
                    if a == b:
                        ans += 1
            return ans

 
        