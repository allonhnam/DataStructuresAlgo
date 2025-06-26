class Solution:
    def isValid(self, s: str) -> bool:
        # mapping closing brackets to their corresponding opening brackets
        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        # stack to keep track of opening brackets encountered
        stack = []
        
        # iterate through each character in the string
        for c in s:
            if c in bracket_map:
                # if it's a closing bracket, check if top of the stack matches the expected opening bracket
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()  # matched pair, pop the opening bracket
                else:
                    return False  # mismatch or stack is empty (no opening bracket to match)
            else:
                # it's an opening bracket, push it onto the stack
                stack.append(c)
        
        # if stack is empty, every opening bracket had a matching closing bracket
        return not stack

# Running the provided examples
sol = Solution()

examples = [
    ("[]", True),
    ("([{}])", True),
    ("[(])", False)
]

for s, expected in examples:
    result = sol.isValid(s)
    print(f"Input: {s!r}")
    print(f"Expected: {expected}, Got: {result}")
    print("---")