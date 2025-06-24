class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        # Step 1: Filter out non-alphanumeric characters and convert to lowercase
        for c in s:
            if c.isalnum():
                res += c.lower()  # Normalize the string to lowercase and remove spaces/punctuation
        
        # Step 2: Use two-pointer technique to compare characters from both ends
        l, r = 0, len(res) - 1

        while l < r:
            if res[l] != res[r]:  # If mismatch found, it's not a palindrome
                return False
            l += 1
            r -= 1
        
        return True  # If all characters matched, it is a palindrome


# Example 1
s1 = "Was it a car or a cat I saw?"
# After filtering: "wasitacaroracatisaw" -> This is a palindrome
print(Solution().isPalindrome(s1))  # Output: True

# Example 2
s2 = "tab a cat"
# After filtering: "tabacat" -> This is NOT a palindrome
print(Solution().isPalindrome(s2))  # Output: False
