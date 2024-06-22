from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        diff = float('inf')
        for i in range(n):
            lo = i+1
            hi = n-1
            while lo < hi:
                sm = nums[i] + nums[lo] + nums[hi]
                if abs(target - sm) < abs(diff):
                    diff = target - sm
                if target > sm:
                    lo+=1
                else:
                    hi-=1
        return target - diff