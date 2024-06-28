class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        Determines the minimum number of characters to append to the end of string s 
        to make t a subsequence of s.

        Args:
        s (str): The source string.
        t (str): The target subsequence string.

        Returns:
        int: The minimum number of characters to append.
        """
        # Initialize positions for both strings
        spos = 0
        tpos = 0

        # Traverse through the source string s
        while spos < len(s):
            # If characters match, move the pointer of t
            if tpos < len(t) and s[spos] == t[tpos]:
                tpos += 1
            # Move the pointer of s
            spos += 1

        # The result is the remaining characters in t that haven't been matched
        return len(t) - tpos

# Example usage:
sol = Solution()
print(sol.appendCharacters("coaching", "coding"))  # Output: 4
