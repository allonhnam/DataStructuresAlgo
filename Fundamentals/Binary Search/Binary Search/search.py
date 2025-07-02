from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)  # right is exclusive

        while l < r:
            m = l + ((r - l) // 2)  # avoid overflow
            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return l - 1 if (l and nums[l - 1] == target) else -1

# Test case 1
nums = [-1, 0, 2, 4, 6, 8]
target = 4
sol = Solution()
print(sol.search(nums, target))  # Expected: 3

# Test case 2
nums = [-1, 0, 2, 4, 6, 8]
target = 3
sol = Solution()
print(sol.search(nums, target))  # Expected: -1
