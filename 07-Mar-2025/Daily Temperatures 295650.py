# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                top = stack.pop()
                ans[top] =  i - top
            stack.append(i)
        return (ans)
            






        



