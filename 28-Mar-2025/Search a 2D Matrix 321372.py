# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right = 0, (len(matrix) * len(matrix[0])) -1
        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // len(matrix[0])][mid%len(matrix[0])]

            if num == target:
                return True
            elif num < target:
                left = mid +1
            else:
                right = mid -1
        return False



        