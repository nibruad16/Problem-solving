# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        count = sum(nums[:k])
        ma_= count
        for i in range(k,len(nums)):
            count -= nums[i-k]
            count += nums[i]
            ma_= max(count,ma_)
        return ma_/k
        