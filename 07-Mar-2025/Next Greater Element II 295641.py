# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        ans = [-1] * len(nums)
        for i in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    top = stack.pop()
                    ans[top] = nums[i]
                stack.append(i)
            
        return ans
         