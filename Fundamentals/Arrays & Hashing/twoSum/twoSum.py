
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hashmap to store number and its index
        map = {}
        
        # Loop through each element in the array
        for i, num in enumerate(nums):
            diff = target - num  # Calculate the number needed to reach the target
            
            # If that number is already in our hashmap, we found the answer
            if diff in map:
                return [map[diff], i]
            
            # Otherwise, store the index of the current number
            map[num] = i

# Test cases
sol = Solution()

# Test case 1: Normal case
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

# Test case 2: Two numbers at the end
print(sol.twoSum([1, 3, 5, 7], 12))   # Output: [2, 3]

# Test case 3: Negative numbers
print(sol.twoSum([-1, -2, -3, -4, -5], -8))  # Output: [2, 4]

# Test case 4: Target is sum of first and last
print(sol.twoSum([0, 4, 3, 0], 0))    # Output: [0, 3]

# Test case 5: Duplicates in the array
print(sol.twoSum([3, 3], 6))          # Output: [0, 1]
