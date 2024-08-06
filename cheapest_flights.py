import sys
from typing import List
from collections import defaultdict
import unittest

class Solution:
    """
    A class to find the cheapest price from a source to a destination with at most k stops.
    """

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Find the cheapest price from src to dst with at most k stops.

        Args:
            n (int): Number of cities.
            flights (List[List[int]]): List of flights, where each flight is [from, to, price].
            src (int): Source city.
            dst (int): Destination city.
            k (int): Maximum number of stops.

        Returns:
            int: The cheapest price, or -1 if no such route exists.
        """
        self.flights = defaultdict(list)
        for s, d, r in flights:
            self.flights[s].append([d, r])
            self.flights[s] = sorted(self.flights[s], key=lambda x: x[1])
        
        self.n = n
        self.src = src
        self.dst = dst
        self.minprice = sys.maxsize
        self.k = k
        
        self.find([src], dst, 0, 0, {})
        return -1 if self.minprice == sys.maxsize else self.minprice

    def find(self, route: List[int], dst: int, hops: int, price: int, route_d: dict) -> int:
        """
        Recursive helper function to find the cheapest price.

        Args:
            route (List[int]): Current route.
            dst (int): Destination city.
            hops (int): Number of stops so far.
            price (int): Current price.
            route_d (dict): Dictionary to keep track of visited cities.

        Returns:
            int: The minimum price found so far.
        """
        if hops - 1 > self.k:
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

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), 200)

    def test_example2(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), 500)

    def test_no_route(self):
        n = 3
        flights = [[0,1,100],[1,2,100]]
        src = 0
        dst = 3
        k = 1
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), -1)

    def test_complex_case(self):
        n = 10
        flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
        src = 6
        dst = 0
        k = 7
        self.assertEqual(self.solution.findCheapestPrice(n, flights, src, dst, k), 14)

if __name__ == '__main__':
    unittest.main()
