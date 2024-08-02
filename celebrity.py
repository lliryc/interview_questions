import random
from typing import List

# The knows API is already defined for you.
def knows(a: int, b: int) -> bool:
    """
    Mock implementation of the knows API.
    In a real scenario, this would be provided externally.
    """
    if b == 9:
        return True
    if a == 9:
        return False
    return False  # random.choice([True, False])

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Find the celebrity in a group of n people.
        
        A celebrity is known by everyone but doesn't know anyone.
        
        Args:
        n (int): The number of people in the group.
        
        Returns:
        int: The index of the celebrity, or -1 if no celebrity is found.
        """
        in_degrees = [0] * n  # Number of people who know person i
        out_degrees = [0] * n  # Number of people person i knows
        unknown_relations = [False] * n  # True if person i has an unknown relation

        for i in range(n - 1):
            for j in range(i + 1, n):
                self._check_relation(i, j, n, in_degrees, out_degrees, unknown_relations)
                self._check_relation(j, i, n, in_degrees, out_degrees, unknown_relations)

        return -1

    def _check_relation(self, a: int, b: int, n: int, 
                        in_degrees: List[int], out_degrees: List[int], 
                        unknown_relations: List[bool]) -> None:
        """
        Check the relationship between two people and update their statistics.
        
        Args:
        a, b (int): Indices of the two people to check.
        n (int): Total number of people.
        in_degrees, out_degrees, unknown_relations (List[int]): Statistics lists to update.
        """
        if not unknown_relations[b] and out_degrees[b] == 0:
            if knows(a, b):
                in_degrees[b] += 1
                out_degrees[a] += 1
                if in_degrees[b] == n - 1:
                    return b
            else:
                unknown_relations[b] = True

# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_celebrity(self):
        self.assertEqual(self.solution.findCelebrity(2), -1)

    def test_celebrity_present(self):
        # Mock the knows function to make person 1 the celebrity
        global knows
        original_knows = knows
        knows = lambda a, b: b == 1 if a != 1 else False
        
        self.assertEqual(self.solution.findCelebrity(3), 1)
        
        # Restore the original knows function
        knows = original_knows

    def test_empty_group(self):
        self.assertEqual(self.solution.findCelebrity(0), -1)

if __name__ == "__main__":
    unittest.main()

# Example usage
s = Solution()
print(s.findCelebrity(2))



