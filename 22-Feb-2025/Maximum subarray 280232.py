# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax = 0
        max_ = float("-inf")
        for i in nums:
            currmax = max(i,currmax + i)
            max_ = max(currmax , max_)
        return  max_