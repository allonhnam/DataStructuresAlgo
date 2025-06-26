import json

class MinStack:
    def __init__(self):
        # Main stack to store all values
        self.stack = []
        # Auxiliary stack to track the minimum value at each level
        self.minStack = []

    def push(self, val: int) -> None:
        # Always push the new value onto the main stack
        self.stack.append(val)
        # Determine the new minimum: either the new value or the previous minimum
        current_min = min(val, self.minStack[-1] if self.minStack else val)
        # Push the current minimum onto the auxiliary stack
        self.minStack.append(current_min)

    def pop(self) -> None:
        # Pop from both stacks to keep them in sync
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum (top of minStack)
        return self.minStack[-1]

# Run the sequence of operations and collect outputs
outputs = []
ms = MinStack()     # constructor, returns None
outputs.append(None)

ms.push(1)          # push 1, returns None
outputs.append(None)
ms.push(2)          # push 2, returns None
outputs.append(None)
ms.push(0)          # push 0, returns None
outputs.append(None)

# getMin() -> 0
outputs.append(ms.getMin())

ms.pop()            # pop top (0), returns None
outputs.append(None)

# top() -> 2
outputs.append(ms.top())
# getMin() -> 1
outputs.append(ms.getMin())

# Print the outputs in JSON format (None -> null)
print(json.dumps(outputs))
