import unittest

def distribute_candies(ratings):
    """
    Distribute candies to children based on their ratings.

    Rules:
    1. Each child must have at least one candy.
    2. Children with a higher rating get more candies than their adjacent neighbors.

    Args:
    ratings (list): A list of integers representing the ratings of children.

    Returns:
    int: The minimum total number of candies needed.
    """
    n = len(ratings)
    if n == 0:
        return 0
    if n == 1:
        return 1

    candies = [1] * n

    # Forward pass: compare with left neighbor
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    # Backward pass: compare with right neighbor and update if necessary
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1

    return sum(candies)


class TestDistributeCandies(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(distribute_candies([]), 0)

    def test_single_child(self):
        self.assertEqual(distribute_candies([1]), 1)

    def test_two_children_same_rating(self):
        self.assertEqual(distribute_candies([1, 1]), 2)

    def test_two_children_different_rating(self):
        self.assertEqual(distribute_candies([1, 2]), 3)

    def test_increasing_ratings(self):
        self.assertEqual(distribute_candies([1, 2, 3, 4, 5]), 15)

    def test_decreasing_ratings(self):
        self.assertEqual(distribute_candies([5, 4, 3, 2, 1]), 15)

    def test_mixed_ratings(self):
        self.assertEqual(distribute_candies([1, 0, 2]), 5)
        self.assertEqual(distribute_candies([1, 2, 2]), 4)
        self.assertEqual(distribute_candies([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]), 19)
        self.assertEqual(distribute_candies([1, 3, 4, 5, 2]), 11)

    def test_all_same_ratings(self):
        self.assertEqual(distribute_candies([1, 1, 1, 1, 1]), 5)


if __name__ == '__main__':
    unittest.main()
