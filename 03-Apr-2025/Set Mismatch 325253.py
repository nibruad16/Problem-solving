# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        new = Counter(nums)
        ans = []
        track = set(nums)
        for key,val in new.items():
            if val >= 2:
                ans.append(key)
        for i in range(1,len(nums)+1):
            if i not in track:
                ans.append(i)

        return ans
        
            
        

