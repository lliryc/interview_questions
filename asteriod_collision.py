from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Simulate collisions between asteroids and return the state of asteroids after all collisions.
        
        Args:
        asteroids (List[int]): A list of integers representing the asteroids. 
                               Positive values are moving right, negative values are moving left.
        
        Returns:
        List[int]: The state of the asteroids after all collisions.
        """
        output = []  # List to store the result
        stack = []   # Stack to manage asteroids moving right

        for ast in asteroids:
            if ast < 0:  # Asteroid moving left
                # Resolve collisions with asteroids moving right
                while stack and stack[-1] < -ast:
                    stack.pop()  # Right-moving asteroid explodes
                if not stack:
                    output.append(ast)  # No right-moving asteroid to collide with
                elif stack[-1] == -ast:
                    stack.pop()  # Both asteroids explode
            else:
                stack.append(ast)  # Asteroid moving right

        # Append remaining right-moving asteroids to output
        output += stack
        return output

if __name__ == "__main__":
    s = Solution()
    # Test cases
    print(s.asteroidCollision([-2, -1, 1, 2]))   # Output: [-2, -1, 1, 2]
    print(s.asteroidCollision([5, 10, -5]))      # Output: [5, 10]
    print(s.asteroidCollision([10, 2, -5]))      # Output: [10]





