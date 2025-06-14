from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Append the length of the string, a separator '#', and the string itself
            # This ensures we know where each string starts and ends during decoding
            res += str(len(s)) + "#" + s
        return res  # Returns a single encoded string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Find the position of '#' to get the length prefix
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Extract length of the next string
            i = j + 1             # Move past the '#' character
            j = i + length        # j now points to the end of the current string
            res.append(s[i:j])    # Extract and append the string to result
            i = j                 # Move to the start of the next encoded string
        return res  # Returns the list of original strings

sol = Solution()

# Test case 1: Simple strings
input1 = ["hello", "world"]
encoded1 = sol.encode(input1)
decoded1 = sol.decode(encoded1)
print("Encoded:", encoded1)
print("Decoded:", decoded1)

# Test case 2: Empty strings
input2 = ["", "test", ""]
encoded2 = sol.encode(input2)
decoded2 = sol.decode(encoded2)
print("Encoded:", encoded2)
print("Decoded:", decoded2)

# Test case 3: Strings with special characters
input3 = ["a#b#c", "123#456", "##"]
encoded3 = sol.encode(input3)
decoded3 = sol.decode(encoded3)
print("Encoded:", encoded3)
print("Decoded:", decoded3)

# Test case 4: Strings with spaces
input4 = ["", " ", "   ", "space bar"]
encoded4 = sol.encode(input4)
decoded4 = sol.decode(encoded4)
print("Encoded:", encoded4)
print("Decoded:", decoded4)
