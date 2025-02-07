# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        row , col = len(matrix) , len(matrix[0])
        ans = [[0]*row for _ in range(col)]

        for r in range(row):
            for c in range(col):
                ans[c][r] = matrix[r][c]
        return ans