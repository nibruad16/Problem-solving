# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:

        left = right = 0
        inc = [0] * len(height)
        dec = [0] * len(height)

        for i in range(len(height)):
            j = -i - 1

            inc[i] = left
            dec[j] = right

            left = max(left,height[i])
            right = max(right,height[j])

        ans = 0
        for i in range(len(height)):
            temp = min(inc[i],dec[i])
            ans += max(0,temp - height[i])

        return ans



        