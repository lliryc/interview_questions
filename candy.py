from typing import List
import unittest

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Distribute candies to children based on their ratings.

        Rules:
        1. Each child must have at least one candy.
        2. Children with a higher rating get more candies than their adjacent neighbors.

        Args:
        ratings (List[int]): A list of integers representing the ratings of children.

        Returns:
        int: The minimum total number of candies needed.
        """
        n = len(ratings)
        if n == 1:
            return 1
        if n == 2:
            return 3 if ratings[0] != ratings[1] else 2

        candies = [None] * n
        nodes = []

        # Identify local minima
        if ratings[0] <= ratings[1]:
            nodes.append((0, 1))
        if ratings[n-1] <= ratings[n-2]:
            nodes.append((n-1, 1))
        for i in range(1, n-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                nodes.append((i, 1))

        # Distribute candies from local minima
        while nodes:
            new_nodes = []
            for i, c in nodes:
                candies[i] = c
                if i > 0 and ratings[i-1] > ratings[i] and (candies[i-1] is None or candies[i-1] <= c):
                    new_nodes.append((i-1, c+1))
                if i < n-1 and ratings[i+1] > ratings[i] and (candies[i+1] is None or candies[i+1] <= c):
                    new_nodes.append((i+1, c+1))
            nodes = new_nodes

        return sum(candies)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_child(self):
        self.assertEqual(self.solution.candy([1]), 1)

    def test_two_children_same_rating(self):
        self.assertEqual(self.solution.candy([1, 1]), 2)

    def test_two_children_different_rating(self):
        self.assertEqual(self.solution.candy([1, 2]), 3)

    def test_increasing_ratings(self):
        self.assertEqual(self.solution.candy([1, 2, 3, 4, 5]), 15)

    def test_decreasing_ratings(self):
        self.assertEqual(self.solution.candy([5, 4, 3, 2, 1]), 15)

    def test_mixed_ratings(self):
        self.assertEqual(self.solution.candy([1, 0, 2]), 5)
        self.assertEqual(self.solution.candy([1, 2, 2]), 4)
        self.assertEqual(self.solution.candy([1, 3, 2, 2, 1]), 7)
        self.assertEqual(self.solution.candy([1, 2, 87, 87, 87, 2, 1]), 13)

    def test_all_same_ratings(self):
        self.assertEqual(self.solution.candy([1, 1, 1, 1, 1]), 5)


if __name__ == '__main__':
    unittest.main()

