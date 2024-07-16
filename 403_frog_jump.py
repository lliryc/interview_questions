from collections import defaultdict

class Solution(object):
    def canCross(self, stones):
        """
        Determines if the frog can cross the river by jumping on stones.
        
        Parameters:
        stones (List[int]): Positions of the stones in the river.
        
        Returns:
        bool: True if the frog can cross, False otherwise.
        """
        # Convert the list of stones to a set for O(1) lookups
        stone_positions = set(stones)
        # Dictionary to store the possible jump distances from each stone
        jumps = defaultdict(set)
        # The frog starts on the first stone, it can jump to the second stone with distance 1
        jumps[1] = {1}
        # The position of the last stone
        last_stone = stones[-1]
        
        # Iterate over the stones starting from the second one
        for stone in stones[1:]:
            # If the last stone is already in the jumps dictionary, return True
            if last_stone in jumps:
                return True
            # If the current stone is not in the jumps dictionary, skip it
            if stone not in jumps:
                continue
            
            # Get the possible jump distances from the current stone
            possible_jumps = jumps[stone]
            # Remove the current stone from the dictionary to avoid revisiting
            del jumps[stone]
            
            # For each possible jump distance, calculate the next stone positions
            for jump in possible_jumps:
                # Check the three possible jump distances: k-1, k, and k+1
                if (stone + jump - 1) in stone_positions:
                    jumps[stone + jump - 1].add(jump - 1)
                if (stone + jump) in stone_positions:
                    jumps[stone + jump].add(jump)
                if (stone + jump + 1) in stone_positions:
                    jumps[stone + jump + 1].add(jump + 1)
        
        # If we exit the loop without returning, the frog cannot cross the river
        return False

# Create an instance of the Solution class
solution = Solution()

# Test cases
print(f'Test 1 = {solution.canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17]) == True}')
print(f'Test 2 = {solution.canCross(stones=[0, 1, 2, 3, 4, 8, 9, 11]) == False}')
print(f'Test 3 = {solution.canCross(stones=[0, 1, 3, 6, 10, 15, 16, 21]) == True}')
