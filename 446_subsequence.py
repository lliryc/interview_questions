from typing import List
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        mem = defaultdict(lambda:defaultdict(int))
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                pcnt = mem[j][diff]
                mem[i][diff] = mem[i][diff] + pcnt + 1
                cnt += pcnt
        return cnt

sol = Solution()

print(sol.numberOfArithmeticSlices([1,2,1,2,4,1,5,10]))

print(sol.numberOfArithmeticSlices([2,4,6,8,10]))
