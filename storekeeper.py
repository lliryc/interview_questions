from typing import List
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        man_loc = None
        block_loc = None
        shape = (len(grid), len(grid[0]))
        for j in range(shape[0]):
            for i in range(shape[1]):
                if grid[j][i] == 'S':
                    man_loc = (i,j)
                    grid[j][i] = '.'
                elif grid[j][i] == 'B':
                    block_loc = (i,j)
                    grid[j][i] = '.'
                if man_loc is not None and block_loc is not None:
                    break
        if man_loc is None and block_loc is None:
            return -1
        moves = self.bfs(man_loc, block_loc, grid, shape)
        return moves

    def check(self, p, shape):
        return 0 <= p[0] < shape[1] and 0 <= p[1] < shape[0]

    def bfs(self, man_loc, block_loc, grid, shape):
        MAX = 2 ** 32
        st = (man_loc, block_loc)
        visited = {st: 0}
        queue = [st]
        minres = MAX
        while len(queue) > 0:
            st = queue.pop(0)
            (man_loc, block_loc) = st
            # move bloc
            minres = self.move_block(man_loc, block_loc, grid, shape, queue, visited, minres)
            # move man
            self.move_man(man_loc, block_loc, grid, shape, queue, visited)
        return -1 if minres == MAX else minres

    def move_man(self, man_loc, block_loc, grid, shape, queue, visited):
        for m in self.moves():
            cman_loc = self.sum(man_loc, m)
            if cman_loc == block_loc:
                continue
            if self.check(cman_loc, shape):
                cst = (cman_loc, block_loc)
                if cst in visited and visited[cst] <= visited[(man_loc, block_loc)]:
                    continue
                c = grid[cman_loc[1]][cman_loc[0]]
                if c == '.' or c == 'T':
                    cst = (cman_loc, block_loc)
                    queue.append(cst)
                    visited[cst] = visited[(man_loc, block_loc)]

    def move_block(self, man_loc, block_loc, grid, shape, queue, visited, minres):
        if self.mhd(man_loc, block_loc) != 1:
            return minres
        block_move = self.sum((block_loc[0] - man_loc[0], block_loc[1] - man_loc[1]), block_loc)
        if self.check(block_move, shape) and (grid[block_move[1]][block_move[0]] == '.' or grid[block_move[1]][block_move[0]] == 'T'):
            #move block
            cman_loc = block_loc
            cblock_loc = block_move
            cst = (cman_loc, cblock_loc)
            if cst in visited and visited[cst] <= visited[(man_loc, block_loc)] + 1:
                return minres
            visited[cst] = visited[(man_loc, block_loc)] + 1
            if grid[cblock_loc[1]][cblock_loc[0]] == 'T':
                minres = min(minres, visited[cst])
            else:
                queue.append(cst)
        return minres

    def mhd(self, p1, p2):
        d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        return d
    def moves(self):
        return [(-1,0), (1,0), (0,1), (0,-1)]
    def sum(self, p1, p2):
        return tuple([sum(x) for x in zip(p1, p2)])

s = Solution()
# print(s.minPushBox([["#","#","#","#","#","#"],
#                ["#","T","#","#","#","#"],
#                ["#",".",".","B",".","#"],
#                ["#",".","#","#",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]))
# print(s.minPushBox([["#","#","#","#","#","#"],
#                     ["#","T",".",".","#","#"],
#                     ["#",".","#","B",".","#"],
#                     ["#",".",".",".",".","#"],
#                     ["#",".",".",".","S","#"],
#                     ["#","#","#","#","#","#"]]))
print(s.minPushBox([["#",".",".",".",".",".",".",".",".","."],
                    [".",".",".",".",".","#",".",".",".","#"],
                    ["#",".","#",".",".","T",".",".",".","."],
                    [".","#",".",".",".",".",".",".",".","."],
                    [".",".",".",".",".",".","#",".",".","."],
                    [".",".",".","#","#","S",".","B",".","."],
                    ["#",".",".",".",".",".",".","#",".","."],
                    [".","#",".",".",".",".",".",".",".","."],
                    [".",".",".",".",".",".",".",".",".","."],
                    [".",".",".",".",".","#",".",".",".","."]]))
