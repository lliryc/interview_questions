from typing import List
from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Determines the order of characters in an alien language given a sorted dictionary of words.

        Args:
        words (List[str]): A list of words sorted in the alien language.

        Returns:
        str: A string representing the order of characters in the alien language.
        """
        if len(words) == 0:
            return ""
        if len(words) == 1:
            return "".join(list(set(words[0])))

        # Initialize dictionaries for counting incoming edges and storing adjacency lists
        self.income_edges = defaultdict(int)
        self.edges = defaultdict(set)

        # Collect all unique characters
        alphabet = set(words[0])
        for i in range(1, len(words)):
            if not self.set_edges(words[i - 1], words[i]):
                return ""
            alphabet = alphabet.union(set(words[i]))

        # Collect vertices with no incoming edges
        vertexes = [c for c in alphabet if c not in self.income_edges]
        for c in alphabet:
            if c not in self.income_edges:
                self.income_edges[c] = 0

        return self.traversal(vertexes)

    def set_edges(self, word1: str, word2: str) -> bool:
        """
        Sets the directed edges between characters of two words based on their order.

        Args:
        word1 (str): The first word.
        word2 (str): The second word.

        Returns:
        bool: True if edges were set successfully, False if there's a conflict.
        """
        l1, l2 = len(word1), len(word2)
        if l1 < l2 and word1 == word2[:l1]:
            return True
        if l1 > l2 and word1[:l2] == word2:
            return False

        l = min(l1, l2)
        for i in range(l):
            if word1[i] != word2[i]:
                c1, c2 = word1[i], word2[i]
                if c2 not in self.edges[c1]:
                    self.edges[c1].add(c2)
                    self.income_edges[c2] += 1
                break
        return True

    def traversal(self, vertexes: List[str]) -> str:
        """
        Performs a topological sort on the graph to determine the character order.

        Args:
        vertexes (List[str]): List of characters with no incoming edges.

        Returns:
        str: A string representing the order of characters, or an empty string if there's a cycle.
        """
        order = []
        while vertexes:
            new_vertexes = []
            order.extend(vertexes)
            for v in vertexes:
                del self.income_edges[v]
                for nv in self.edges[v]:
                    self.income_edges[nv] -= 1
                    if self.income_edges[nv] == 0:
                        new_vertexes.append(nv)
            vertexes = new_vertexes

        if self.income_edges:
            return ""

        return "".join(order)

# Example usage
s = Solution()
print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
