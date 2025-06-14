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
