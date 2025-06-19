from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Track digits seen in each column, row, and 3x3 square
        cols = defaultdict(set)    # key: col index -> set of seen digits
        rows = defaultdict(set)    # key: row index -> set of seen digits
        squares = defaultdict(set) # key: (row//3, col//3) -> set of seen digits in each 3x3 square

        for r in range(9):            # loop over all rows
            for c in range(9):        # loop over all columns
                if board[r][c] == ".":
                    continue          # skip empty cells
                
                val = board[r][c]

                # Check if the value already exists in the same row, column, or square
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]):
                    return False      # Invalid if duplicate is found
                
                # Otherwise, record the digit in row, column, and square
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True  # All checks passed; board is valid

sol = Solution()

board1 = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],  # <--- "1" here conflicts with row
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

print(sol.isValidSudoku(board1))  # Output: True
print(sol.isValidSudoku(board2))  # Output: False
