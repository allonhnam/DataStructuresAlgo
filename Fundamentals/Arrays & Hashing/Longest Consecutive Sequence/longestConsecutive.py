from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  # Convert list to set for O(1) lookups
        longest = 0         # Tracks the length of the longest sequence found

        for num in numSet:
            # Only start counting if `num` is the beginning of a sequence
            # i.e., (num - 1) is not in the set, so this is the first in the chain
            if (num - 1) not in numSet:
                length = 1
                # Count how long the consecutive sequence is
                while (num + length) in numSet:
                    length += 1
                # Update the longest sequence found so far
                longest = max(length, longest)
        
        return longest  # Return the length of the longest consecutive sequence

sol = Solution()

# Test case 1: Regular consecutive sequence
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4 ([1, 2, 3, 4])

# Test case 2: Duplicates and unordered input
print(sol.longestConsecutive([1, 2, 0, 1]))  # Output: 3 ([0, 1, 2])

# Test case 3: Empty list
print(sol.longestConsecutive([]))  # Output: 0

# Test case 4: Single element
print(sol.longestConsecutive([10]))  # Output: 1

# Test case 5: Negative numbers
print(sol.longestConsecutive([-2, -3, -1, 0, 1]))  # Output: 5 ([-3, -2, -1, 0, 1])

# Test case 6: All numbers the same
print(sol.longestConsecutive([7, 7, 7]))  # Output: 1

# Test case 7: Already sorted consecutive list
print(sol.longestConsecutive([1, 2, 3, 4, 5]))  # Output: 5
