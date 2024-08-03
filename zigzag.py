class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert the input string into a zigzag pattern and return the result.

        Args:
        s (str): The input string to be converted.
        numRows (int): The number of rows in the zigzag pattern.

        Returns:
        str: The string read line by line after being written in a zigzag pattern.
        """
        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize rows
        rows = [''] * numRows
        
        current_row = 0
        step = 1

        for char in s:
            rows[current_row] += char
            
            # Change direction if we're at the top or bottom row
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
            
            current_row += step

        # Join all rows and return
        return ''.join(rows)


# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_normal_case(self):
        self.assertEqual(self.solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(self.solution.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_single_row(self):
        self.assertEqual(self.solution.convert("PAYPALISHIRING", 1), "PAYPALISHIRING")

    def test_two_rows(self):
        self.assertEqual(self.solution.convert("ABCDEF", 2), "ACEBDF")

    def test_num_rows_greater_than_string_length(self):
        self.assertEqual(self.solution.convert("ABC", 5), "ABC")

    def test_empty_string(self):
        self.assertEqual(self.solution.convert("", 3), "")

if __name__ == "__main__":
    unittest.main()
