# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        track = len(piles)//3
        left = 0
        right = 1
        count = 0
        for i in range(track):
            temp = min(piles[left],piles[right])
            count += temp
            left += 2
            right += 2
        return count

        