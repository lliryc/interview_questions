from typing import List
from functools import lru_cache

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        self.grid = grid
        r = len(grid)
        c = len(grid[0])
        cnt = 0
        for i in range(1, r):
            pos = None
            for j in range(c):
                if self.grid[i][j] == 1:
                    if pos is None:
                        pos = j
                    l = j - pos + 1
                    if 3 <= l:
                        l = l - 1 if l % 2 == 0 else l
                        for k in range(min(l, 2 * i + 1), 1, -2):
                            cnt += int(self.pyramid(i, j, k))
                else:
                    pos = None
        Solution.pyramid.cache_clear()
        for i in range(r - 2, -1, -1):
            pos = None
            for j in range(c):
                if self.grid[i][j] == 1:
                    if pos is None:
                        pos = j
                    l = j - pos + 1
                    if 3 <= l:
                        l = l - 1 if l % 2 == 0 else l
                        for k in range(min(l, 2 * (r - 1 - i) + 1), 1, -2):
                            cnt += int(self.inv_pyramid(i, j, k))
                else:
                    pos = None
        Solution.inv_pyramid.cache_clear()
        return cnt


    @lru_cache
    def pyramid(self, i, j, l):
        if l == 1:
            return self.grid[i][j] == 1
        return self.pyramid(i, j, l - 2) and self.pyramid(i - 1, j - 1, l - 2)

    @lru_cache
    def inv_pyramid(self, i, j, l):
        if l == 1:
            return self.grid[i][j] == 1
        return self.inv_pyramid(i, j, l - 2) and self.inv_pyramid(i + 1, j - 1, l - 2)



sol = Solution()
print(sol.countPyramids([[0,1,1],
                         [1,1,1],
                         [1,0,1],
                         [1,1,1]]))
#print(sol.countPyramids(grid = [[1,1,1],[1,1,1]]))
#print(sol.countPyramids(grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]))


