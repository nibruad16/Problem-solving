# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        ans1 = []
        ans2 =[]
        for row in grid:
            ans1.append(max(row))
        
        for row in range(n):
            val = 0
            for col in range(len(grid[0])):
                val = max(grid[col][row],val)
            ans2.append(val)
        sums = 0
        for i in range(n):
            for j in range(n):
                temp  = min(ans1[i],ans2[j])
                sums += temp - grid[i][j]
        return sums



