# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sums = {0: 1} 
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            if current_sum - goal in prefix_sums:
                count += prefix_sums[current_sum - goal]
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count