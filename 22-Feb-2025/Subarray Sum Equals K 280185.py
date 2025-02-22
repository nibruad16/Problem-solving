# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hashmap = Counter({0:1})
        count = 0
        sum_ = 0
        for i in nums:            
            sum_ += i  
            count += hashmap[sum_- k]
            hashmap[sum_] += 1 
             
        return count





         
        



