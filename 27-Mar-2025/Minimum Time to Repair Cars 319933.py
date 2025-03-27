# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = max(ranks) * (cars ** 2)

        while left <= right:
            mid = left + (right - left) // 2

            total = 0
            for i in ranks:
                total += int(sqrt(mid/i))
            
            
            if total < cars:
                left = mid + 1
            else:
                right = mid -1
        
    
        return left



        



