class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # Compute left products
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        
        # Compute right products and multiply
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res

sol = Solution()

print(sol.productExceptSelf([1, 2, 3, 4]))       # Output: [24, 12, 8, 6]
print(sol.productExceptSelf([2, 3, 4, 5]))       # Output: [60, 40, 30, 24]
print(sol.productExceptSelf([1, 0, 3, 0]))       # Output: [0, 0, 0, 0]
print(sol.productExceptSelf([0, 1, 2, 3]))       # Output: [6, 0, 0, 0]
print(sol.productExceptSelf([5]))                # Output: [1]
