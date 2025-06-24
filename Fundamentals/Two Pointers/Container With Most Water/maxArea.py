from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            # Width between the lines
            width = r - l
            # Height is limited by the shorter line
            h = min(height[l], height[r])
            # Compute area
            area = width * h
            # Update maximum area
            res = max(res, area)

            # Move the pointer at the shorter line inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res

height = [1,7,2,5,4,7,3,6]
print(Solution().maxArea(height))  # Output: 36
