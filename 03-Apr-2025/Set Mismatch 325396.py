# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        ans = []
        while i < n:
            check = nums[i] - 1
            if nums[check] != nums[i] :
                nums[check],nums[i] = nums[i],nums[check]
            else:
                i += 1
  
        for i in range(len(nums)):
            if nums[i] != i+1:
                return [nums[i],i+1]
                                                                                                       











        # new = Counter(nums)
        # ans = []
        # track = set(nums)
        # for key,val in new.items():
        #     if val >= 2:
        #         ans.append(key)
        # for i in range(1,len(nums)+1):
        #     if i not in track:
        #         ans.append(i)

        # return ans
        
            
        

