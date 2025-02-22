# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        coun = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                coun += 1
            while coun > k:
                if nums[l] == 0:
                    coun -= 1
                l += 1
            
            res = max(r - l + 1 , res)
        return res