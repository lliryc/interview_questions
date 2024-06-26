from typing import List
import heapq
import sys

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        This function finds the smallest range that includes at least one number 
        from each of the k lists.
        
        :param nums: List of k sorted lists of integers
        :return: List containing the smallest range [start, end]
        """
        k = len(nums)  # Number of lists
        mn = sys.maxsize  # Initialize the minimum value to the maximum possible value
        mx = -sys.maxsize  # Initialize the maximum value to the minimum possible value
        wa = []  # Working array (min-heap) to store the current elements
        
        # Initialize the heap and find the initial min and max
        for i in range(k):
            num = nums[i].pop(0)
            heapq.heappush(wa, (num, i))
            mn = min(mn, num)
            mx = max(mx, num)
        
        # Initialize the smallest range
        tmn, tmx = mn, mx
        
        while True:
            # Extract the smallest element from the heap
            num, i = heapq.heappop(wa)
            
            # If any list is exhausted, return the current smallest range
            if len(nums[i]) == 0:
                return [mn, mx]
            
            # Add the next element from the same list to the heap
            num = nums[i].pop(0)
            heapq.heappush(wa, (num, i))
            
            # Update the current min and max
            tmn = wa[0][0]  # The new minimum element in the heap
            tmx = max(tmx, num)  # The current maximum element
            
            # Update the smallest range if a smaller one is found
            if tmx - tmn < mx - mn:
                mx, mn = tmx, tmn
        
        return [mx, mn]

# Example usage
sol = Solution()
print(sol.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
