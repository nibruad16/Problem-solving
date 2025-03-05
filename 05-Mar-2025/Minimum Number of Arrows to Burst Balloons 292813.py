# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrow = 1
        last_arr = points[0][1]
        for start,end in points:
            if start > last_arr:
                arrow += 1
                last_arr = end
        return arrow
        

        