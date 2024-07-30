from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        if n == 2:
            if ratings[0] != ratings[1]:
                return 3
            return 2
        candies = [None] * n
        nodes = []
        if ratings[0] <= ratings[1]:
            nodes.append((0, 1))
        if ratings[n-1] <= ratings[n-2]:
            nodes.append((n-1, 1))
        for i in range(1, n-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                nodes.append((i, 1))
        while len(nodes):
            new_nodes = []
            for i, c in nodes:
                candies[i] = c
                if i > 0 and ratings[i-1] > ratings[i]:
                    new_nodes.append((i-1, c+1))
                if i < n-1 and ratings[i+1] > ratings[i]:
                    new_nodes.append((i+1, c+1))
            nodes = new_nodes
        return sum(candies)

sol = Solution()
print(sol.candy([1,2,2]))

