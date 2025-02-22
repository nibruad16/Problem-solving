# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    
                
                    if num in rows[i]:
                        return False
                    rows[i][num] = 1

                   
                    if num in cols[j]:
                        return False
                    cols[j][num] = 1

                   
                    if num in boxes[box_index]:
                        return False
                    boxes[box_index][num] = 1

        return True