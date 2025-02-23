# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.presum = [[]]
            return

        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.presum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]  # Corrected dimensions

        for row in range(self.rows):
            for col in range(self.cols):
                self.presum[row + 1][col + 1] = (
                    self.presum[row][col + 1] + self.presum[row + 1][col] - self.presum[row][col]
                    + matrix[row][col]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.presum[row2 + 1][col2 + 1] - self.presum[row2 + 1][col1] -
            self.presum[row1][col2 + 1] + self.presum[row1][col1]
        )