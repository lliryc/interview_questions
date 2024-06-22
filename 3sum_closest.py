from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Finds the sum of three integers in nums such that the sum is closest to the given target.

        :param nums: List of integers.
        :param target: The target sum.
        :return: The sum of the three integers closest to the target.
        """
        # Sort the list to enable the two-pointer technique
        nums = sorted(nums)
        n = len(nums)
        # Initialize the difference to a large value
        closest_diff = float('inf')
        
        for i in range(n):
            lo = i + 1
            hi = n - 1
            
            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]
                # Update closest_diff if the current sum is closer to the target
                if abs(target - current_sum) < abs(closest_diff):
                    closest_diff = target - current_sum
                
                # Adjust pointers based on comparison with the target
                if current_sum < target:
                    lo += 1
                else:
                    hi -= 1
        
        # Return the sum closest to the target
        return target - closest_diff

# Example usage
sol = Solution()
print(sol.threeSumClosest([1, 2, 4, 5, 6], 10))  # Example 1
print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Example 2
