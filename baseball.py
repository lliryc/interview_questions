from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        """
        Calculate the sum of the points based on the operations provided.
        
        Args:
        ops (List[str]): A list of strings representing operations.
        
        Returns:
        int: The sum of all the points after performing the operations.
        """
        # Stack to keep track of the points
        points_stack = []
        
        for operation in ops:
            if operation == 'C':
                # Remove the last score
                points_stack.pop()
            elif operation == 'D':
                # Double the last score and add to the stack
                points_stack.append(points_stack[-1] * 2)
            elif operation == '+':
                # Sum the last two scores and add to the stack
                points_stack.append(points_stack[-1] + points_stack[-2])
            else:
                # Convert the operation to an integer and add to the stack
                points_stack.append(int(operation))
        
        # Return the sum of all points
        return sum(points_stack)

# Example usage
sol = Solution()
print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # Output should be 27

