# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
     
        # new = Counter(s1)
        # k = len(s1)
        # count = 0
        
        # for i in range(len(s2)):
        #     temp = Counter(s2[i:k+i])
        #     if temp == new:
        #         count += 1
        # return True if count >= 1 else False

        left = 0
        
        if len(s1) > len(s2):
            return False

        new = Counter(s1)
        temp = Counter(s2[:len(s1)])

        if new == temp:
            return True
        
        for i in range(len(s1),len(s2)):
            temp[s2[left]] -= 1
            temp[s2[i]] += 1

            if temp[s2[left]] == 0:
                del temp[s2[left]]

            if new == temp:
                return True
            
            left += 1
        return False
            

        
        