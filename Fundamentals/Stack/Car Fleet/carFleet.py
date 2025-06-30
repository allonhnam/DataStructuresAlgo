from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine positions and speeds
        pair = [(p, s) for p, s in zip(position, speed)]
        # Sort cars by position descending (closer to target first)
        pair.sort(reverse=True)

        stack = []  # Stack to keep track of fleet arrival times

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)

            # If the current car catches up with the fleet ahead, merge into that fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    target1 = 10
    position1 = [1, 4]
    speed1 = [3, 2]
    output1 = solution.carFleet(target1, position1, speed1)
    print(f"Input: target = {target1}, position = {position1}, speed = {speed1}")
    print(f"Output: {output1}")
    # Expected: 1

    # Example 2
    target2 = 10
    position2 = [4, 1, 0, 7]
    speed2 = [2, 2, 1, 1]
    output2 = solution.carFleet(target2, position2, speed2)
    print(f"Input: target = {target2}, position = {position2}, speed = {speed2}")
    print(f"Output: {output2}")
    # Expected: 3
