# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)
            rotated = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated[j][n - 1 - i] = matrix[i][j]
            return rotated

        def are_equal(matrix1, matrix2):
            n = len(matrix1)
            for i in range(n):
                for j in range(n):
                    if matrix1[i][j] != matrix2[i][j]:
                        return False
            return True

        if are_equal(mat, target):
            return True

        for _ in range(3):
            mat = rotate(mat)
            if are_equal(mat, target):
                return True

        return False