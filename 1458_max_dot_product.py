from typing import List
import sys
from functools import cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        def removeZeros(nums):
            nnums = []
            for num in nums:
                if num == 0:
                    continue
                nnums.append(num)
            return nnums
        nums1 = removeZeros(nums1)
        n = len(nums1)
        nums2 = removeZeros(nums2)
        m = len(nums2)
        matrix = [[nums1[i] * nums2[j] for j in range(m)] for i in range(n)]
        @cache
        def max_prod(i, j):
            if i >= n or j >= m:
                return 0
            mx = -sys.maxsize
            for i1 in range(i, n):
                for j1 in range(j, m):
                    sm = matrix[i1][j1] + max_prod(i1 + 1, j1 + 1)
                    mx = max(sm,matrix[i1][j1], mx)
            return mx
        return max_prod(0, 0)

sol = Solution()
print(sol.maxDotProduct(nums1 = [-96,1,-86,-98,-69,-43,-49,-2,-34,91,52,61,-49,-13,-11,94,-88,-60,-48,9,-81,86,-72,90,37,60,-31,-93,43,-81,89,8,-72,70,-14,-76,32,11,1,-45,-39,-26,70,84,82,95,51,90,-55,-37,-26,-87,-49,8,30,82,59,-30,46,72,44,36,27,28,75,70,99,57,46,86,-49,-98,-18,-57,90,-89,-41,85,-87,88,16,-53,93,-99,35,44,91,5,-99,23],
                        nums2 = [-54,-31,17,-43,-21,87,29,75,45,74,-9,-3,16,97,27,-11,-86,-84,-81,-44,68,88,-2,-62,85,0,37,7,53,-5,-45,17,-26,-37,61,-12,34,-36,45,-58,78,66,-37,-71,43,99,-54,-81,69,-39,-50,51,-26]))