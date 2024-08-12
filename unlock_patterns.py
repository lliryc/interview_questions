from typing import List, Set
from collections import defaultdict

class Solution:
    """
    Solution class for counting the number of valid Android lock patterns.
    """

    def __init__(self):
        """
        Initialize the Solution class with skip patterns and counters.
        """
        self.m = 0
        self.n = 0
        self.skip = defaultdict(int)
        self._initialize_skip_patterns()

    def _initialize_skip_patterns(self):
        """
        Initialize the skip patterns for the Android lock.
        """
        skip_pairs = [
            (1, 3), (1, 7), (3, 9), (7, 9),
            (2, 8), (4, 6), (1, 9), (3, 7)
        ]
        for start, end in skip_pairs:
            self.skip[(start, end)] = self.skip[(end, start)] = 1

    def numberOfPatterns(self, m: int, n: int) -> int:
        """
        Count the number of valid Android lock patterns.

        Args:
            m (int): Minimum number of keys to use.
            n (int): Maximum number of keys to use.

        Returns:
            int: The total number of valid patterns.
        """
        self.m, self.n = m, n
        digits = set(range(1, 10))
        
        return (
            self.dfs(1, digits, 1) * 4 +  # Patterns starting from corners
            self.dfs(2, digits, 1) * 4 +  # Patterns starting from edges
            self.dfs(5, digits, 1)        # Patterns starting from center
        )

    def dfs(self, current: int, available: Set[int], length: int) -> int:
        """
        Perform depth-first search to count valid patterns.

        Args:
            current (int): Current key in the pattern.
            available (Set[int]): Set of available keys.
            length (int): Current length of the pattern.

        Returns:
            int: Number of valid patterns from the current state.
        """
        if length == self.n:
            return 1

        count = int(length >= self.m)  # Count current pattern if it meets minimum length
        available.remove(current)

        for next_key in list(available):
            if self.skip[(current, next_key)] == 0 or (current + next_key) // 2 in available:
                count += self.dfs(next_key, available, length + 1)

        available.add(current)
        return count


def test_solution():
    """
    Unit tests for the Solution class.
    """
    s = Solution()
    
    assert s.numberOfPatterns(1, 1) == 9, "Test case 1 failed"
    assert s.numberOfPatterns(1, 2) == 65, "Test case 2 failed"
    assert s.numberOfPatterns(1, 3) == 385, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
