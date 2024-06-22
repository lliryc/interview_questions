from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        Count the number of triplets in the array such that the sum of the triplet is less than the target.

        :param nums: List of integers.
        :param target: The target sum.
        :return: The number of triplets with a sum less than the target.
        """
        # Sort the array to use the two-pointer technique
        nums = sorted(nums)
        n = len(nums)
        count = 0

        # Iterate through each number, treating it as the first number of the triplet
        for i in range(n - 2):
            lo = i + 1
            hi = n - 1
            while lo < hi:
                # Check if the sum of the current triplet is less than the target
                if nums[i] + nums[lo] + nums[hi] < target:
                    # If true, all triplets between lo and hi are valid
                    count += hi - lo
                    lo += 1  # Move the lower pointer to the right
                else:
                    hi -= 1  # Move the upper pointer to the left if the sum is greater or equal to the target

        return count

# Example usage
sol = Solution()
print(sol.threeSumSmaller(nums=[-2, 0, 1, 3], target=2))  # Output: 2
