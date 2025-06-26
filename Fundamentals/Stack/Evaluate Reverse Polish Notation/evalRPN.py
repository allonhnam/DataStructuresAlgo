from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        Supported operators: +, -, *, /
        Division truncates toward zero.
        """
        stack = []

        for c in tokens:
            if c == "+":
                # Pop two operands and add
                right = stack.pop()
                left = stack.pop()
                result = left + right
                stack.append(result)
            elif c == "-":
                # Pop two operands: left - right
                right = stack.pop()
                left = stack.pop()
                result = left - right
                stack.append(result)
            elif c == "*":
                # Pop two operands and multiply
                right = stack.pop()
                left = stack.pop()
                result = left * right
                stack.append(result)
            elif c == "/":
                # Pop two operands: left / right, truncate toward zero
                right = stack.pop()
                left = stack.pop()
                result = int(float(left) / right)
                stack.append(result)
            else:
                # It's a number; convert to int and push onto stack
                stack.append(int(c))

        # The final result is the only element remaining on the stack
        return stack[0]

# Example 1
tokens = ["1","2","+","3","*","4","-"]
sol = Solution()
output = sol.evalRPN(tokens)
print("Input tokens:", tokens)
print("Output:", output)
