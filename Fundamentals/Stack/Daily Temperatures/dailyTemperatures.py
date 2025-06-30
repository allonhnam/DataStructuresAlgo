from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # Initialize result list with 0s
        stack = []  # Stack to store (temperature, index) pairs

        for i, t in enumerate(temperatures):
            # If current temp is warmer than the one at the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # Record how many days until a warmer temperature
                res[stackInd] = i - stackInd
            # Push current temp and its index onto the stack
            stack.append((t, i))

        return res  # Any index left in stack has no warmer day ahead → remains 0

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    temperatures1 = [30, 38, 30, 36, 35, 40, 28]
    output1 = solution.dailyTemperatures(temperatures1)
    print(f"Input: {temperatures1}")
    print(f"Output: {output1}")
    # Expected: [1, 4, 1, 2, 1, 0, 0]

    # Example 2
    temperatures2 = [22, 21, 20]
    output2 = solution.dailyTemperatures(temperatures2)
    print(f"Input: {temperatures2}")
    print(f"Output: {output2}")
    # Expected: [0, 0, 0]
