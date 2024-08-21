from typing import List

class Solution:
    E = 0
    S = 1
    W = 2
    N = 3

    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        self.m = len(room)
        self.n = len(room[0])
        self.room = room
        self.rooms = 0
        self.visited = [[[0 for k in range(4)] for i in range(self.n)] for j in range(self.m)]
        self.run(0,0,0)
        return self.rooms

    def run(self, r, c, d):
        while True:
            if self.visited[r][c][d] == 1:
                break
            self.visited[r][c][d] = 1
            if self.room[r][c] == 0:
                self.rooms += 1
                self.room[r][c] = 2
            while True:
                nr, nc = self.next(r, c, d)
                if self.possible(nr, nc):
                    r, c = nr, nc
                    break
                else:
                    d = (d + 1) % 4
                if self.visited[r][c][d] == 1:
                    break
        return

    def next(self, r, c, d):
        if d == self.E:
            c += 1
        elif d == self.S:
            r += 1
        elif d == self.W:
            c -= 1
        elif d == self.N:
            r -= 1
        return r, c

    def possible(self, r, c):
        if r < 0 or r >= self.m:
            return False
        if c < 0 or c >= self.n:
            return False
        return self.room[r][c] != 1

s = Solution()
print(s.numberOfCleanRooms([[0,0,0],[0,0,1]]))




