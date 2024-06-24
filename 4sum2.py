from typing import List
from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        nums = [nums1, nums2, nums3, nums4]
        nl = len(nums)
        numsd = [Counter(nums[i]) for i in range(nl)]
        nnumsd = []
        ld = {}
        for key0 in numsd[0]:
            for key1 in numsd[1]:
                key = key0 + key1
                ld[key] = ld.get(key, 0) + numsd[0][key0]*numsd[1][key1]
        nnumsd.append(ld)
        rd = {}
        for key0 in numsd[-1]:
            for key1 in numsd[-2]:
                key = key0 + key1
                rd[key] = rd.get(key, 0) + numsd[-1][key0]*numsd[-2][key1]
        nnumsd.append(rd)
        d = {}
        for key0 in nnumsd[0]:
            for key1 in nnumsd[1]:
                key = key0 + key1
                d[key] = d.get(key, 0) + nnumsd[0][key0]*nnumsd[1][key1]
        return d.get(0, 0)

s = Solution()
print(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))



