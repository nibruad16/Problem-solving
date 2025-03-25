# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        best = -1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            calculated_h = 0
            for i in piles:
               calculated_h += ceil(i / mid)
            if calculated_h  <= h:
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        return best

           



