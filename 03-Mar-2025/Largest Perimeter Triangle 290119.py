# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                ans.append(nums[i]+nums[i+1]+nums[i+2])
        return 0 if len(ans) == 0 else max(ans)

        