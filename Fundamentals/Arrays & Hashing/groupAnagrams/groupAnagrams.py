from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # key: character count tuple, value: list of anagrams

        for str in strs:
            count = [0] * 26  # Initialize frequency count for 26 letters (a-z)

            for char in str:
                # Map each character to an index and increment its count
                count[ord(char) - ord('a')] += 1

            # Use the character count tuple as a key (e.g., (1,0,0,...,1) for "ab")
            res[tuple(count)].append(str)

        # Return the grouped anagrams as a list of lists
        return list(res.values())

# Test cases
sol = Solution()

# Example 1
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs1))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Example 2
strs2 = [""]
print(sol.groupAnagrams(strs2))  # [['']]

# Example 3
strs3 = ["a"]
print(sol.groupAnagrams(strs3))  # [['a']]

# Example 4
strs4 = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
print(sol.groupAnagrams(strs4))  # [['abc', 'bca', 'cab'], ['xyz', 'zyx', 'yxz']]
