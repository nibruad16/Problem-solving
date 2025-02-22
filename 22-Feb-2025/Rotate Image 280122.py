# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotates a square matrix 90 degrees clockwise in-place.
        """
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()