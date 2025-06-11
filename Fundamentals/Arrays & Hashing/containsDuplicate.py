# Contains Duplicate
# Solved 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to check every element against every other element in the array. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# Is there a way to check if an element is a duplicate without comparing it to every other element? Maybe there's a data structure that is useful here.


# Hint 3
# We can use a hash data structure like a hash set or hash map to store elements we've already seen. This will allow us to check if an element is a duplicate in constant time.



from collections import defaultdict
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize a counter to track the occurrences of each number
        counter = defaultdict(int)
        
        # Iterate through each number in the input list
        for num in nums:
            counter[num] += 1  # Increment the count for this number
            
            # If any number appears more than once, return True
            if counter[num] > 1:
                return True
        
        # If no duplicates are found, return False
        return False

# Example test cases:
sol = Solution()

# Test case 1: Contains duplicates
nums1 = [1, 2, 3, 4, 2]
print(sol.containsDuplicate(nums1))  # Output: True

# Test case 2: No duplicates
nums2 = [1, 2, 3, 4, 5]
print(sol.containsDuplicate(nums2))  # Output: False

# Test case 3: Empty list
nums3 = []
print(sol.containsDuplicate(nums3))  # Output: False

# Test case 4: All duplicates
nums4 = [7, 7, 7, 7]
print(sol.containsDuplicate(nums4))  # Output: True
