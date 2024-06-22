from typing import List
from collections import Counter
import math

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        Count the number of ways to choose three elements from the array such that their sum equals the target.

        :param arr: List of integers.
        :param target: The target sum.
        :return: The number of ways to choose three elements that sum up to the target.
        """
        # Frequency dictionary to count occurrences of each element
        freqd = Counter(arr)
        # Sorted unique elements of the array
        arr = sorted(list(freqd.keys()))
        # Dictionary to map each element to its position in the sorted array
        posd = {c: i for i, c in enumerate(arr)}
        n = len(arr)
        count = 0

        # Case 1: All three elements are the same
        if target % 3 == 0:
            count += math.comb(freqd[target // 3], 3)
        
        # Case 2: Two elements are the same, one is different
        for i, item in enumerate(arr):
            key1 = target - 2 * item
            if key1 in posd and posd[key1] > i:
                count += math.comb(freqd[item], 2) * freqd[key1]
            
            if (target - item) % 2 == 0 and not (target % 3 == 0 and target // 3 == item):
                key2 = (target - item) // 2
                if key2 in posd and posd[key2] > i:
                    count += math.comb(freqd[key2], 2) * freqd[item]
        
        # Case 3: All three elements are different
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                key = target - arr[i] - arr[j]
                if key in posd and posd[key] > j:
                    count += freqd[arr[i]] * freqd[arr[j]] * freqd[key]
        
        return count

# Example usage
sol = Solution()
print(sol.threeSumMulti([3, 3, 3, 0], 6))  # Example 1
print(sol.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))  # Example 2
print(sol.threeSumMulti([1, 1, 2, 2, 2, 2], 5))  # Example 3
