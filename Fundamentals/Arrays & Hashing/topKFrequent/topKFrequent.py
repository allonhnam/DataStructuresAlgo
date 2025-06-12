import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)  # Count the frequency of each number

        for key, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))        # Push (frequency, number)
            else:
                heapq.heappushpop(heap, (val, key))     # If heap is full, pushpop (min-heap keeps k most frequent)
        
        return [h[1] for h in heap]  # Extract just the numbers from the heap


sol = Solution()

# Example 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(sol.topKFrequent(nums1, k1))  # Output: [2, 1] or [1, 2]

# Example 2
nums2 = [1]
k2 = 1
print(sol.topKFrequent(nums2, k2))  # Output: [1]

# Example 3
nums3 = [4, 4, 4, 6, 6, 7, 8, 8, 8, 8]
k3 = 2
print(sol.topKFrequent(nums3, k3))  # Output: [4, 8] or [8, 4]

# Example 4
nums4 = [5, 5, 5, 6, 6, 7, 7, 7, 8, 8]
k4 = 3
print(sol.topKFrequent(nums4, k4))  # Output: [5, 7, 6] (order can vary)