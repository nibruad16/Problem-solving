# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = right  # Default to max, refine down
        while left < right:
            mid = (left + right) // 2
            countDays = 1
            maxWeights = 0
            for weight in weights:
                if maxWeights + weight > mid:
                    countDays += 1
                    maxWeights = weight
                else:
                    maxWeights += weight
            
            if countDays > days:
                left = mid + 1
            else:
                right = mid
                ans = mid  # Update with the tested capacity
        return ans