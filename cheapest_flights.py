import sys
from typing import List
from collections import defaultdict

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.flights = defaultdict(list)
        for s, d, r in flights:
            self.flights[s].append([d, r])
            self.flights[s] = list(sorted(self.flights[s], key=lambda x: x[1]))
        self.n = n
        self.src = src
        self.dst = dst
        self.minprice = sys.maxsize
        self.k = k
        self.find([src], dst, 0, 0, {})
        return -1 if self.minprice >= sys.maxsize else self.minprice

    def find(self, route, dst, hops, price, route_d):
        if hops-1 > self.k:
            return self.minprice
        if price > self.minprice or route[-1] in route_d:
            return self.minprice

        if route[-1] == dst:
            self.minprice = min(self.minprice, price)
            return self.minprice

        route_d[route[-1]] = True

        for s, d in self.flights[route[-1]]:
            route.append(s)
            self.find(route, dst, hops + 1, price + d, route_d)
            route.pop()

        del route_d[route[-1]]

        return self.minprice

s = Solution()
#print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
print(s.findCheapestPrice(10, [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]], 6, 0, 7))
