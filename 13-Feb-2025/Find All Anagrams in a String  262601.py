# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        new = Counter(p)
        temp = Counter(s[:len(p)])
        ans = []

        left = 0
        if temp == new:
            ans.append(left)
        
    
        for r in range(len(p),len(s)):
            temp[s[left]] -= 1
            temp[s[r]] += 1

            if temp[s[left]] == 0:
                del temp[s[left]]
            
            left += 1

            if temp == new:
                ans.append(left)
       
        return ans

        



        