
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create counters for both strings
        countS = defaultdict(int)
        countT = defaultdict(int)

        # Count occurrences of each character in string s
        for c in s:
            countS[c] += 1
        
        # Count occurrences of each character in string t
        for c in t:
            countT[c] += 1
        
        # If the two dictionaries are equal, the strings are anagrams
        return countS == countT

# Test cases
sol = Solution()

# Test case 1: Regular anagrams
print(sol.isAnagram("listen", "silent"))  # Output: True

# Test case 2: Not anagrams (different letters)
print(sol.isAnagram("hello", "bello"))    # Output: False

# Test case 3: Not anagrams (different lengths)
print(sol.isAnagram("abc", "ab"))         # Output: False

# Test case 4: Empty strings (are anagrams)
print(sol.isAnagram("", ""))              # Output: True

# Test case 5: Anagrams with repeated letters
print(sol.isAnagram("aabbcc", "abcabc"))  # Output: True

# Test case 6: Case sensitivity
print(sol.isAnagram("abc", "CBA"))        # Output: False
