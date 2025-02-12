# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        gap = len(height) - 1
        right = len(height) - 1
        left = 0
        max_num = 0
        while left < right:
            temp = min(height[left],height[right])
            area = temp * gap
            max_num = max(max_num ,area)
            if height[left] < height[right]:
                left += 1
                gap -= 1
            elif  height[left] == height[right]:
                left += 1
                right -= 1
                gap -= 2
            else:
                right -= 1
                gap -= 1
        return max_num

        