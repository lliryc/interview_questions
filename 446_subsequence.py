from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0
        # Use a defaultdict of defaultdicts to store the count of arithmetic slices ending at each index with a given difference
        mem = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                previous_count = mem[j][diff]
                mem[i][diff] += previous_count + 1
                total_count += previous_count

        return total_count

# Example usage
sol = Solution()
print(sol.numberOfArithmeticSlices([1, 2, 1, 2, 4, 1, 5, 10]))  # Example 1
print(sol.numberOfArithmeticSlices([2, 4, 6, 8, 10]))  # Example 2
