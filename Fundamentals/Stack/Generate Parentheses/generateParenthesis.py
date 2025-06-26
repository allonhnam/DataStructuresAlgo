class Solution:
    def generateParenthesis(self, n):
        """
        Generate all combinations of n pairs of well-formed parentheses.
        Uses dynamic programming by building up from smaller numbers of pairs.
        """
        # res[k] will hold all valid combinations for k pairs of parentheses
        res = [[] for _ in range(n + 1)]
        # Base case: with 0 pairs, there's one valid combination: the empty string
        res[0] = [""]

        # Build results for k = 1 to n
        for k in range(1, n + 1):
            # Split k pairs into:
            # - i pairs inside the first "(" ")" pair
            # - (k - i - 1) pairs after that pair
            for i in range(k):
                for left in res[i]:  # all combinations for i pairs inside
                    for right in res[k - i - 1]:  # all combinations for remaining pairs
                        # Form a new combination by wrapping 'left' in parentheses,
                        # then appending the 'right' part.
                        res[k].append(f"({left}){right}")

        return res[n]


# Instantiate and test the solution
sol = Solution()

# Example 1
print("Input: n = 1")
print("Output:", sol.generateParenthesis(1))

# Example 2
print("\nInput: n = 3")
print("Output:", sol.generateParenthesis(3))
