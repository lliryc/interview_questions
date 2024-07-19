from typing import List
import itertools

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        """
        Perform brace expansion on the given expression.

        :param expression: A string containing the expression to expand.
        :return: A sorted list of unique strings generated from the expansion.
        """
        # Initialize groups to collect parts of the expression and level to track nested braces
        groups = [[]]
        level = 0
        
        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i + 1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])
        
        # Use set to store unique words
        word_set = set()
        for group in groups:
            word_set |= set(map(''.join, itertools.product(*group)))
        
        # Return sorted list of unique words
        return sorted(word_set)

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    expression1 = "{a,b}{c,{d,e}}"
    expected_output1 = ["ac", "ad", "ae", "bc", "bd", "be"]
    assert solution.braceExpansionII(expression1) == expected_output1, f"Test case 1 failed: expected {expected_output1}, got {solution.braceExpansionII(expression1)}"
    print(f"Test case 1 passed: {solution.braceExpansionII(expression1)} == {expected_output1}")

    # Test case 2
    expression2 = "{{a,z},a{b,c},{ab,z}}"
    expected_output2 = ["a", "ab", "ac", "z"]
    assert solution.braceExpansionII(expression2) == expected_output2, f"Test case 2 failed: expected {expected_output2}, got {solution.braceExpansionII(expression2)}"
    print(f"Test case 2 passed: {solution.braceExpansionII(expression2)} == {expected_output2}")

    # Test case 3
    expression3 = "{ac,b}{c,{d,e}}"
    expected_output3 = ["acc", "acd", "ace", "bc", "bd", "be"]
    assert solution.braceExpansionII(expression3) == expected_output3, f"Test case 3 failed: expected {expected_output3}, got {solution.braceExpansionII(expression3)}"
    print(f"Test case 3 passed: {solution.braceExpansionII(expression3)} == {expected_output3}")


