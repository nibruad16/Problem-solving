# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = []
        presum.append(nums[0])
        for i in range(1,len(nums)):
            presum.append(presum[i-1] + nums[i])
        return presum