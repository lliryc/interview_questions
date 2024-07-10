class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Compare two strings s and t to determine if they are equal after processing backspace characters ('#').
        
        Args:
        s (str): The first input string.
        t (str): The second input string.
        
        Returns:
        bool: True if the processed versions of s and t are equal, False otherwise.
        """
        return self.processed(s) == self.processed(t)

    def processed(self, s: str) -> str:
        """
        Process the input string to simulate the effect of backspace characters ('#').
        
        Args:
        s (str): The input string to process.
        
        Returns:
        str: The processed string after applying all backspaces.
        """
        res = []
        for c in s:
            if c == "#":
                if res:
                    res.pop()  # Remove the last character if backspace is encountered
            else:
                res.append(c)  # Add the character to the result list
        return "".join(res)  # Join the list into a final string

if __name__ == "__main__":
    s = Solution()
    # Test cases
    print(s.backspaceCompare("ab#c", "ad#c") == True)  # Both strings become "ac"
    print(s.backspaceCompare("ab##", "c#d#") == True)  # Both strings become ""
    print(s.backspaceCompare("a##c", "#a#c") == True)  # Both strings become "c"
    print(s.backspaceCompare("a#c", "b") == False)    # "a#c" becomes "c", "b" stays "b"


