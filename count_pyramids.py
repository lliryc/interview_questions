from typing import List
from functools import lru_cache

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        """
        Count the number of pyramids and inverse pyramids in the given grid.
        
        Args:
        grid (List[List[int]]): A 2D grid of 0s and 1s.
        
        Returns:
        int: The total count of pyramids and inverse pyramids.
        """
        self.grid = grid
        rows, cols = len(grid), len(grid[0])
        
        # Count normal pyramids
        normal_count = self._count_pyramids(rows, cols, self.pyramid)
        Solution.pyramid.cache_clear()
        
        # Count inverse pyramids
        inverse_count = self._count_pyramids(rows, cols, self.inv_pyramid, inverse=True)
        Solution.inv_pyramid.cache_clear()
        
        return normal_count + inverse_count

    def _count_pyramids(self, rows: int, cols: int, pyramid_func, inverse: bool = False) -> int:
        """
        Helper method to count pyramids or inverse pyramids.
        
        Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        pyramid_func (function): Function to check for pyramid or inverse pyramid.
        inverse (bool): Whether to count inverse pyramids.
        
        Returns:
        int: The count of pyramids or inverse pyramids.
        """
        count = 0
        range_start = 1 if not inverse else rows - 2
        range_end = rows if not inverse else -1
        range_step = 1 if not inverse else -1
        
        for i in range(range_start, range_end, range_step):
            pos = None
            for j in range(cols):
                if self.grid[i][j] == 1:
                    if pos is None:
                        pos = j
                    length = j - pos + 1
                    if length >= 3:
                        length = length - 1 if length % 2 == 0 else length
                        max_height = 2 * i + 1 if not inverse else 2 * (rows - 1 - i) + 1
                        for k in range(min(length, max_height), 1, -2):
                            count += int(pyramid_func(i, j, k))
                else:
                    pos = None
        return count

    @lru_cache
    def pyramid(self, i: int, j: int, l: int) -> bool:
        """
        Check if there's a pyramid of length l with its base at (i, j).
        
        Args:
        i (int): Row index of the pyramid's base center.
        j (int): Column index of the pyramid's base center.
        l (int): Length of the pyramid's base.
        
        Returns:
        bool: True if a pyramid exists, False otherwise.
        """
        if l == 1:
            return self.grid[i][j] == 1
        return self.pyramid(i, j, l - 2) and self.pyramid(i - 1, j - 1, l - 2)

    @lru_cache
    def inv_pyramid(self, i: int, j: int, l: int) -> bool:
        """
        Check if there's an inverse pyramid of length l with its base at (i, j).
        
        Args:
        i (int): Row index of the inverse pyramid's base center.
        j (int): Column index of the inverse pyramid's base center.
        l (int): Length of the inverse pyramid's base.
        
        Returns:
        bool: True if an inverse pyramid exists, False otherwise.
        """
        if l == 1:
            return self.grid[i][j] == 1
        return self.inv_pyramid(i, j, l - 2) and self.inv_pyramid(i + 1, j - 1, l - 2)

# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        grid = [[0,1,1],[1,1,1],[1,0,1],[1,1,1]]
        self.assertEqual(self.sol.countPyramids(grid), 4)

    def test_example_2(self):
        grid = [[1,1,1],[1,1,1]]
        self.assertEqual(self.sol.countPyramids(grid), 2)

    def test_example_3(self):
        grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]
        self.assertEqual(self.sol.countPyramids(grid), 13)

    def test_empty_grid(self):
        grid = [[]]
        self.assertEqual(self.sol.countPyramids(grid), 0)

    def test_single_cell(self):
        grid = [[1]]
        self.assertEqual(self.sol.countPyramids(grid), 0)

    def test_no_pyramids(self):
        grid = [[1,0,1],[0,1,0],[1,0,1]]
        self.assertEqual(self.sol.countPyramids(grid), 0)

if __name__ == "__main__":
    unittest.main()


