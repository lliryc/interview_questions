from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        cnt = 0
        for i in range(n-2):
            lo = i+1
            hi = n-1
            while lo < hi:
                if nums[i] + nums[lo] + nums[hi] < target:
                    cnt += hi - lo
                    lo+=1
                else:
                    hi -= 1
        return cnt

sol = Solution()
print(sol.threeSumSmaller(nums = [-2,0,1,3], target = 2))
