# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        ans = ""
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp1 = str(nums[i]) + str(nums[j])
                temp2 = str(nums[j]) + str(nums[i])
                if int(temp1) < int(temp2):
                    nums[i] , nums[j] = nums[j] , nums[i]
        for i in nums:
            ans += str(i)
    
        zc = ans.count("0")
        
        if zc == len(ans):
            return "0"
        else:
            return ans

      
        # ans = nums[0]
        # for i in range(1,len(nums)):
        #     temp = str(ans) + str(nums[i])
        #     temp2 = str(nums[i]) + str(ans)
        #     ans = max(int(temp) , int(temp2))
        # return str(ans)