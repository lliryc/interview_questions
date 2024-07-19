class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Compute the bitwise AND of all numbers in the range [left, right].

        :param left: The start of the range (inclusive).
        :param right: The end of the range (inclusive).
        :return: The bitwise AND of all numbers in the range.
        """
        # Calculate the range between right and left
        range_diff = right - left
        
        # If the range is 0, the result is the same as 'left'
        if range_diff == 0:
            return left
        
        # Initialize variables
        shift = 0
        acc = 0
        
        # Keep shifting left and right until they are the same
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # After the loop, 'left' and 'right' should be the same, containing only the common prefix
        return left << shift

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Range includes multiple numbers
    left1, right1 = 5, 7
    expected_output1 = 4
    assert solution.rangeBitwiseAnd(left1, right1) == expected_output1, f"Test case 1 failed: expected {expected_output1}, got {solution.rangeBitwiseAnd(left1, right1)}"
    print(f"Test case 1 passed: {solution.rangeBitwiseAnd(left1, right1)} == {expected_output1}")

    # Test case 2: Range is a single number
    left2, right2 = 1, 1
    expected_output2 = 1
    assert solution.rangeBitwiseAnd(left2, right2) == expected_output2, f"Test case 2 failed: expected {expected_output2}, got {solution.rangeBitwiseAnd(left2, right2)}"
    print(f"Test case 2 passed: {solution.rangeBitwiseAnd(left2, right2)} == {expected_output2}")
