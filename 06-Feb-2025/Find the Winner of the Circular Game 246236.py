# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [x for x in range(1,n+1)]
        i = 0
        remove = 0
        while len(arr) > 1:
            remove = (i + k - 1) % len(arr)
            arr.pop(remove)
            i = remove % len(arr)
        return arr[0]
       
