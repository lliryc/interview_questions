from typing import List
import heapq
import sys

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        mn = sys.maxsize
        mx = -sys.maxsize
        wa = []
        for i in range(k):
            num = nums[i].pop(0)
            heapq.heappush(wa, (num, i))
            mn = min(mn, num)
            mx = max(mx, num)
        tmn, tmx = mn, mx
        while True:
            (num, i) = heapq.heappop(wa)
            if len(nums[i]) == 0:
                return [mn, mx]
            num = nums[i].pop(0)
            heapq.heappush(wa, (num, i))
            tmn = wa[0][0]
            tmx = max(tmx, num)
            if tmx - tmn < mx - mn:
                mx, mn = tmx, tmn
        return [mx, mn]

sol = Solution()

print(sol.smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]]))