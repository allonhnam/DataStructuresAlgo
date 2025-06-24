from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Two pointers: left and right

        while l < r:
            curSum = numbers[l] + numbers[r]  # Current sum of two numbers

            if curSum > target:
                r -= 1  # Sum too big, move right pointer left
            elif curSum < target:
                l += 1  # Sum too small, move left pointer right
            else:
                return [l + 1, r + 1]  # Found the pair (1-indexed)

        return []  # No valid pair found

# Example 1
numbers = [1, 2, 3, 4]
target = 3

# Explanation:
# numbers[0] + numbers[1] = 1 + 2 = 3, which matches the target
# So the returned indices (1-indexed) should be [1, 2]

print(Solution().twoSum(numbers, target))  # Output: [1, 2]
