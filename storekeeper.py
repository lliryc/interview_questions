from typing import List, Tuple
from collections import deque

class Solution:
    """
    Solution class for the 'Push Box' problem.
    """

    def minPushBox(self, grid: List[List[str]]) -> int:
        """
        Find the minimum number of pushes to move the box to the target.

        Args:
            grid (List[List[str]]): The game grid represented as a 2D list.

        Returns:
            int: Minimum number of pushes required, or -1 if impossible.
        """
        man_loc, box_loc = self._find_start_positions(grid)
        if man_loc is None or box_loc is None:
            return -1

        moves = self._bfs(man_loc, box_loc, grid)
        return moves if moves != float('inf') else -1

    def _find_start_positions(self, grid: List[List[str]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        Find the starting positions of the man and the box in the grid.

        Args:
            grid (List[List[str]]): The game grid.

        Returns:
            Tuple[Tuple[int, int], Tuple[int, int]]: Man and box positions.
        """
        man_loc, box_loc = None, None
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 'S':
                    man_loc = (x, y)
                    grid[y][x] = '.'
                elif cell == 'B':
                    box_loc = (x, y)
                    grid[y][x] = '.'
                if man_loc and box_loc:
                    return man_loc, box_loc
        return man_loc, box_loc

    def _bfs(self, man_loc: Tuple[int, int], box_loc: Tuple[int, int], grid: List[List[str]]) -> int:
        """
        Perform a breadth-first search to find the minimum number of pushes.

        Args:
            man_loc (Tuple[int, int]): Initial man position.
            box_loc (Tuple[int, int]): Initial box position.
            grid (List[List[str]]): The game grid.

        Returns:
            int: Minimum number of pushes required.
        """
        shape = (len(grid), len(grid[0]))
        queue = deque([(man_loc, box_loc)])
        visited = {(man_loc, box_loc): 0}
        min_pushes = float('inf')

        while queue:
            man_loc, box_loc = queue.popleft()
            pushes = visited[(man_loc, box_loc)]

            # Try to move the box
            min_pushes = self._try_move_box(man_loc, box_loc, grid, shape, queue, visited, pushes, min_pushes)

            # Move the man
            self._move_man(man_loc, box_loc, grid, shape, queue, visited, pushes)

        return min_pushes

    def _try_move_box(self, man_loc: Tuple[int, int], box_loc: Tuple[int, int], grid: List[List[str]],
                      shape: Tuple[int, int], queue: deque, visited: dict, pushes: int, min_pushes: int) -> int:
        """
        Attempt to move the box and update the minimum pushes if successful.

        Args:
            man_loc (Tuple[int, int]): Current man position.
            box_loc (Tuple[int, int]): Current box position.
            grid (List[List[str]]): The game grid.
            shape (Tuple[int, int]): Grid dimensions.
            queue (deque): BFS queue.
            visited (dict): Visited states.
            pushes (int): Current number of pushes.
            min_pushes (int): Current minimum pushes.

        Returns:
            int: Updated minimum pushes.
        """
        if self._manhattan_distance(man_loc, box_loc) != 1:
            return min_pushes

        push_direction = (box_loc[0] - man_loc[0], box_loc[1] - man_loc[1])
        new_box_loc = self._add_tuples(box_loc, push_direction)

        if self._is_valid_move(new_box_loc, grid, shape):
            new_state = (box_loc, new_box_loc)
            new_pushes = pushes + 1

            if new_state not in visited or visited[new_state] > new_pushes:
                visited[new_state] = new_pushes
                queue.append(new_state)

                if grid[new_box_loc[1]][new_box_loc[0]] == 'T':
                    min_pushes = min(min_pushes, new_pushes)

        return min_pushes

    def _move_man(self, man_loc: Tuple[int, int], box_loc: Tuple[int, int], grid: List[List[str]],
                  shape: Tuple[int, int], queue: deque, visited: dict, pushes: int):
        """
        Move the man to adjacent positions.

        Args:
            man_loc (Tuple[int, int]): Current man position.
            box_loc (Tuple[int, int]): Current box position.
            grid (List[List[str]]): The game grid.
            shape (Tuple[int, int]): Grid dimensions.
            queue (deque): BFS queue.
            visited (dict): Visited states.
            pushes (int): Current number of pushes.
        """
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_man_loc = self._add_tuples(man_loc, move)

            if new_man_loc == box_loc:
                continue

            if self._is_valid_move(new_man_loc, grid, shape):
                new_state = (new_man_loc, box_loc)

                if new_state not in visited or visited[new_state] > pushes:
                    visited[new_state] = pushes
                    queue.append(new_state)

    @staticmethod
    def _is_valid_move(pos: Tuple[int, int], grid: List[List[str]], shape: Tuple[int, int]) -> bool:
        """
        Check if a move to the given position is valid.

        Args:
            pos (Tuple[int, int]): Position to check.
            grid (List[List[str]]): The game grid.
            shape (Tuple[int, int]): Grid dimensions.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return (0 <= pos[0] < shape[1] and 0 <= pos[1] < shape[0] and
                grid[pos[1]][pos[0]] in ['.', 'T'])

    @staticmethod
    def _manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        """
        Calculate the Manhattan distance between two points.

        Args:
            p1 (Tuple[int, int]): First point.
            p2 (Tuple[int, int]): Second point.

        Returns:
            int: Manhattan distance.
        """
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @staticmethod
    def _add_tuples(t1: Tuple[int, int], t2: Tuple[int, int]) -> Tuple[int, int]:
        """
        Add two tuples element-wise.

        Args:
            t1 (Tuple[int, int]): First tuple.
            t2 (Tuple[int, int]): Second tuple.

        Returns:
            Tuple[int, int]: Result of addition.
        """
        return (t1[0] + t2[0], t1[1] + t2[1])

# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_case(self):
        grid = [
            ["#","#","#","#","#","#"],
            ["#","T","#","#","#","#"],
            ["#",".",".","B",".","#"],
            ["#",".","#","#",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]
        ]
        self.assertEqual(self.solution.minPushBox(grid), 3)

    def test_impossible_case(self):
        grid = [
            ["#","#","#","#","#","#"],
            ["#","T","#","#","#","#"],
            ["#","#","#","B",".","#"],
            ["#","#","#","#",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]
        ]
        self.assertEqual(self.solution.minPushBox(grid), -1)

    def test_no_moves_needed(self):
        grid = [
            ["#","#","#"],
            ["#","T","#"],
            ["#","B","#"],
            ["#","S","#"],
            ["#","#","#"]
        ]
        self.assertEqual(self.solution.minPushBox(grid), 1)

    def test_complex_case(self):
        grid = [
            ["#",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".","#",".",".",".","#"],
            ["#",".","#",".",".","T",".",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".","#",".",".","."],
            [".",".",".","#","#","S",".","B",".","."],
            ["#",".",".",".",".",".",".","#",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".","#",".",".",".","."]
        ]
        self.assertEqual(self.solution.minPushBox(grid), 5)

if __name__ == "__main__":
    unittest.main()
