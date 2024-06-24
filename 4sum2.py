from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        Counts the number of tuples (i, j, k, l) such that:
        nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
        
        Args:
        nums1: List[int] - The first list of integers.
        nums2: List[int] - The second list of integers.
        nums3: List[int] - The third list of integers.
        nums4: List[int] - The fourth list of integers.
        
        Returns:
        int - The count of tuples (i, j, k, l) that satisfy the condition.
        """
        
        # Count the sums of all pairs from nums1 and nums2
        count_ab = Counter(a + b for a in nums1 for b in nums2)
        
        # Count the sums of all pairs from nums3 and nums4 and check against count_ab
        count = sum(count_ab[-c - d] for c in nums3 for d in nums4)
        
        return count

# Example usage:
s = Solution()
result = s.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2])
print(result)  # Output: 2



