from typing import List

class Solution:
    """
    A class to solve the problem of counting the number of clean rooms
    that a robot can clean given a room layout.
    """

    # Direction constants
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        """
        Counts the number of clean rooms after the robot has finished cleaning.

        Args:
            room (List[List[int]]): A 2D grid representing the room layout.
                                    0: empty space, 1: obstacle

        Returns:
            int: The number of clean rooms.
        """
        self.m, self.n = len(room), len(room[0])
        self.room = room
        self.clean_rooms = 0
        self.visited = [[[False for _ in range(4)] for _ in range(self.n)] for _ in range(self.m)]
        
        self._clean(0, 0, self.EAST)
        return self.clean_rooms

    def _clean(self, row: int, col: int, direction: int) -> None:
        """
        Recursive function to simulate the robot's cleaning process.

        Args:
            row (int): Current row position of the robot.
            col (int): Current column position of the robot.
            direction (int): Current direction the robot is facing.
        """
        while True:
            if self.visited[row][col][direction]:
                return

            self.visited[row][col][direction] = True
            if self.room[row][col] == 0:
                self.clean_rooms += 1
                self.room[row][col] = 2  # Mark as cleaned

            for _ in range(4):  # Try all 4 directions
                next_row, next_col = self._get_next_position(row, col, direction)
                if self._is_valid_move(next_row, next_col):
                    row, col = next_row, next_col
                    break
                direction = (direction + 1) % 4
            else:  # If no valid move found in any direction
                return

    def _get_next_position(self, row: int, col: int, direction: int) -> tuple:
        """
        Calculates the next position based on the current position and direction.

        Args:
            row (int): Current row position.
            col (int): Current column position.
            direction (int): Current direction.

        Returns:
            tuple: Next (row, col) position.
        """
        if direction == self.EAST:
            return row, col + 1
        elif direction == self.SOUTH:
            return row + 1, col
        elif direction == self.WEST:
            return row, col - 1
        elif direction == self.NORTH:
            return row - 1, col

    def _is_valid_move(self, row: int, col: int) -> bool:
        """
        Checks if the given position is a valid move.

        Args:
            row (int): Row to check.
            col (int): Column to check.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return (0 <= row < self.m and 0 <= col < self.n and self.room[row][col] != 1)


# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_room(self):
        room = [[0]]
        self.assertEqual(self.solution.numberOfCleanRooms(room), 1)

    def test_single_obstacle(self):
        room = [[0, 1], [0, 0]]
        self.assertEqual(self.solution.numberOfCleanRooms(room), 3)

    def test_multiple_obstacles(self):
        room = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
        self.assertEqual(self.solution.numberOfCleanRooms(room), 5)

    def test_no_clean_rooms(self):
        room = [[1]]
        self.assertEqual(self.solution.numberOfCleanRooms(room), 0)

    def test_complex_room(self):
        room = [
            [0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(self.solution.numberOfCleanRooms(room), 13)

if __name__ == "__main__":
    unittest.main()


