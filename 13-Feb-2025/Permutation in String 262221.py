# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

     
        new = Counter(s1)
        k = len(s1)
        count = 0
        
        for i in range(len(s2)):
            temp = Counter(s2[i:k+i])
            if temp == new:
                count += 1
        return True if count >= 1 else False
            
        