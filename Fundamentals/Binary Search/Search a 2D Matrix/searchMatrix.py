from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False

# Example 1
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
sol = Solution()
print(sol.searchMatrix(matrix, target))  # Expected: True

# Example 2
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15
sol = Solution()
print(sol.searchMatrix(matrix, target))  # Expected: False
