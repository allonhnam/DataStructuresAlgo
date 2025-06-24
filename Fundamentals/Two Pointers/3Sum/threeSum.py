from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array to use two-pointer technique efficiently

        for i, a in enumerate(nums):
            # Skip duplicate values for the first number to avoid repeated triplets
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1  # Set left and right pointers

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1  # If sum too big, move right pointer left
                elif threeSum < 0:
                    l += 1  # If sum too small, move left pointer right
                else:
                    # Found a triplet that sums to zero
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res  # Return all unique triplets that sum to 0

# --- Example 1 ---
nums1 = [-1, 0, 1, 2, -1, -4]
print("Example 1 Output:", Solution().threeSum(nums1))
# Expected: [[-1, -1, 2], [-1, 0, 1]]

# --- Example 2 ---
nums2 = [0, 1, 1]
print("Example 2 Output:", Solution().threeSum(nums2))
# Expected: []

# --- Example 3 ---
nums3 = [0, 0, 0]
print("Example 3 Output:", Solution().threeSum(nums3))
# Expected: [[0, 0, 0]]
