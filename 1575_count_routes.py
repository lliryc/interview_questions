from typing import List
from functools import cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7
        @cache
        def find_route(i, cf):
            if cf < 0:
                return 0
            cnt = 0
            if i == finish:
                cnt += 1
            for j in range(len(locations)):
                if i == j:
                    continue
                cnt+=find_route(j, cf - abs(locations[i] - locations[j]))
            return cnt % mod

        return find_route(start, fuel)

sol = Solution()
print(sol.countRoutes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5))
