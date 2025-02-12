# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for i in range(len(costs)):
            if coins - costs[i] >= 0:
                count += 1
                coins -= costs[i]
        return count
        