# Problem: Find the Middle Index in Array - https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        presum = []
        presum.append(nums[0])

        resum = [0] * (len(nums) + 1)

        for i in range(1,len(nums)):
            presum.append(presum[i-1] + nums[i])
        
        for i in range(len(nums)-1,-1,-1):
            resum[i] = resum[i+1] + nums[i]
        
        for i in range(len(nums)):
            if presum[i] == resum[i]:
                return i
        return -1


        