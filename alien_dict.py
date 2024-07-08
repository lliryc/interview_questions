from typing import List
from collections import defaultdict
class Solution:

    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""
        if len(words) == 1:
            return "".join(list(set(words[0])))
        self.income_edges = defaultdict(int)
        self.edges = defaultdict(lambda: set([]))
        alphabet = set(words[0])
        for i in range(1, len(words)):
            if not self.set_edges(words[i-1], words[i]):
                return ""
            alphabet = alphabet.union(set(words[i]))
        vertexes = []
        for c in alphabet:
            if c not in self.income_edges:
                self.income_edges[c] = 0
                vertexes.append(c)
        return self.traversal(vertexes)

    def set_edges(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        if l1 < l2 and word1 == word2[:l1]:
            return True
        if l1 > l2 and word1[:l2] == word2:
            return False
        l = min(l1, l2)
        for i in range(l):
            if word1[i] != word2[i]:
                c1 = word1[i]
                c2 = word2[i]
                if c2 not in self.edges[c1]:
                    self.edges[c1].add(c2)
                    self.income_edges[c2] += 1
                break
        return True

    def traversal(self, vertexes):
        order = []
        while True:
            new_vertexes = []
            if len(vertexes) == 0:
                break
            order.extend(vertexes)
            for v in vertexes:
                del self.income_edges[v]
                nns = self.edges[v]
                for nv in nns:
                    self.income_edges[nv] -= 1
                    if self.income_edges[nv] == 0:
                        new_vertexes.append(nv)
            vertexes = new_vertexes
        if len(self.income_edges) > 0:
            return ""
        return "".join(order)

s = Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))


