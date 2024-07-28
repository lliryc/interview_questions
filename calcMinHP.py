import unittest

class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        Calculate the minimum initial health needed to rescue the princess.
        
        Args:
        dungeon (List[List[int]]): A 2D grid representing the dungeon.
        
        Returns:
        int: The minimum initial health required.
        """
        if not dungeon or not dungeon[0]:
            return 1
        
        m, n = len(dungeon), len(dungeon[0])
        
        # Initialize dp table with infinity
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        
        # Set base cases
        dp[m][n-1] = dp[m-1][n] = 1
        
        # Fill dp table from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        
        return dp[0][0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_dungeon(self):
        dungeon = [[-2, -3, 3],
                   [-5, -10, 1],
                   [10, 30, -5]]
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 7)

    def test_empty_dungeon(self):
        self.assertEqual(self.solution.calculateMinimumHP([]), 1)

    def test_single_cell_positive(self):
        self.assertEqual(self.solution.calculateMinimumHP([[5]]), 1)

    def test_single_cell_negative(self):
        self.assertEqual(self.solution.calculateMinimumHP([[-5]]), 6)

    def test_all_positive(self):
        dungeon = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 1)

    def test_all_negative(self):
        dungeon = [[-1, -2, -3],
                   [-4, -5, -6],
                   [-7, -8, -9]]
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 21)


if __name__ == "__main__":
    unittest.main()
