# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        track = 0
        for i in range(len(nums)-1):
            track = max(track,nums[i]+i)
            if track == i:
                return False
        return True
        


        

        # if len(nums) == 1:
        #     return True

        # new = len(nums) - 1

        # for i in range(len(nums)):
        #     if new - nums[i] <= 0 :
        #         return True
        #     new -= 1
        # return False
    
        # by = 0
        # for i in range(len(nums)-1):
        #     left = nums[i]
        #     if left >= new:
        #         return True
            
          
        #     ans = 0
        #     while ans <= new and left <= new:
        #         ans += left
        #         left += nums[left]
        #         if left >= new:
        #             return True

        #         if ans == left:
        #             by += 1

        #         if ans - new >= 0:
        #             return True           
        #     new -= 1
          
            
        
        
            
            
            

            
        


        