# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        result = []
        direction = 1 
        row, col = 0, 0

        for _ in range(m * n):
            result.append(mat[row][col])

            new_row, new_col = row - direction, col + direction

            if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                if direction == 1:  
                    if col + 1 < n:
                        row, col = row, col + 1
                    else:
                        row, col = row + 1, col
                else:  
                    if row + 1 < m:
                        row, col = row + 1, col
                    else:
                        row, col = row, col + 1
                direction *= -1  
            else:
                row, col = new_row, new_col

        return result