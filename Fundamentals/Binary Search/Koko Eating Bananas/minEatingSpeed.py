from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p / k)

            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

# Example 1
piles = [1,4,3,2]
h = 9
sol = Solution()
print(sol.minEatingSpeed(piles, h))  # Expected: 2

# Example 2
piles = [25,10,23,4]
h = 4
sol = Solution()
print(sol.minEatingSpeed(piles, h))  # Expected: 25
