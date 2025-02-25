# Problem: Minimize Maximum Pair Sum in Array - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        right = len(nums) - 1
        nums.sort()
        while left < right:
            temp = nums[left] + nums[right]
            left += 1
            right -= 1
            ans = max(ans,temp)
        return ans
        