# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            start_i, end_i = firstList[i]
            start_j, end_j = secondList[j]

            start_intersect = max(start_i, start_j)
            end_intersect = min(end_i, end_j)

            if start_intersect <= end_intersect:
                result.append([start_intersect, end_intersect])

            
            if end_i < end_j:
                i += 1
            else:
                j += 1

        return result