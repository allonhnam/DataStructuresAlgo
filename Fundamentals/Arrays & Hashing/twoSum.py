# Two Sum
# Solved 
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]
# Constraints:

# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to check every pair of numbers in the array. This would be an O(n^2) solution. Can you think of a better way? Maybe in terms of mathematical equation?


# Hint 2
# Given, We need to find indices i and j such that i != j and nums[i] + nums[j] == target. Can you rearrange the equation and try to fix any index to iterate on?


# Hint 3
# we can iterate through nums with index i. Let difference = target - nums[i] and check if difference exists in the hash map as we iterate through the array, else store the current element in the hashmap with its index and continue. We use a hashmap for O(1) lookups.

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
