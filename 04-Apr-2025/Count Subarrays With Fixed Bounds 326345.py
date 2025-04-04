# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0 
        j = -1 
        prevmin = -1
        prevmax = -1 
        for i, num in enumerate(nums): 
            if num < minK or num > maxK:
                j = i 
            if num == minK:
                prevmin = i 
            if num == maxK:
                prevmax = i 

       
            ans += max(0, min(prevmin, prevmax) - j)

        return ans
        